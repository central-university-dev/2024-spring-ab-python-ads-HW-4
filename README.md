# OSM Tree Counter API

A FastAPI service that queries the OpenStreetMap Overpass API to return the number of trees in a given city for a given year. Every successful request is logged to PostgreSQL, and a stored procedure identifies the most frequently queried city.

## Project Structure

```
Counting-trees-Open-Street-Map/
├── app/
│   ├── main.py            # FastAPI endpoints
│   ├── models.py          # SQLAlchemy ORM model (Trees table)
│   ├── schemas.py         # Pydantic input schema
│   ├── database.py        # PostgreSQL engine and session setup
│   └── model_predict.py   # Overpass API query and response parsing
├── tests/
│   └── __init__.py
├── database.sql           # PostgreSQL init: Trees table + most_frequent_city() procedure
├── app.Dockerfile
├── pg.Dockerfile
├── docker-compose.yaml    # FastAPI app + PostgreSQL 13.3
├── Makefile               # lint, format, check targets
└── pyproject.toml
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| POST | `/information` | Returns tree count for a city/country/year |

**Request body for `/information`:**

```json
{
  "city": "Berlin",
  "country": "Germany",
  "year": "2022"
}
```

The endpoint queries Overpass API for OSM nodes tagged `natural=tree` within the specified area, filtered by date. The result and request timestamp are saved to the database.

## Database

The `Trees` table logs all requests:

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key |
| `city` | String | Queried city |
| `country` | String | Queried country |
| `year` | Integer | Queried year |
| `trees_count` | Integer | Tree count returned |
| `request_time` | DateTime | Timestamp of request |

`most_frequent_city()` - stored procedure that returns the city with the highest number of logged queries.

## Configuration

Set in `.env`:

| Variable | Description |
|----------|-------------|
| `DB_URL` | PostgreSQL connection string |

Default for docker-compose: `postgresql+psycopg2://postgres:postgres@postgres:5432/postgres`

## Running with Docker

```bash
docker-compose up --build
```

API available at `http://localhost:8000`. PostgreSQL at port 5432.

## Requirements

```
fastapi
uvicorn
sqlalchemy
psycopg2
requests
osmpythontools
pandas
numpy
httpx
python-dotenv
pytest
black
flake8
pylint
mypy
```
