from django.shortcuts import render

def index(request):
	context = {
	'foto' : 'img/Kevin Asyraf.jpg',
	}
	return render(request, 'index.html', context)