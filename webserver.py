from fastapi import FastAPI
from yggamonitors.lib.web.compile_data import check_all_sites


app = FastAPI()


@app.get("/")
async def root():
    statuses: dict = check_all_sites()
    return statuses


@app.get("/graph/{site}")
def graph():
    pass