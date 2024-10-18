from django.urls import path
from shops import views

urlpatterns = [
    path('register', views.ShopRegister.as_view(), name="register"),
    path('search', views.UserSearch.as_view(), name='search'),
]