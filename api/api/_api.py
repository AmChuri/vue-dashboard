"""Module to setup fastapi API to expose API to the outside world."""
import logging
import random
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


import uvicorn

ERROR_CODES = [c for c in range(10)]
LOGGER = logging.getLogger("API")
app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    uname: str
userName = ''

userNameList = []
# count the number of times request was made
RequestCount = 0

@app.get("/get_lists")
def generate_lists() -> Dict[str, Any]:
    """Endpoint that generates resolved, unresolved and backlog lists."""
    LOGGER.info('Generating resolved, unresolved and backlog lists.')
    global RequestCount, userName
    RequestCount+=1
    print(userName)
    return {
        'resolved': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error ABC occured, that is `resolved`'
        } for error_idx in range(50)],
        'unresolved': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error DEF occured, that is `unresolved`'
        } for error_idx in range(50, 100)],
        'backlog': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error XYZ occured, that is in the `backlog`'
        } for error_idx in range(100, 150)]
    }

@app.get("/get_log_count")
def log_count():
    global RequestCount
    return{RequestCount}

@app.post("/setname")
def set_name(data: Data):
    global userName
    userName = data.uname
    return True


def run(host: str, port: int) -> None:
    """Run the code challenge API."""
    uvicorn.run(app, host=host, port=port)
