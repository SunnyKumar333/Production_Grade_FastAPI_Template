from starlette.middleware.base import BaseHTTPMiddleware
from utils.generate_corelation_id import generateCorrelationID
from utils.context import corelationIDContextVar


class CorelationIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Generate or extract correlation ID here
        correlation_id = generateCorrelationID()
        corelationIDContextVar.set(correlation_id)
        # request.state.correlation_id = correlation_id
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = correlation_id
        return response