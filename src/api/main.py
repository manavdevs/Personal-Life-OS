from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def test():
    try:
        return {"Health Status": "👍"}
    except:
        return {"Health Status": "👎"}
        
        

