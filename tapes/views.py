from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from tapes.models import Tape

def index(request):
	tapes = Tape.objects.all()[:5]
	return render(request, 'index.html', { 'tapes': tapes })