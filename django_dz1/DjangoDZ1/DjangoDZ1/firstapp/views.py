from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    index1 = ('<!DOCTYPE html><html lang="ru"><head>'
            '<meta charset="UTF-8">'
            '<title>Главная страница</title>'
            '</head><body>Главная страница</body></html>')
    return HttpResponse(index1)


def about(request):
    about1 = ('<!DOCTYPE html> <html lang="ru" > '
              '<head> <meta charset="UTF-8"> <title>Сведения обо мне</title> '
              '</head>'
              ' <body> <header> <h1>Обо мне </h1> </header>'
              ' <main><p>Многострочный текст</p>'
              ' <ul> таки да</ul>'
              ' <ul> таки нет</ul>'
              ' </main> </body> </html>')
    return HttpResponse(about1)

