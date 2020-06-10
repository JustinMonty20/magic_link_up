from django.urls import path
from .views import AddedView, SearchView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('added/', AddedView.as_view()),
    path('search/', SearchView.as_view()),
    ]


