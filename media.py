'''The class Movie is defined by a title, poster image and a youtube trailer'''


class Movie():
    '''The constructor of the movie class:
    it defines the title,poster image and youtube URL'''
    def __init__(self, title, box_art, poster_image_url, trailer_youtube_url):
        self.title = title
        self.box_art = box_art
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
