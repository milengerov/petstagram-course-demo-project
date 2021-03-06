import os
from os.path import join

from django import forms
from django.conf import settings

from petstagram_demo_project.core.forms import BootstrapFormMixin
from petstagram_demo_project.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"


class EditPetForm(PetForm):

    # delete old image - doesn't work through administration. If we want to - make it in the models
    def save(self, commit=True):
        db_pet = Pet.objects.get(pk=self.instance.id)

        if commit:
            # path = join(settings.MEDIA_ROOT, db_pet.image.url[len("/media/"):])
            path = join(settings.MEDIA_ROOT, str(db_pet.image))
            os.remove(path)
        return super().save(commit)



    class Meta:
        model = Pet
        fields = "__all__"
        widgets = {
            "type": forms.TextInput(
                attrs={
                    "readonly": "readonly"
                }
            )
        }
