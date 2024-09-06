from django import forms
from .models import Description


class Descriptionform(forms.ModelForm):
    class Meta:
        model= Description
        fields= ["subject", "description"]