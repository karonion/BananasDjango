"""Bananas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from bananaAPP import views
from django.views.defaults import permission_denied
from functools import partial as curry


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # Админка
    path('', views.index, name='home'),  # Главная страница
    path('bananaAPP', views.index_app, name='index_app'),  # Приложение
    path('getfeedback', views.get_feedback, name='get_feedback'),  # Обратная связь (для админа)
    path('addpost', views.add_post, name='add_post'),  # Создание поста
    path('summernote/', include('django_summernote.urls')),  # Ссылка для передачи summernote
    path('post/<int:id>', views.post_deatils, name='post_details'),  # Пост детально
    path('upload/', views.add_post),  # Для загрузки файлов на сервер
    path('about', views.about_us, name='about_us'),  # О нас
    path('register', views.register, name='registration'),  # Регистрация
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]

# Дополнительная проверка для summernote
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
