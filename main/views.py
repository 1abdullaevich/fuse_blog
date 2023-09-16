from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'apps/index.html'


class AboutView(TemplateView):
    template_name = 'apps/about.html'


class AddPostView(TemplateView):
    template_name = 'apps/add_post.html'


class BlogView(TemplateView):
    template_name = 'apps/blog.html'


class ContactView(TemplateView):
    template_name = 'apps/contact.html'


class PostView(TemplateView):
    template_name = 'apps/post.html'


class ProfileView(TemplateView):
    template_name = 'apps/profile.html'


class ProfileDetailView(TemplateView):
    template_name = 'apps/profile_detail.html'

