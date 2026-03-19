from django.db import models

# Create your models here.
class Translation(models.Model):
    original_text = models.TextField()
    translated_text = models.TextField()
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_text[:50]}... -> {self.translated_text[:50]}..."