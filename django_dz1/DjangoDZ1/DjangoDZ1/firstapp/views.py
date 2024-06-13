from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    index1 = ('<!DOCTYPE html><html lang="ru"><head>'
            '<meta charset="UTF-8">'
            '<title>Главная страница</title>'
            '</head>'
            '<body>'
            'Главная страница'
            '<p> <a href="http://127.0.0.1:8000/about"> Обо мне</a> </p>'
            '</body>'
            '</html>')
    return HttpResponse(index1)


def about(request):
    about1 = ('<!DOCTYPE html> <html lang="ru" > '
              '<head> <meta charset="UTF-8"> <title>Сведения обо мне</title> '
              '</head>'
              ' <body> <header> <h1>Немного обо мне </h1> </header>'
              ' <main><p>Многострочный текст</p>'
              ' <ul> имя - Алексей</ul>'
              ' <ul> студент Гикбрейнс</ul>'
              ' <p><a href="http://127.0.0.1:8000/"> Главная страница</a></p>'
              ' </main> </body> </html>')
    return HttpResponse(about1)

