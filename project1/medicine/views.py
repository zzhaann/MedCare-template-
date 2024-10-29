from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Remedy, Surgeons, Nurses


def home(request):
    posts = Article.objects.all()
    items = Remedy.objects.all()
    return render(request, 'med/index.html', {'title': 'Main page', 'posts': posts, 'items': items})


def contact(request):
    return render(request, 'med/contact.html', )


def about(request):
    return render(request, 'med/about.html', {'title': 'about'})


def service(request):
    return render(request, 'med/service.html')


def remedy(request):
    surgeon = Surgeons.objects.all()
    nurse = Nurses.objects.all()
    return render(request, 'med/remedy.html', {'surgeons': surgeon, 'nurses': nurse})


'''
posts = Article.objects.all()
return render(request, 'med/...', {'posts':posts})
html file-da :
{% for post in posts %}
<div>
<h3>{{ post.title }}</h3>

<div>
<img src="{{ post.photo.url }}" alt="{{ post.title }}">
{{ post.content }}</div>
<p>{{ post.created_at }}</p>

</div>
{% endfor %}
{{posts}}
'''