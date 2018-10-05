from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.google_test),
    path('member/', views.google_test),
]