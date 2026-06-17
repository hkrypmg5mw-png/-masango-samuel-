import datetime
from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)

class AuditLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user = request.user.email
            role = request.user.role
        else:
            user = "Anonymous"
            role = "None"

        method = request.method
        path = request.path
        timestamp = datetime.datetime.now().isoformat()

        logger.info(f"AUDIT: [{timestamp}] User: {user} ({role}) | Method: {method} | Path: {path}")

    def process_response(self, request, response):
        return response
