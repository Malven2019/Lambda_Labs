"""Database functions"""

import os  #Built-in library/ Auto PEP Compliance

from dotenv import load_dotenv # Importing from third parties, SQLAlchemy, Fast API etc
from fastapi import APIRouter # Dotenv for loading environment variables
from sqlalchemy import create_engine

load_dotenv()
database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
engine = create_engine(database_url)
router = APIRouter()


@router.get('/info') # Router/Endpoint name
async def get_url():
    """Verify we can connect to the database,
    and return the database URL, in this format:

    dialect://user:password@host/dbname
    """
    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()
        return {'url': url_without_password}


@router.get('/hello')
async def hello_world():
    return {'Hello': 'World'}
