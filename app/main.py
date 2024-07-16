from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, cruds
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins=[
    "http://localhost:4200"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/feedback')
async def post_feedback(feedback: schemas.CreateFeedback, db: Session = Depends(get_db)):
    feedback = cruds.create_feedback(db, data=feedback)
    return {"message":"Feedback shared"}

@app.get('/feedback')
def get_feedbacks(db: Session = Depends(get_db)):
    feedbacks = cruds.get_feedbacks(db)
    if feedbacks is None:
        return {"data":list()}
    return {"data": feedbacks}

@app.get('/feedback/stats', response_model=schemas.Analysis)
def get_feedback_stats(db: Session = Depends(get_db)):
    return cruds.get_analysis(db)

