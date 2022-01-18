from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import FeedbackForm
from .models import Feedback


def index(request):  # Главная страница
    return render(request, 'index.html')


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
    feed = Feedback.objects.all()
    return render(request, 'getfeedback.html', {'feed':feed})