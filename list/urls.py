from django.urls import path
from list import views

urlpatterns = [
    path('',views.home),
    path('delete/<int:id>/',views.delete_entry),


]