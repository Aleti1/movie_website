import webbrowser





class Movie():
    """This class provides a way to store movie related information
       and to replay trailers for each movie from a given link """



#-----------------------------------------------------------------------------------------------

 #This function will take as input the variables movie title, movie poster and youtube trailer
    def __init__(self, movie_title, movie_info, poster_image, trailer_youtube):
        self.title = movie_title
        self.info  = movie_info
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#-----------------------------------------------------------------------------------------------

#this function will take input the self variable from __init__ function and the output will be the youtube movie trailer """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
#this will open a link where each movie has it's information (www.imdb.com)
    def show_info(self):
        webbrowser.open(self.movie_info_url)
