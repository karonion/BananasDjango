from django.contrib import admin
from .models import Articles, Feedback, User
from django_summernote.admin import SummernoteModelAdmin


# Класс Summernote наследует admin.ModelAdmin. Для добавления TextArea Summernote
class SummernoteModelForTextArea(SummernoteModelAdmin):
    summernote_fields = ('text', 'preview')
    list_display = ('title', 'preview', 'created_by', 'created_date')
    fields = ('title', 'preview', 'text', 'created_by', 'created_date', 'rank', 'category')


'''Для изменения отображения данных без класса SummerNote'''
'''class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'created_by', 'created_date')
    fields = ('name', 'preview', 'text', 'created_by', 'created_date', 'rank', 'category')'''


admin.site.register(Feedback)
admin.site.register(User)
admin.site.register(Articles, SummernoteModelForTextArea)




