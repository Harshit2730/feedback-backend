from pydantic import BaseModel

class FeedbackBase(BaseModel):
    feedback:str
    rating:int

class CreateFeedback(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id:int
    polarity:int
    subjectivity:int
    rating:int
    
    class config:
        orm_mode=True

class Analysis(BaseModel):
    stats:dict
    words:list
    trend:list

