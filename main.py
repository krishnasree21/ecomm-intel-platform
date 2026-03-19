from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from textblob import TextBlob
from sqlalchemy.orm import Session
from database import AnalysisRecord, get_db
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
    existing = db.query(AnalysisRecord).filter(
        AnalysisRecord.product_name == data.product_name
    ).first()

    if existing:
        # Update existing record instead of creating new one
        existing.your_price = data.price
        existing.competitor_price = data.competitor_price
        existing.review = data.review
        existing.sentiment = sentiment
        existing.sentiment_score = round(sentiment_score, 2)
        existing.pricing_insight = pricing_insight
        existing.recommendation = recommendation
        existing.created_at = datetime.utcnow()
        db.commit()
        saved_status = "updated"
    else:
        # Save new record
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
        db.commit()
        saved_status = "new"
        
    return {
        "product": data.product_name,
        "sentiment_score": round(sentiment_score, 2),
        "sentiment": sentiment,
        "pricing_insight": pricing_insight,
        "recommendation": recommendation,
        "record_status": saved_status
    }

# Health check endpoint
@app.get("/")
def home():
    return {"status": "E-Commerce Intelligence API is running successfully"}

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