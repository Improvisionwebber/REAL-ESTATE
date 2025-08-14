from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)

from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    search_fields = ('name', 'email', 'phone', 'message')
