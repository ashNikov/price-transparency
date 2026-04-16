from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    slug: str
    icon_url: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: UUID
    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    unit: Optional[str] = None
    category_id: Optional[UUID] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: UUID
    created_at: datetime
    class Config:
        from_attributes = True

class PriceReportBase(BaseModel):
    product_id: UUID
    price: float
    currency: str = 'NGN'
    quantity: Optional[str] = None
    location_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class PriceReportCreate(PriceReportBase):
    pass

class PriceReportResponse(PriceReportBase):
    id: UUID
    is_verified: bool
    created_at: datetime
    class Config:
        from_attributes = True
