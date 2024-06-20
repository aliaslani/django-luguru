from loguru import logger
from django.http import HttpResponse

def my_view(request):
    logger.debug("This is a debug message")
    logger.error("This is an error message")
    return HttpResponse("Hello, Loguru!")