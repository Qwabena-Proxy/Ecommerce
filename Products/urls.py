from django.urls import path
from . import views

urlpatterns= [
    path('', views.indexPage, name='index'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('upload_new_product', views.newProducts, name='upload_new_product'),
    # path('logout', views.logout, name='logout'),
    # path('signup', views.signupPage, name='signup'),
    # path('task', views.userPage, name='userPage'),
    # path('addtask', views.addTask, name='addtask'),

]