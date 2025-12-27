import uuid
import sys
import re
from decimal import Decimal

from sqlalchemy import create_engine, delete, String, DECIMAL
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, Mapped, mapped_column

DATABASE_URL = "sqlite:///./wallet.db"

class Base(DeclarativeBase):
    pass

class Reciept(Base):
    __tablename__ = "reciepts"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    store: Mapped[str] = mapped_column(String(100))
    subtotal: Mapped[Decimal] = mapped_column(DECIMAL(precision=10, scale=2))
    total: Mapped[Decimal] = mapped_column(DECIMAL(precision=10, scale=2))
    date: Mapped[str] = mapped_column(String(8))

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(engine, autoflush=True, expire_on_commit=False)

Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

def clear_db():
    with sessionLocal() as db:
        with db.begin():
            db.execute(delete(Reciept))

if len(sys.argv) > 1:
    if sys.argv[1] == "-c":
        clear_db()
        sys.exit()

letters = [chr(i) for i in range(97, 97 + 26)]
numbers = [i for i in range(10)]
punc = [chr(i) for i in range(32, 48)]
punc.extend([chr(i) for i in range(58, 65)])
punc.extend([chr(i) for i in range(91, 97)])
punc.extend([chr(i) for i in range(123, 127)])
punc.pop(punc.index("-"))

stores = {
    "walmart" : "Walmart",
    "nofrills" : "No Frills",
    "costco" : "Costco",
    "food" : "Food Basics",
    "shoppers" : "Shoppers Drug Mart"
}

# Regex Patterns
# Matches: 12.34 or 1,200.50
PRICE_PATTERN = r"(\d{1,3}(?:,\d{3})*\.\d{2})"
# Matches: MM/DD/YY, MM/DD/YYYY, or DD-MM-YYYY
DATE_PATTERN = r"(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})"

def create_reciept(file_path, db):
    # Clean output
    lines = []
    with open(file_path, "r") as f:
        for line in f:
            clean_line = "".join(c for c in line if c.isprintable()).strip()
            if len(clean_line) > 2:
                lines.append(clean_line)

    store = "Unknown Store"
    subtotal = 0.0
    total = 0.0
    date = "00/00/00"

    # Parse the lines
    for i, line in enumerate(lines):
        line_lower = line.lower()

        # Find Store
        for key, full_name in stores.items():
            if key in line_lower:
                store = full_name
                break

        # Find Date
        date_match = re.search(DATE_PATTERN, line)
        if date_match:
            date = date_match.group(1)

        # Find Subtotal
        if "sub" in line_lower and "total" in line_lower:
            price_match = re.search(PRICE_PATTERN, line)
            if price_match:
                subtotal = float(price_match.group(1))
            elif i + 1 < len(lines):
                next_line_price = re.search(PRICE_PATTERN, lines[i+1])
                if next_line_price:
                    subtotal = float(next_line_price.group(1))

        # Find Total
        if "total" in line_lower and "sub" not in line_lower:
            price_match = re.search(PRICE_PATTERN, line)
            if price_match:
                total = float(price_match.group(1))
            elif i + 1 < len(lines):
                next_line_price = re.search(PRICE_PATTERN, lines[i+1])
                if next_line_price:
                    total = float(next_line_price.group(1))

    # 3. Save to Database
    new_reciept = Reciept(
        store=store,
        subtotal=subtotal,
        total=total,
        date=date[:8]
    )
    db.add(new_reciept)
    return new_reciept

def save_output():
    with sessionLocal() as db:
        with db.begin():
            new_reciept = create_reciept("output.txt", db)
        db.refresh(new_reciept)

if __name__ == "__main__":
    save_output()
