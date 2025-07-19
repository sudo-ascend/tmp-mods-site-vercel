from django.contrib import admin
from modeltranslation.translator import register
from modeltranslation.admin import TranslationAdmin
from main.models import Comment, Mod, New

admin.site.register(Comment)

@admin.register(New)
class NewAdmin(TranslationAdmin):
    pass

@admin.register(Mod)
class ModTranslationOptions(TranslationAdmin):
    pass