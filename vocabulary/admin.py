from django.contrib import admin
from .models import Vocabulary

# Register your models here.
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ['word', 'definition']

admin.site.register(Vocabulary, VocabularyAdmin)
