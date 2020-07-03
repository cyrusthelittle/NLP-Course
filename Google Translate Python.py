import googletrans
from googletrans import Translator

translator = Translator()
print('Enter your text...')
sourceText=input()
a=translator.detect(sourceText)
if a.lang == 'fa':
    print('متن فارسی است')
    destText=translator.translate(sourceText, dest='en')
if a.lang == 'en':
    print('text is English')
    destText=translator.translate(sourceText, dest='fa')

print(destText.text)
