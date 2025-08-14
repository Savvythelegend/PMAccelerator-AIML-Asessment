from fastapi import FastAPI, HTTPException, Query, Body # type: ignore
from models import WeatherRequestCreate, WeatherRequestUpdate, WeatherResponse
from repositories import create_request, get_requests, get_request_by_id, update_request, delete_request
from weather_client_async import AsyncWeatherClient
from typing import Optional, List

app = FastAPI(title="Weather App API", description="API for managing weather requests and fetching weather data.")

# CREATE
@app.post("/requests", response_model=WeatherResponse, status_code=201)
async def create_weather_request(request: WeatherRequestCreate):
    client = AsyncWeatherClient()
    weather_data = await client.get_current(
        request.location_input,
        request.start_date,
        request.end_date
    )

    db_record = weather_data.dict()
    db_record["resolved_name"] = weather_data.get("location", {}).get("name")
    db_record["latitude"] = weather_data.get("location", {}).get("lat")
    db_record["longitude"] = weather_data.get("location", {}).get("lon")
    db_record["result_json"] = weather_data

    created = create_request(db_record)
    if "error" in created:
        raise HTTPException(status_code=500, detail=created["error"])
    return created

# READ ALL
@app.get("/requests", response_model=List[WeatherResponse])
def get_all_requests(filters: Optional[str] = Query(None, description="Filters as JSON string")):
    # You may want to parse filters from JSON string if needed
    requests = get_requests(filters)
    if not requests:
        raise HTTPException(status_code=404, detail="No requests found")
    return requests

# READ ONE
@app.get("/requests/{request_id}", response_model=WeatherResponse)
def get_one_request(request_id: int):
    request = get_request_by_id(request_id)
    if "error" in request:
        raise HTTPException(status_code=404, detail=request["error"])
    return request

# UPDATE
@app.patch("/requests/{request_id}", response_model=WeatherResponse)
async def update_weather_request(request_id: int, request: WeatherRequestUpdate):
    updated_data = {}
    if request.location_input is not None:
        updated_data["location_input"] = request.location_input
    if request.start_date is not None:
        updated_data["start_date"] = request.start_date
    if request.end_date is not None:
        updated_data["end_date"] = request.end_date
    if not updated_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    updated = update_request(request_id, updated_data)
    if "error" in updated:
        raise HTTPException(status_code=500, detail=updated["error"])
    return updated

# DELETE
@app.delete("/requests/{request_id}", status_code=204)
def delete_weather_request(request_id: int):
    deleted = delete_request(request_id)
    if "error" in deleted:
        raise HTTPException(status_code=500, detail=deleted["error"])
    return {"message": "Request deleted successfully"}
