from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count_likes = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title