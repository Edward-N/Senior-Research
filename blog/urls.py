from django.urls import path
from . import views

urlpatterns = [
  path("blogs/", views.index, name="blog"),
  path("new/", views.new, name="new"),
  path("<int:id>",views.post_detail,name='post-detail'),
  path("<int:id>/delete/", views.delete,name="delete"),
  path("<int:id>/edit", views.edit, name="edit"),
  path("<int:id>/update/", views.update,name="update")
]
