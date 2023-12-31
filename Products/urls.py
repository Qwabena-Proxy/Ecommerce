from django.urls import path
from . import views

urlpatterns= [
    path('', views.indexPage, name='index'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('upload_new_product', views.newProducts, name='upload_new_product'),
    path('product_details/<int:productid>/<str:productname>',views.productDetails, name='details'),
    path('update_product/<int:productid>/<str:productname>',views.updateProduct, name='update'),
    path('delete_product/<int:productid>/<str:productname>',views.deleteProduct, name='delete'),
    path('add_category', views.categoryAdd, name='addcategory'),
    path('add_brand', views.brandAdd, name='addbrand'),
    path('add_brand_image', views.brandimageAdd, name='addbrandimage'),
    path('tails', views.tails, name=''),
    path('products', views.products, name='products'),
    path('reviews', views.reviews, name='reviews'),
]