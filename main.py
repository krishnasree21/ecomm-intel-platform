from landing import landing_content
from database import AnalysisRecord, PriceHistory, get_db
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from textblob import TextBlob
from sqlalchemy.orm import Session
from templates import html_content
from datetime import datetime

# This creates your API application
app = FastAPI(title="E-Commerce Intelligence API")

# This defines what data the API accepts
class ProductData(BaseModel):
    product_name: str
    price: float
    competitor_price: float
    review: str

# This is your first intelligence endpoint
@app.post("/analyze")
def analyze_product(data: ProductData, db: Session = Depends(get_db)):
    
    # Sentiment analysis
    sentiment_score = TextBlob(data.review).sentiment.polarity
    
    if sentiment_score > 0.2:
        sentiment = "Positive"
    elif sentiment_score < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    # Pricing intelligence
    price_diff = data.competitor_price - data.price
    if price_diff > 0:
        pricing_insight = f"You are ${price_diff:.2f} cheaper than competitor"
    elif price_diff < 0:
        pricing_insight = f"You are ${abs(price_diff):.2f} more expensive than competitor"
    else:
        pricing_insight = "Same price as competitor"

    # Recommendation
    if sentiment == "Positive" and price_diff >= 0:
        recommendation = "Strong position — good reviews and competitive price"
    elif sentiment == "Negative" and price_diff < 0:
        recommendation = "At risk — bad reviews and overpriced"
    elif sentiment == "Positive" and price_diff < 0:
        recommendation = "Good reviews but consider reducing price"
    else:
        recommendation = "Improve product quality and review your pricing"

    # Save to database
    # Check if product already exists in database
    # Check if product already exists
    existing = db.query(AnalysisRecord).filter(
        AnalysisRecord.product_name == data.product_name
    ).first()

    if existing:
        existing.your_price = data.price
        existing.competitor_price = data.competitor_price
        existing.review = data.review
        existing.sentiment = sentiment
        existing.sentiment_score = round(sentiment_score, 2)
        existing.pricing_insight = pricing_insight
        existing.recommendation = recommendation
        existing.created_at = datetime.utcnow()
        saved_status = "updated"
    else:
        record = AnalysisRecord(
            product_name=data.product_name,
            your_price=data.price,
            competitor_price=data.competitor_price,
            review=data.review,
            sentiment=sentiment,
            sentiment_score=round(sentiment_score, 2),
            pricing_insight=pricing_insight,
            recommendation=recommendation
        )
        db.add(record)
        saved_status = "new"

    # Always save to price history — runs for BOTH new and existing
    history_record = PriceHistory(
        product_name=data.product_name,
        your_price=data.price,
        competitor_price=data.competitor_price,
        sentiment_score=round(sentiment_score, 2)
    )
    db.add(history_record)
    db.commit()

    return {
        "product": data.product_name,
        "sentiment_score": round(sentiment_score, 2),
        "sentiment": sentiment,
        "pricing_insight": pricing_insight,
        "recommendation": recommendation
    }


@app.get("/")
def home():
    return {"status": "E-Commerce Intelligence API is running successfully"}

# Health check endpoint
#@app.get("/")
#def home():
 #   return {"status": "E-Commerce Intelligence API is running successfully"}

# Competitor comparison model
class CompetitorData(BaseModel):
    product_name: str
    your_price: float
    competitors: dict

@app.post("/compare")
def compare_competitors(data: CompetitorData):
    
    # Rank all prices together
    all_prices = dict(data.competitors)
    all_prices["Your Product"] = data.your_price
    
    # Sort from cheapest to most expensive
    ranked = sorted(all_prices.items(), key=lambda x: x[1])
    
    # Find your position
    position = [i+1 for i, (name, _) in enumerate(ranked) if name == "Your Product"][0]
    total = len(ranked)
    
    # Generate insight
    if position == 1:
        insight = "You are the CHEAPEST in the market — strong competitive position"
    elif position <= total // 2:
        insight = f"You rank {position} out of {total} — competitive pricing"
    else:
        insight = f"You rank {position} out of {total} — consider reducing price"

    return {
        "product": data.product_name,
        "your_price": data.your_price,
        "market_ranking": f"{position} out of {total}",
        "insight": insight,
        "full_ranking": [{"rank": i+1, "name": n, "price": p} for i, (n, p) in enumerate(ranked)]
    }


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return html_content


@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    records = db.query(AnalysisRecord).order_by(AnalysisRecord.created_at.desc()).all()
    return [
        {
            "product_name": r.product_name,
            "your_price": r.your_price,
            "competitor_price": r.competitor_price,
            "sentiment": r.sentiment,
            "sentiment_score": r.sentiment_score,
            "pricing_insight": r.pricing_insight,
            "recommendation": r.recommendation,
            "created_at": str(r.created_at)
        }
        for r in records
    ]
@app.get("/trend/{product_name}")
def get_price_trend(product_name: str, db: Session = Depends(get_db)):
    records = db.query(PriceHistory).filter(
        PriceHistory.product_name == product_name
    ).order_by(PriceHistory.recorded_at.asc()).all()
    
    return [
        {
            "date": str(r.recorded_at),
            "your_price": r.your_price,
            "competitor_price": r.competitor_price,
            "sentiment_score": r.sentiment_score
        }
        for r in records
    ]

@app.get("/score/{product_name}")
def get_product_score(product_name: str, db: Session = Depends(get_db)):
    record = db.query(AnalysisRecord).filter(
        AnalysisRecord.product_name == product_name
    ).first()

    if not record:
        return {"error": "Product not found"}

    score = 5.0
    score += record.sentiment_score * 3
    price_diff = record.competitor_price - record.your_price
    if price_diff > 20:
        score += 2
    elif price_diff > 10:
        score += 1.5
    elif price_diff > 0:
        score += 1
    elif price_diff < -20:
        score -= 2
    elif price_diff < -10:
        score -= 1.5
    elif price_diff < 0:
        score -= 1

    score = max(0, min(10, round(score, 1)))

    if score >= 8:
        label = "Excellent"
        color = "#22c55e"
    elif score >= 6:
        label = "Good"
        color = "#3b82f6"
    elif score >= 4:
        label = "Average"
        color = "#f59e0b"
    else:
        label = "Poor"
        color = "#ef4444"

    return {
        "product": record.product_name,
        "score": score,
        "label": label,
        "color": color,
        "sentiment_score": record.sentiment_score,
        "price_difference": round(price_diff, 2)
    }

@app.get("/fetch-price/{product_name}")
async def fetch_competitor_price(product_name: str):
    from price_data import find_product_price
    
    result = find_product_price(product_name)
    
    if result:
        import random
        # Return a competitor price from our database
        competitors = result.get("competitors", {})
        if competitors:
            comp_name = list(competitors.keys())[0]
            comp_price = list(competitors.values())[0]
            # Add slight variation to make it realistic
            varied_price = comp_price
            return {
                "product": product_name,
                "suggested_price": varied_price,
                "competitor_name": comp_name,
                "source": "Market Price Database",
                "status": "found",
                "all_competitors": competitors
            }
    
    return {
        "product": product_name,
        "suggested_price": None,
        "message": "Product not in database. Please enter price manually.",
        "status": "not_found"
    }