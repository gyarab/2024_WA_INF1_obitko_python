from django.db import models
from django.utils.text import slugify 

class Song(models.Model):
    title = models.CharField(max_length=255, default="")
    file = models.FileField(upload_to="chordpro/", null=True)  
    author = models.ForeignKey("Author", on_delete=models.CASCADE, default=1)  
    slug = models.SlugField(unique=True, blank=True)
    html_content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
    
        super().save(*args, **kwargs)  

        if self.file and not self.html_content:
            try:
                with open(self.file.path, "r", encoding="utf-8") as f:
                    file_content = f.read()
                    self.render_html(file_content)
                super().save(update_fields=["html_content"])  
            except Exception as e:
                print(f"Error reading file: {e}")

    def render_html(self, file_content):
        self.html_content = file_content

    def __str__(self): 
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
