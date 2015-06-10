from games.models import Game
from games.serializers import GameSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

game = Game(title = 'Fifa 16',
	gamePicUrl = 'http://www.google.com/',
	pic1Url = 'http://www.google.com/',
	pic2Url = 'http://www.google.com/',
	pic3Url = 'http://www.google.com/',
	publisher = 'EA Sports',
	publishedDate = '2015-8-2',
	ratedInfo = 'Rated PEGI-3',
	gameCats = 'Sports/Team',
	trailerUrl = 'https://www.youtube.com/watch?v=B4L1HyM4ie0',
	buyUrl = 'http://www.amazon.com/',
	rating = 8.0,
	)

game.save()

game = Game(title = 'Assasins Creed 3',
	gamePicUrl = 'http://www.google.com/',
	pic1Url = 'http://www.google.com/',
	pic2Url = 'http://www.google.com/',
	pic3Url = 'http://www.google.com/',
	publisher = 'Ubisoft',
	publishedDate = '2013-10-5',
	ratedInfo = 'Rated PEGI-18',
	gameCats = 'Action/Adventure/Stealth',
	trailerUrl = 'https://www.youtube.com/watch?v=-pUhraVG7Ow',
	buyUrl = 'http://www.amazon.com/',
	rating = 8.5,
	)

game.save()



serializer = GameSerializer(game)
content = JSONRenderer().render(serializer.data)
print content