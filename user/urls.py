
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterUserApiView.as_view(), name='register'),
    path('admin/register/',views.RegisterAdminApiView.as_view(), name='adminregister'),
    path('login/',views.LoginApiView.as_view(),name='login'),
    path('logout/',views.LogOutApiview.as_view(),name='logout'),
    path('refreshtoken/',views.TokenRefreshApiView.as_view(),name='refreshtoken'),
    
]



