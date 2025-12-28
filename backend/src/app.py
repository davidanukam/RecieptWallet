from fastapi import FastAPI, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
import shutil
import os

from src.db import get_db, create_receipt

app = FastAPI(title="Receipt Upload API", description="An API to handle uploaded receipts")

@app.post("/upload-receipt")
async def upload_receipt(file: UploadFile, db: Session = Depends(get_db)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        new_entry = create_receipt(temp_path, db)
        db.commit()
        db.refresh(new_entry)
        return {"status": "success", "id": str(new_entry.id)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
