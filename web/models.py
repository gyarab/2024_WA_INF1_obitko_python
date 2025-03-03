from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to="chordpro/", null=True, blank=True)  
    content = models.TextField(blank=True)

    def __str__(self):
        return f"Song: {self.title}"  
