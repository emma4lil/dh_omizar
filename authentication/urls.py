from django.conf.urls import url

from .views import UserViewSet, RegistrationAPIView

urlpatterns = [
    # url(r'^users/', UserViewSet.as_view({'get':'list'})),
    url(r'^users/', RegistrationAPIView.as_view()),
]
