from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Use PostgreSQL on Render, SQLite locally
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./ecomm_intel.db")

# Fix for Render PostgreSQL URL format
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Different settings for SQLite vs PostgreSQL
if "sqlite" in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class AnalysisRecord(Base):
    __tablename__ = "analysis_records"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    your_price = Column(Float)
    competitor_price = Column(Float)
    review = Column(String)
    sentiment = Column(String)
    sentiment_score = Column(Float)
    pricing_insight = Column(String)
    recommendation = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class PriceHistory(Base):
    __tablename__ = "price_history"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    your_price = Column(Float)
    competitor_price = Column(Float)
    sentiment_score = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()