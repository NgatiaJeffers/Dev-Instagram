from django import forms
from cloudinary.models import CloudinaryField

class PostForm(forms.Form):
    image = CloudinaryField('image')
    image_name = forms.CharField(widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Image Name"}))
    image_caption = forms.CharField(widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Image Name"}))

class CommentForm(forms.Form):
    body = forms.CharField(widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Leavea Comment"}))