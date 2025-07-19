from modeltranslation.translator import register, TranslationOptions
from .models import Mod, New


@register(Mod)
class ModTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'content')