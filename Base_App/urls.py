from django.urls import path
from Base_App import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_view, name='menu'),
    path('book/', views.book_table_view, name='book_table'),
    path('feedback/', views.feedback_view, name='feedback_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('sign-up/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
]
