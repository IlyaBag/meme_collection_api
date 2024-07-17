from fastapi import FastAPI

from api_v1.views import router


app = FastAPI()

app.include_router(router)
