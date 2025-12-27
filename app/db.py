import uuid
import sys

from sqlalchemy import create_engine, delete, String, DECIMAL
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, Mapped, mapped_column

DATABASE_URL = "sqlite:///./wallet.db"

class Base(DeclarativeBase):
    pass

class Reciept(Base):
    __tablename__ = "reciepts"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    store: Mapped[str] = mapped_column(String(100))
    subtotal: Mapped[float] = mapped_column(DECIMAL(precision=10, scale=2))
    total: Mapped[float] = mapped_column(DECIMAL(precision=10, scale=2))
    date: Mapped[str] = mapped_column(String(8))

engine = create_engine(DATABASE_URL, echo=True)
sessionLocal = sessionmaker(engine, autoflush=True, expire_on_commit=False)

Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

with sessionLocal() as db:
    with db.begin():
        new_reciept = Reciept(store="WALMART", subtotal="11.99", total="67.00", date="08/20/10")
        db.add(new_reciept)
    db.refresh(new_reciept)

def clear_db():
    with sessionLocal() as db:
        with db.begin():
            db.execute(delete(Reciept))

if sys.argv[1] == "-c":
    clear_db()
