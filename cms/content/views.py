from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

def articles(request):
    with open('articles.json', encoding="utf-8") as f:
        data = json.load(f)
    
    html = '<ul>'
    for article in data:
        title = article['title']
        content = article['content']
        html += f'<li><a href="/article/{title}">{title}</a></li>'
    html += '</ul>'
    
    return HttpResponse(html)