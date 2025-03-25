from django import forms
from .models import Song, Author

class SongUploadForm(forms.ModelForm):
	class Meta:
		model = Song 
		fields =  ["title", "file", "author"]
		labels = {
			"title": "Title",
			"file": "File",
			"author": "Author"
		}
		help_texts = {
			"author": "No author? <a href='/create_author/'>Create one</a>"
		}

class CreateAuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ["name"]
		labels = {
			"name": "Name"
		}