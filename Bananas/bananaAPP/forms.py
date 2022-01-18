from django import forms


class FeedbackForm(forms.Form):  # Форма обратной связи. Страница "Контакты".
    contact = forms.CharField(required=True, help_text='Месенджер або пошта', label=r"Як з вами зв'язатись?", widget=forms.TextInput(attrs={'class':'form-control'}))
    text = forms.CharField(required=True, label='Текст', widget=forms.TextInput(attrs={'class':'form-control'}))


class LoginForm(forms.Form):  # Форма логинизации
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailField)
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput())
    remember_me = forms.BooleanField(label="Запам'ятати мене", initial=True)


class RegisterForm(forms.Form):  # Форма регистрации.
    first_name = forms.CharField(required=True, label="Ім'я")
    last_name = forms.CharField(required=True, label='Прізвище')
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True, label='Повторіть пароль', widget=forms.PasswordInput())  # Написать проверку на совпадение с первым паролем


class Addpost(forms.Form):  # Создание поста
    name = forms.CharField(required=True, label="Ім'я")
    preview = forms.CharField(required=True, label="Прев'ю")
    preview_photo = forms.ImageField(required=True, label='Фото')