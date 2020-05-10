from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    )

urlpatterns = [
    # home
    path("", BlogListView.as_view(), name="home"),
    # detail
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    # post new
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    # post edit
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    # post delete
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
]
