from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('done/<str:pk>',views.done,name = 'done'),
    path('update/<str:pk>',views.update,name = 'update'),
    path('delete/<str:pk>',views.delete,name = 'delete')
]