from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import random

class createTask(BaseModel):
    id : int 
    name : str
    assignee : str
    project : str
    start_time : datetime
    ChethanLReddyProperty : Optional[str] = ' '

class updateTask(BaseModel):
    name: str
    id : int
    assignee : str
    project : str
    start_time : datetime


