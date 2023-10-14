from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('done/', views.done, name='done'),
    path('pending/', views.pending, name='pending'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('create/', views.create, name='create'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]
