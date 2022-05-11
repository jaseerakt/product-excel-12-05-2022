from django.urls import path
from . import views

urlpatterns=[

    path('home/', views.home),
    path('upload_file/', views.upload_file),
    path('select/', views.select),
    path('product/', views.product),
    path('upload_product/', views.upload_product),
]