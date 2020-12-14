from .views import JobOfferListAPIView,JobOfferDetailAPIView
from django.urls import path

urlpatterns = [
		path('jobs/',JobOfferListAPIView.as_view(),name='job-list'),
		path('jobs/<int:pk>/',JobOfferDetailAPIView.as_view(),name='job-detail'),
]