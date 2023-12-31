from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    body = "<html>" \
           "<body>" \
           "<h1>Welcome to fast api</h1>" \
           "<div>" \
           "try it: <a href='/api/calc?x=2&y=3&z=10'>calculator</a>" \
           "</div>" \
           "</body" \
           "</html>"
    return fastapi.responses.HTMLResponse(content=body)


@api.get("/api/calc")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(content={"error": "Error: z cannot be zero."},
                                              status_code=400)
        # return fastapi.Response(content='{"error": "Error: z cannot be zero."}',
        #                         media_type="application/json",
        #                         status_code=400)

    value = (x + y)
    if z is not None:
        value /= z
    return {
        "x": x,
        "y": y,
        "z": z,
        "value": value
    }


uvicorn.run(api, host="127.0.0.1", port=8000)
