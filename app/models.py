from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.title
class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # automatically saves submission time

    def __str__(self):
        return f"{self.name} - {self.email}"