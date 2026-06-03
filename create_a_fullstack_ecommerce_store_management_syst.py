# Full Stack E-Commerce Store Management System

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, Sequence, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List, Optional

DATABASE_URL = "sqlite:///./ecommerce.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    name = Column(String(100), index=True)
    category = Column(String(100))
    price = Column(Float)
    stock = Column(Integer)
    sku = Column(String(50), unique=True)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
    customer_name = Column(String(100))
    total_amount = Column(Float)
    status = Column(String(50))

Base.metadata.create_all(bind=engine)

# Pydantic Models
class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    stock: int
    sku: str
class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    sku: str
class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float
    status: str
class OrderResponse(BaseModel):
    id: int
    customer_name: str
    total_amount: float
    status: str

# FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Product routes
@app.post('/products/', response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get('/products/', response_model=List[ProductResponse])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@app.get('/products/{product_id}', response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put('/products/{product_id}', response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete('/products/{product_id}', response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted"}

# Order routes
@app.post('/orders/', response_model=OrderResponse)
@app.get('/orders/', response_model=List[OrderResponse])
