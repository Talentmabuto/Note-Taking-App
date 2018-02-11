from django.urls import path

from . import views

app_name = 'to'

urlpatterns = [
    path('', views.ListCreateView.as_view(), name='create'),
    path('list/', views.NoteListView.as_view(), name='list'),
    path('delete/<int:pk>/', views.ListDeleteView.as_view(), name='delete'),
]
