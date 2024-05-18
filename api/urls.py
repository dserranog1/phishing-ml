from django.urls import path

from api import views

urlpatterns = [
    path("predict/", views.PredictView.as_view(), name="model_prediction"),
]