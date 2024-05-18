from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework.views import APIView


class PredictView(APIView):
    def post(self, request):
        url = request.data.get("url")
        if not url:
            return HttpResponseBadRequest("URL is required")
        return JsonResponse({"url": url, "is_phising": True, "probability": 99})

    def get(self, request):
        return HttpResponse("Using a very cool model!", 200)
