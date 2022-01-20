from django import forms
from django_summernote.widgets import SummernoteWidget


# Форма обратной связи. Страница "Контакты".
class FeedbackForm(forms.Form):
    contact = forms.CharField(required=True, help_text='Месенджер або пошта', label=r"Як з вами зв'язатись?", widget=forms.TextInput(attrs={'class':'form-control'}))
    text = forms.CharField(required=True, label='Текст', widget=forms.TextInput(attrs={'class':'form-control'}))


# Форма логинизации
class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailField)
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput())
    remember_me = forms.BooleanField(label="Запам'ятати мене", initial=True)


# Форма регистрации.
class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, label="Ім'я")
    last_name = forms.CharField(required=True, label='Прізвище')
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True, label='Повторіть пароль', widget=forms.PasswordInput())  # Написать проверку на совпадение с первым паролем


# Создание поста
class Addpost(forms.Form):
    name = forms.CharField(required=True, label="Your name", widget=forms.TextInput(attrs={'size':50, 'rows':'10', 'cols':'10'}))
    preview = forms.CharField(required=True, label="Preview", widget=forms.TextInput(attrs={'size':50}))
    text = forms.CharField(widget=SummernoteWidget)
    preview_photo = forms.ImageField(required=False, label='Photo label')