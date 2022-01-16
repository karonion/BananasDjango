from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import FeedbackForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('<h2> About site </h2>')


def contact(request):
    return HttpResponse('<h2> Our contacts </h2>')


def index_app(request):
    data = {
        'header': 'Заголовок переданного сообщения',
        'message': 'Сообщение'
    }
    return render(request, 'bananaAPP/index_app.html', context=data)


def feedback(request):
    if request.method == 'POST':
        contact = request.POST.get('contact')
        text = request.POST.get('text')
        pass  # Добавить обработку данных
    else:
        return render(request, 'feedback.html',
                  {'forms':FeedbackForm})