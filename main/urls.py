from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', AboutView.as_view(), name='about'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('post/', PostView.as_view(), name='post'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-detail/', ProfileDetailView.as_view(), name='profile_detail'),
]
