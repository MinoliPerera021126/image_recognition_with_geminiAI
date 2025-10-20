from django import forms
from .models import ImageUpload

class ImageUploadForm(forms.ModelForm): # This form is for uploading images
    class Meta: # Meta class to specify model and fields
        model = ImageUpload 
        fields = ['image']

