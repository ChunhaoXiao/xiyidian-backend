from typing import List
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import String,DateTime,ForeignKey
import datetime
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class ClothOrder(Base):
    __tablename__ = 'orders'
    id:Mapped[int] = mapped_column(primary_key=True)
    openid:Mapped[str] = mapped_column(String(100))
    status:Mapped[str] = mapped_column(String(20),default="1")
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    confirmed_at:Mapped[datetime.datetime] = mapped_column(nullable=True)
    items:Mapped[List["ClothItem"]] = relationship(back_populates="order")
    
class ClothItem(Base):
    __tablename__ = 'order_items'
    id:Mapped[int] = mapped_column(primary_key=True)
    order_id:Mapped[int] = mapped_column(ForeignKey("orders.id"))
    cate_id:Mapped[int]
    quantity:Mapped[int]
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    order:Mapped["ClothOrder"] = relationship(back_populates="items")
    
class Token(Base):
    __tablename__ = "token"
    id:Mapped[int] = mapped_column(primary_key=True)
    token_value:Mapped[str] = mapped_column(String(300))
    updated_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    
    
    
    
    