
from os import link
from fastapi import FastAPI

import api_rest
import api_graphql


app = FastAPI()


app.include_router(api_rest.router)
app.include_router(api_graphql.router,  prefix="/graphql")