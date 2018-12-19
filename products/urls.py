from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name = 'add_product'),
    path('<int:product_id>/', views.detail, name = 'product_detail'),
    path('<int:product_id>/upvote', views.upvote, name = 'upvote'),
]
