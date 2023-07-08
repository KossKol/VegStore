from django.urls import path
from .views import CartView, ProductView, ShopView, CartViewSet, WishlistView, DelWishlist, AddWishlist, WishlistViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

router_2 = routers.DefaultRouter()
router_2.register(r'wishlist', WishlistViewSet)

app_name = 'store'
urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('', ShopView.as_view(), name='shop'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/del/<int:id>/', DelWishlist.as_view(), name='del'),
    path('wishlist/add/<int:id>/', AddWishlist.as_view(), name='add')
]
