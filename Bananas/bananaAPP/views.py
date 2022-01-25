from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import FeedbackForm, PostForm
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


# Обратная связь
def feedback(request):
    if request.method == 'POST':
        feed = Feedback()
        feed.contact = request.POST.get('contact')
        feed.text = request.POST.get('text')
        feed.save()
        return HttpResponse('Агонь, всё получилось')
    else:
        return render(request, 'feedback.html',
                  {'forms':FeedbackForm})


# Получение обратной связи
def get_feedback(request):
    feed = Feedback.objects.all().order_by('-date')
    return render(request, 'getfeedback.html', {'feed':feed})


def add_post(request):
    if request.method == 'POST':
        image_form = PostForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
        return HttpResponseRedirect('/')
    else:
        image_form = PostForm()
        return render(request, 'addpost.html', {'image_form': image_form})


# Пост детально
def post_deatils(request, id):
    article = Articles.objects.get(id=id)
    return render(request, 'post.html', {'article': article})


def about_us(request):
    return render(request, 'About-us.html')