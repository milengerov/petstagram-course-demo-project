from django.urls import path

from petstagram_demo_project.pets.views import get_all_pets, get_pet_details, like_a_pet, create_pet, edit_pet, \
    delete_pet, comment_pet

urlpatterns = [
    path("", get_all_pets, name="list_all_pets"),
    path("details/<int:pk>/", get_pet_details, name="pet_details"),
    path("like/<int:pk>/", like_a_pet, name="like_a_pet"),

    path("create/", create_pet, name="create_pet"),
    path("edit/<int:pk>/", edit_pet, name="edit_pet"),
    path("delete/<int:pk>/", delete_pet, name="delete_pet"),

    path("comment/<int:pk>", comment_pet, name="comment_pet"),
]
