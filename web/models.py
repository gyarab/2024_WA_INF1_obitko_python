from django.db import models
from django.utils.text import slugify 

class Song(models.Model):
    title = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to="chordpro/", null=True)  
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
    
        super().save(*args, **kwargs)  

        if self.file and not self.content:
            try:
                with open(self.file.path, "r", encoding="utf-8") as f:
                    self.content = f.read()
                super().save(update_fields=["content"])  
            except Exception as e:
                print(f"Error reading file: {e}")
