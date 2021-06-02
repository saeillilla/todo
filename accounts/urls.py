from django.urls import path
from accounts import views
urlpatterns = [
    path('login/',views.sign_in),
    path('signup/',views.sign_up),
    path('logout/',views.user_logout),


]