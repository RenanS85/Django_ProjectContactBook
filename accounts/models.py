from django.db import models
from book.models import Contact
from django import forms

class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('show',)