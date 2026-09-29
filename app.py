from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String
from database import engine, SessionLocal, Base

app = FastAPI()


# ---- DB Model ----
class OrderTable(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String)
    quantity = Column(Integer)
    status = Column(String, default="created", nullable=False)


Base.metadata.create_all(bind=engine)


# ---- Pydantic ----
class Order(BaseModel):
    product: str = Field(min_length=1)
    quantity: int


class OrderStatusUpdate(BaseModel):
    status: str


# ---- Health ----
@app.get("/health")
def health():
    return {"status": "ok"}


# ---- Create Order ----
@app.post("/orders")
def create_order(order: Order):
    db = SessionLocal()

    db_order = OrderTable(
        product=order.product,
        quantity=order.quantity,
        status="created"
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    db.close()

    return {
        "id": db_order.id,
        "product": db_order.product,
        "quantity": db_order.quantity,
        "status": db_order.status
    }


# ---- Get Order ----
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    db = SessionLocal()

    order = db.query(OrderTable).filter(OrderTable.id == order_id).first()

    db.close()

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "id": order.id,
        "product": order.product,
        "quantity": order.quantity,
        "status": order.status
    }


# ---- Update Order ----
@app.put("/orders/{order_id}")
def update_order(order_id: int, update: OrderStatusUpdate):
    db = SessionLocal()

    order = db.query(OrderTable).filter(OrderTable.id == order_id).first()

    if order is None:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = update.status

    db.commit()
    db.refresh(order)

    db.close()

    return {
        "id": order.id,
        "product": order.product,
        "quantity": order.quantity,
        "status": order.status
    }
