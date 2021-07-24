from django.shortcuts import render, redirect

from petstagram_demo_project.common.forms import CommentForm
from petstagram_demo_project.common.models import Comment
from petstagram_demo_project.pets.forms import PetForm, EditPetForm
from petstagram_demo_project.pets.models import Pet, Like


def get_all_pets(req):
    all_pets = Pet.objects.all()
    context = {"pets": all_pets}
    return render(req, 'pets/pet_list.html', context)


def get_pet_details(req, pk):
    current_pet = Pet.objects.get(pk=pk)
    current_pet.likes = current_pet.like_set.count

    context = {
        "pet": current_pet,
        "comment_form": CommentForm(
            initial={
                "pet_pk": pk
            }
        ),
        "comments": current_pet.comment_set.all(),
    }
    return render(req, 'pets/pet_detail.html', context)


# def comment_pet(req, pk):
#     pet = Pet.objects.get(pk=pk)
#     comment_form = CommentForm(req.POST)
#     if comment_form.is_valid():
#         comment = Comment(
#             comment=comment_form.cleaned_data["comment"],
#             pet=pet
#         )
#         comment.save()
#
#     return redirect("pet_details", pet.id)

# 2nd Way:
def comment_pet(req, pk):
    # pet = Pet.objects.get(pk=pk)
    comment_form = CommentForm(req.POST)
    if comment_form.is_valid():
        # comment = Comment(
        #     comment=comment_form.cleaned_data["comment"],
        #     pet=pet
        # )
        # comment.save()
        comment_form.save()

    # return redirect("pet_details", pet.id)
    return redirect("pet_details", pk)


def like_a_pet(req, pk):
    current_pet = Pet.objects.get(pk=pk)
    print(current_pet.__dict__)
    like = Like(pet=current_pet)
    like.save()
    return redirect("pet_details", current_pet.id)  # redirect to the url with name="pet_details"


def create_pet(req):
    if req.method == "POST":
        form = PetForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_all_pets")
    else:
        form = PetForm()

    context = {"form": form}
    return render(req, "pets/pet_create.html", context)


def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == "POST":
        form = EditPetForm(req.POST, req.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("list_all_pets")
    else:
        form = EditPetForm(instance=pet)

    context = {
        "form": form,
        "pet": pet
    }
    return render(req, "pets/pet_edit.html", context)


def delete_pet(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == "POST":
        pet.delete()
        return redirect("list_all_pets")
    else:
        return render(req, "pets/pet_delete.html", context={"pet": pet})
