from django.shortcuts import render, redirect

from petstagram_demo_project.pets.models import Pet, Like


def get_all_pets(req):
    all_pets = Pet.objects.all()
    context = {"pets": all_pets}
    return render(req, 'pets/pet_list.html', context)


def get_pet_details(req, pk):
    current_pet = Pet.objects.get(pk=pk)
    current_pet.likes = current_pet.like_set.count
    context = {"pet": current_pet}
    return render(req, 'pets/pet_detail.html', context)


def like_a_pet(req, pk):
    current_pet = Pet.objects.get(pk=pk)
    print(current_pet.__dict__)
    like = Like(pet=current_pet)
    like.save()
    return redirect("pet_details", current_pet.id)      # redirect to the url with name="pet_details"

