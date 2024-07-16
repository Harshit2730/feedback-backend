from sqlalchemy.orm import Session
from textblob import TextBlob
from . import models, schemas, utils


def get_feedbacks(db:Session):
    return db.query(models.Feedback).all()

def create_feedback(db:Session, data: schemas.CreateFeedback):
    value = TextBlob(data.feedback)
    feedback = models.Feedback(feedback=data.feedback, polarity=round(value.sentiment.polarity,2), subjectivity=round(value.sentiment.subjectivity,2), rating=data.rating)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

def get_analysis(db:Session):
    data = db.query(models.Feedback).all()
    utils.init(data)
    result = schemas.Analysis
    result.stats = utils.get_stats()
    result.words = utils.get_word_count()
    result.trend = utils.get_trend()
    return result
