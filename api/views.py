from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseServerError,
    JsonResponse,
)
from requests import HTTPError, RequestException
from rest_framework.views import APIView

from api.services.web_scrape import get_website_features
from api.services.ml_model import predict_with_model


class PredictView(APIView):
    def post(self, request):
        url = request.data.get("url")
        if not url:
            return HttpResponseBadRequest("URL is required")
        try:
            features = get_website_features(url)
            is_phishing, probability = predict_with_model(features=features)
            return JsonResponse(
                {"url": url, "is_phising": is_phishing, "probability": probability}
            )
        except HTTPError as e:
            return HttpResponse(
                f"{e.response.reason} for url {e.response.url}",
                status=e.response.status_code,
            )
        except RequestException as e:
            return HttpResponseBadRequest(e)
        except Exception as e:
            print(e)
            return HttpResponseServerError("Internal server error")

    def get(self, _):
        return HttpResponse(
            "V1: Using tuned pre trained Random Forest Classifier. Refer to the docs for more info",
            200,
        )
