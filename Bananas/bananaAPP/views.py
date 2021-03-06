from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
from django.views.generic import ListView
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .forms import FeedbackForm, PostForm, RegisterForm
from .models import Feedback, Articles


def index(request):  # Главная страница
    article_scope = Articles.objects.all().order_by('-created_date')  # Получаем все посты отсортированные по дате
    # Пагинация
    paginator = Paginator(article_scope, 6)  # Пагинация по 6 элементов
    page_number = request.GET.get('page')  # Узнаём номер страницы
    page_obj = paginator.get_page(page_number)  # По номеру страницы передаём список обьектов
    return render(request, 'index.html', {'page_obj': page_obj})


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


#  Добавление поста для демонстрации Юзеру
def add_post(request):
    if request.method == 'POST':
        image_form = PostForm(request.POST, request.FILES)
        if image_form.is_valid():
            #image_form.save()
            return HttpResponseForbidden()
    else:
        image_form = PostForm()
        return render(request, 'addpost.html', {'image_form': image_form})


# Пост детально
def post_deatils(request, id):
    if request.method == 'POST':
        pass  # Для лайков\комментариев
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
        #  Отправляем администратору уведомление о новом фидбеке
        send_mail(
            'New feedback!',
            f'New feedback from {feed.contact} with text {feed.text}.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_TO_EMAIL],
            fail_silently=False
        )
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
            confirm_password = request.POST['confirm_password']
            if password != confirm_password:  # Если пароли не совпадают - сообщаем юзеру и редиректим на регистрацию
                messages.add_message(request, messages.WARNING, 'Passwords does not match, please try again!')
                return HttpResponseRedirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                # Отправка сообщения на почту об успешной регистрации с логином и паролем
                msg = render_to_string('registration/registration-succesful.html', {'login': username,
                                                                                    'password': password})  # Собираем сообщение
                send_mail(
                    'Registration succesful',
                    msg,
                    settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[f'{email}'],
                    fail_silently=False,
                    html_message=msg  # Указываем, что сообщение - HTML файл
                )
                #  Редирект на главную страницу с сообщением об успешной регистрации
                messages.add_message(request, messages.SUCCESS, 'Thank you for registration, your login and password have been sent to email.')
                return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})


# Выдача результатов поиска по сайту
class SearchResultsView(ListView):
    model = Articles
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        # Собираем список результатов, включаем результаты по параметрам.
        object_list = Articles.objects.filter(Q(text__icontains=query) |
                                              Q(preview__icontains=query) |
                                              Q(title__icontains=query))
        return object_list
