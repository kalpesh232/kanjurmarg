import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class customTimeMiddelware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, proceed):
        start_time = time.time()
        response = await proceed(request)
        print("*" * 25, response)
        duration = time.time() - start_time
        print(f"Request took {duration} seconds")
        return response