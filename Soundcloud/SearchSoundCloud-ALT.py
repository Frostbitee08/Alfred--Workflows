import soundcloud
from Feedback import Feedback

client = soundcloud.Client(client_id='0c61ce131a2c1db8e56059446e33456a')

feedback = Feedback()
tracks = client.get('/tracks', q="{query}", limit=9)
for track in tracks:
	artist = client.get('/users/' + str(track.user_id))
	url = "http://www.soundcloud.com/" + artist.permalink + '/' + track.permalink
	feedback.add_item(track.title, artist.permalink, url)

print feedback