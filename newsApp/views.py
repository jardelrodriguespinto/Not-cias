from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=b465a2f3a6e3d98617bfffb93fe9f22c&countries=pt')
    res = r.json()
    data = res['data']
    title = []
    author = []
    description = []
    url = []
    image = []
    
    for i in data:
        title.append(i['title'])
        author.append(i['author'])
        description.append(i['description'])
        url.append(i['url'])
        image.append(i['image'])
    news = zip(title, author, description, url, image)
    
    return render(request , 'index.html', {'news': news})
    