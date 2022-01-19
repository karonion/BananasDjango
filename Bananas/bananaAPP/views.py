from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import FeedbackForm, Addpost
from .models import Feedback, Articles


def index(request):  # Главная страница
    article_scope = Articles.objects.all().order_by('-created_date')  # Получаем все посты отсортированные по дате
    return render(request, 'index.html', {'article_scope': article_scope})


def about(request):  # О нас
    return HttpResponse('<h2> About site </h2>')


def contact(request):  # Контакты
    return HttpResponse('<h2> Our contacts </h2>')


def index_app(request):  # Приложение
    data = {
        'header': 'Заголовок переданного сообщения',
        'message': 'Сообщение'
    }
    return render(request, 'bananaAPP/index_app.html', context=data)


def feedback(request):  # Обратная связь
    if request.method == 'POST':
        feed = Feedback()
        feed.contact = request.POST.get('contact')
        feed.text = request.POST.get('text')
        feed.save()
        return HttpResponse('Агонь, всё получилось')
    else:
        return render(request, 'feedback.html',
                  {'forms':FeedbackForm})

def get_feedback(request):  # Получение обратной связи
    feed = Feedback.objects.all().order_by('-date')
    return render(request, 'getfeedback.html', {'feed':feed})

def add_post(request):
    if request.method == 'POST':
        created_by = request.POST.get('name')
        preview = request.POST.get('preview')
        text = request.POST.get('text')
        photo = request.POST.get('preview_photo')
        article = Articles(created_by=created_by, preview=preview, text=text)
        article.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'addpost.html', {'form':Addpost})