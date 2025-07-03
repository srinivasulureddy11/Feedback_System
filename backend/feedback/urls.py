from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feedback.views import FeedbackViewSet

router = DefaultRouter()
router.register('', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]