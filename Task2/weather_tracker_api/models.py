# models: checks for validates the user input and the upate (since they are only needed body parameters)

from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class WeatherRequestCreate(BaseModel):
    user_name: str
    location_input: str
    start_date: date
    end_date: date

class WeatherRequestUpdate(BaseModel):
    location_input: Optional[str] 
    start_date: Optional[date]
    
    end_date: Optional[date]

class WeatherResponse(BaseModel):
    id: int
    city: str
    date_: date
    type: str
    data: dict