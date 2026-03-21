from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Creates a database file called ecomm_intel.db on your computer
SQLALCHEMY_DATABASE_URL = "sqlite:///./ecomm_intel.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This is your database table — every analysis gets saved here
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

# Creates the table automatically
Base.metadata.create_all(bind=engine)

class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    your_price = Column(Float)
    competitor_price = Column(Float)
    sentiment_score = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)

# Update tables
Base.metadata.create_all(bind=engine)

# Gets a database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()