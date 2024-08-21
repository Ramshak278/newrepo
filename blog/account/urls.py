from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='render_signup'),
    # Other URL patterns for the app...
]
