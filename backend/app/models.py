from sqlalchemy import Column, String, Boolean, Text, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True)
    email = Column(String(150), unique=True)
    password_hash = Column(Text, nullable=False)
    role = Column(String(20), default='shopper')
    is_verified = Column(Boolean, default=False)
    avatar_url = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    icon_url = Column(Text)
    parent_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'))

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'))
    unit = Column(String(50))
    image_url = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    business_name = Column(String(150), nullable=False)
    description = Column(Text)
    market_name = Column(String(150))
    address = Column(Text)
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))
    is_verified = Column(Boolean, default=False)
    badge = Column(String(20), default='none')
    created_at = Column(TIMESTAMP, server_default=func.now())

class PriceReport(Base):
    __tablename__ = "price_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    reported_by = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    merchant_id = Column(UUID(as_uuid=True), ForeignKey('merchants.id'))
    price = Column(DECIMAL(12,2), nullable=False)
    currency = Column(String(10), default='NGN')
    quantity = Column(String(50))
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))
    location_name = Column(String(200))
    is_verified = Column(Boolean, default=False)
    expires_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())
