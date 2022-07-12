from django.urls import path
from .views import (
    register,
    login,
    logout,
    activate,
    my_orders,
    dashboard,
    edit_profile,
    forgot_password,
    reset_password_page,
    reset_password_validate,
)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', dashboard, name='dashboard'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    path('reset_password_page/', reset_password_page, name='reset_password_page'),

    path('my_orders/', my_orders, name='my_orders'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
