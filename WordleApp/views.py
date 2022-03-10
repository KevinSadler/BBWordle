from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from random_word import RandomWords
from django.template import RequestContext

from WordleApp.forms import wordle

def index(request):
    template = loader.get_template('WordleApp/index.html')
    return HttpResponse(template.render({}, request))

def gameView(request):
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective", minDictionaryCount = 3, minLength=5, maxLength=5)
    form = wordle()
    guesses = ["Beers"]
    return render(request, 'WordleApp/index.html', {'form': form, 'magicWord': word, 'guesses': guesses})

def handleSubmit(request):
     if request.method == 'POST':
        value = request.POST.get('guess', None)
        print(value)
        return HttpResponse(value)