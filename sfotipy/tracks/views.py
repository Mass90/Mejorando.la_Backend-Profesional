import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core import serializers

from .models import Track

def track_view(request, title):
#	try:
#		track = Track.objects.get(title=title)
#	except Track.DoesNotExist:
#		raise Http404

	#Esta linea hace todo lo que esta comentado
	track = get_object_or_404(Track, title=title)
	bio = track.artist.biography
	
	data = {
		'title': track.title,
		'order': track.order,
		'album': {
			'title': track.album.title
		},
		'artist': {
			'name': track.artist.first_name,
			'bio': bio,

		}
	}

	#default encoder
	json_data = json.dumps(data)

	#render HTML
	#return render(request, 'tracks.html', {'track': track, 'bio': bio})

	return HttpResponse(json_data, content_type='application/json')