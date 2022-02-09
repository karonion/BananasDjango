from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Articles


# Форма обратной связи. Страница "Контакты".
class FeedbackForm(forms.Form):
    contact = forms.CharField(required=True, help_text='Месенджер або пошта', label=r"How do we get in touch with you?", widget=forms.TextInput(attrs={'class':'form-control', 'style':'width: 400px'}))
    text = forms.CharField(required=True, label='Text', widget=forms.Textarea(attrs={'class':'form-control', 'style': 'height: 100px'}))


# Форма регистрации
class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, label="First name", widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    last_name = forms.CharField(required=True, label='Last name', widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={"class": "form-control form-control-sm"}))
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={"class": "form-control form-control-sm"}))
    confirm_password = forms.CharField(required=True, label='Password again', widget=forms.PasswordInput(attrs={"class": "form-control form-control-sm"}))  # Написать проверку на совпадение с первым паролем


# Создание поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('image', 'text', 'preview', 'title')
        widgets = {
            'text': SummernoteWidget,
            'preview': forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            'title': forms.TextInput(attrs={"class": "form-control form-control-sm"}),
        }