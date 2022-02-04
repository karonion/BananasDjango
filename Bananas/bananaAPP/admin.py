from django.contrib import admin
from .models import Articles, Feedback
from django_summernote.admin import SummernoteModelAdmin


# Класс Summernote наследует admin.ModelAdmin. Для добавления TextArea Summernote
class SummernoteModelForTextArea(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('title', 'preview', 'created_date')
    fields = ('title', 'preview', 'text', 'created_by', 'created_date', 'category', 'image')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('contact', 'date')
    fields = ('contact', 'text', 'date')


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Articles, SummernoteModelForTextArea)




