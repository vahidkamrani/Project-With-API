from django.urls import path
from complaint import views


urlpatterns = [
    path('post-complaint/', views.post_complaint),
    path('get-complaints/', views.get_complaints),
]
