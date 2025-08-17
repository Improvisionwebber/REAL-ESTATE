from django import forms
from .models import Post
from .models import ContactSubmission
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image_url']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'message']