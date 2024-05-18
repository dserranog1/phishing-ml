from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseServerError,
    JsonResponse,
)
from requests import HTTPError, RequestException
from rest_framework.views import APIView

from api.services.web_scrape import get_website_features


class PredictView(APIView):
    def post(self, request):
        url = request.data.get("url")
        if not url:
            return HttpResponseBadRequest("URL is required")
        try:
            features = get_website_features(url)
            return JsonResponse({"url": url, "is_phising": True, "probability": 99})
        except HTTPError as e:
            return HttpResponse(
                f"{e.response.reason} for url {e.response.url}",
                status=e.response.status_code,
            )
        except RequestException as e:
            return HttpResponseBadRequest(e)
        except Exception as _:
            return HttpResponseServerError()

    def get(self, request):
        return HttpResponse("Using a very cool model!", 200)
