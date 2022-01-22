from django.urls import path
from .views import ProductsList, ProductDetail, NewssList, NewsDetail

urlpatterns = [
    path('', NewssList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
]

