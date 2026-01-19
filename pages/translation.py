from modeltranslation.translator import register, TranslationOptions

from .models import Item


@register(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'content')
    