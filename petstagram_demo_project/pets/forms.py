from django import forms

from petstagram_demo_project.core.forms import BootstrapFormMixin
from petstagram_demo_project.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"


class EditPetForm(PetForm):
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
