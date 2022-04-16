from django import template


register = template.Library()


STRONG_WORDS = [
    'блаблабла',
    'Блаблабла',
    'глупая',
    'глупый',
]

@register.filter()
def censor(value):
   if not isinstance(value, str):
       raise ValueError('Нельзя цензурировать не строку')

   for word in STRONG_WORDS:
       value = value.replace(word[1:], '*' * (len(word)-1))

   return value




# @register.filter()
# def censor(text):
#     for word, initial in C_WORDS.items():
#         text = text.replace(word.lower(), initial)
#     return f'{text}'
