from django.http import HttpResponse
from django.shortcuts import render

rezultatai = ('pirmas', 'antras', 'trecias', 'ketvirtas', 'penktas')

def hello(request):
	return render(request, 'index.html', {'results': rezultatai})
	#return HttpResponse(hello_again())