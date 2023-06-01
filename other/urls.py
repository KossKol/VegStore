from django.urls import path

from .views import CurrentDateView, RandomData, HelloWorld, IndexView

urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('random/', RandomData.as_view()),
    path('hello/', HelloWorld.as_view()),
    path('index/', IndexView.as_view())
]
