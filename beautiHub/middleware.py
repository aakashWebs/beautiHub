from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from django.http import HttpResponse

REQUEST_COUNT = Counter('request_count', 'App Request Count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])

class PrometheusAfterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        REQUEST_COUNT.labels(request.method, request.path).inc()
        return response

class PrometheusBeforeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        with REQUEST_LATENCY.labels(request.path).time():
            response = self.get_response(request)
        return response

def metrics(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)
