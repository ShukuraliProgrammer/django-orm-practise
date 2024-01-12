from django.urls import path
from .views import AuthorListAPIView

urlpatterns = [
    path("authors/", AuthorListAPIView.as_view(), name="author-list"),
]