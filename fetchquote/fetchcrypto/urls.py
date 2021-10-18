from django.conf.urls import url
from django.urls import path, include
from .views import FetchQuoteApiView

urlpatterns = [
    path('v1/quotes', FetchQuoteApiView.as_view()),
]