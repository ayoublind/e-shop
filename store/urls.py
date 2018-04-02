from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # ex: /store/5/
    path('<int:product_id>/', views.detail, name='detail'),
    # ex: /store/5/addToCart/
    path('<int:product_id>/addToCart/', views.addToCart, name='addToCart'),
    # ex: /store/5/addToFavorites/
    path('<int:product_id>/addToFavorites/', views.addToFavorites, name='addToFavorites'),
]
