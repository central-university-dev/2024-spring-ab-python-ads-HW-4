import datetime
import os

import requests
import sql_models
from database import SessionLocal, engine
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from schemas import TreesRequestBody
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

load_dotenv()
sql_models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/count_trees")
def get_count_trees(body: TreesRequestBody, db: Session = Depends(get_db)) -> int:
    max_size = os.getenv("OVERPASS_QUERY_RAM_MAXSIZE", 2000000000)
    timeout = os.getenv("OVERPASS_TIMEOUT", 15)
    base_url = os.getenv("OVERPASS_API_URL")

    if not base_url:
        raise HTTPException(
            status_code=500,
            detail="OVERPASS_API_URL is not set in the environment variables",
        )

    query = f"""
    [out:json][date:"{body.year}-01-01T11:00:00Z"][maxsize:{max_size}][timeout:{timeout}];
    area["name:en"={body.country}]['admin_level'='2']->.country;
    area["name:en"={body.city}](area.country)->.city;
    node["natural"="tree"](area.city);
    out count;
    """
    db.add(
        sql_models.Requests(
            req_time=datetime.datetime.now(),
            city=body.city,
            country=body.country,
            year=body.year,
        )
    )
    db.commit()

    try:
        response = requests.get(base_url, params={"data": query})
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail=str(e))

    if response.status_code == 200:
        try:
            data = response.json()
            for elem in data.get("elements", []):
                if elem["type"] == "count":
                    return int(elem["tags"]["total"])
        except (ValueError, KeyError):
            raise HTTPException(
                status_code=500,
                detail="Error parsing the response from the Overpass API.",
            )
    else:
        raise HTTPException(
            status_code=response.status_code, detail="Overpass API returned an error."
        )

    raise HTTPException(
        status_code=500, detail="Unable to retrieve tree count from the Overpass API."
    )


@app.get("/most_frequent_city")
def get_most_pop_city(db: Session = Depends(get_db)) -> str | None:
    result = db.execute(text("SELECT most_frequent_city()")).fetchall()
    if result:
        return result[0][0]
