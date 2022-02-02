from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .forms import FeedbackForm, PostForm, RegisterForm
from .models import Feedback, Articles


def index(request):  # Главная страница
    article_scope = Articles.objects.all().order_by('-created_date')  # Получаем все посты отсортированные по дате
    return render(request, 'index.html', {'article_scope': article_scope})


def contact(request):  # Контакты
    return HttpResponse('<h2> Our contacts </h2>')


def index_app(request):  # Приложение
    data = {
        'header': 'Заголовок переданного сообщения',
        'message': 'Сообщение'
    }
    return render(request, 'bananaAPP/index_app.html', context=data)


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
    if request.method == 'POST':
        pass
    else:
        article = Articles.objects.get(id=id)
        return render(request, 'post.html', {'article': article})


# О нас + форма обратной связи
def about_us(request):
    if request.method == 'POST':
        feed = Feedback()
        feed.contact = request.POST.get('contact')
        feed.text = request.POST.get('text')
        feed.save()
        messages.add_message(request, messages.SUCCESS, 'Thank you for feedback, we are going to contact with you!')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'About-us.html',  {'forms': FeedbackForm})


# Регистрация
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['email']
            email = request.POST['email']
            password = request.POST['password']
            print(f'username is {username}, password is {password}, email is {email}')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for registration, your login and password have been sent to email.')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Not valid')
    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
