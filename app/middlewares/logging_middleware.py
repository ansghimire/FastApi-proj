import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Log request details
        logger.info(f"🚀 Incoming request: {request.method} {request.url}")
        
        response = await call_next(request)
        
        # Log response details
        process_time = time.time() - start_time
        logger.info(f"✅ Response: {response.status_code} | Process time: {process_time:.2f}s")

        return response
