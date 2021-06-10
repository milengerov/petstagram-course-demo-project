from django.urls import path

from petstagram_demo_project.pets.views import get_all_pets, get_pet_details, like_a_pet

urlpatterns = [
    path("", get_all_pets, name="list_all_pets"),
    path("details/<int:pk>/", get_pet_details, name="pet_details"),
    path("like/<int:pk>/", like_a_pet, name="like_a_pet"),
]
