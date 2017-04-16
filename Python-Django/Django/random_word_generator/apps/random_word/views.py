from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def index(request):
    if not 'attempt' in request.session:
		request.session['attempt'] = 0
		request.session['word'] = 'Click Generate Button for a Random String'
    return render(request, 'random.html')

def create(request):
	random_word = ''
	vowels = ['a','e','i','o','u','y']
	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
	for i in range(7):
		cons_index = random.randint(0,len(consonants)-1)
		random_word += consonants[cons_index]
		vow_index = random.randint(0,len(vowels)-1)
		random_word += vowels[vow_index]
	request.session['attempt'] += 1
	request.session['word'] = random_word
	return redirect('/')

def reset(request):
	del request.session['attempt']
	del request.session['word']
	return redirect('/')
