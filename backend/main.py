import uvicorn
from src.api import get_output
from src.db import save_output

if __name__ == "__main__":
    # get_output()
    # save_output()
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000)
