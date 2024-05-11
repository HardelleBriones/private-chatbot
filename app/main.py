from fastapi import FastAPI
import uvicorn
#from . import models
# from .database import engine
from routers import query, knowledge_base, user, evaluation, ingest_data
#models.Base.metadata.create_all(bind=engine)

from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

app.include_router(query.router)
app.include_router(ingest_data.router)
app.include_router(knowledge_base.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


