import fastapi
import uvicorn


api = fastapi.FastAPI()


@api.get("/api/calc")
def calculate():
    value = 2 + 2
    return {
        "value": value
    }


uvicorn.run(api, host="127.0.0.1", port=8000)
