from django import forms


class FeedbackForm(forms.Form):
    contact = forms.CharField(required=True, help_text='Месенджер або пошта', label=r"Як з вами зв'язатись?", widget=forms.TextInput(attrs={'class':'form-control'}))
    text = forms.CharField(required=True, label='Текст', widget=forms.TextInput(attrs={'class':'form-control'}))