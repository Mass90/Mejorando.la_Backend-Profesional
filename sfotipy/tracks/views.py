from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Track

def track_view(request, title):
#	try:
#		track = Track.objects.get(title=title)
#	except Track.DoesNotExist:
#		raise Http404

	#Esta linea hace todo lo que esta comentado
	track = get_object_or_404(Track, title=title)
	bio = track.artist.biography
	
	return render(request, 'tracks.html', {'track': track, 'bio': bio})