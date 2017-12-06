import media
import fresh_tomatoes


#-----------------------------------------------------------------------------------------------
"""each of the following variables represents a movie and takes input from Movie class and outputs the title of the movie, a poster with the movie and an youtube trailer link """
star_trek = media.Movie("Star Trek: Into darkness",
                        "http://www.imdb.com/title/tt1408101/?ref_=nv_sr_1",
                        "https://vignette.wikia.nocookie.net/memoryalpha/images/c/cc/Star_Trek_Into_Darkness_novelization_cover.jpg/revision/latest?cb=20130328184140&path-prefix=en",
                        "https://youtu.be/QAEkuVgt6Aw")

interstellar = media.Movie("Interstellar",
                           "http://www.imdb.com/title/tt0816692/?ref_=nv_sr_2",
                           "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/ZZ1B173521.jpg",
                           "https://youtu.be/zSWdZVtXT7E")

star_wars = media.Movie("Star Wars - Revenge of the Sith",
                        "http://www.imdb.com/title/tt0121766/?ref_=nv_sr_3",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_UY268_CR9,0,182,268_AL_.jpg",
                        "https://youtu.be/5UnjrG_N8hU")

tron = media.Movie("Tron: Legacy",
                   "http://www.imdb.com/title/tt1104001/?ref_=nv_sr_1",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4NTk4MTk1OF5BMl5BanBnXkFtZTcwNTE2MDIwNA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                   "https://youtu.be/L9szn1QQfas")

thor = media.Movie("Thor: Ragnarok",
                   "http://www.imdb.com/title/tt3501632/?ref_=nv_sr_1",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                   "https://youtu.be/ue80QwXMRHg")

bladerun = media.Movie("Blade Runner 2049",
                       "http://www.imdb.com/title/tt1856101/",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNzA1Njg4NzYxOV5BMl5BanBnXkFtZTgwODk5NjU3MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://youtu.be/gCcx85zbxz4")

pirates = media.Movie("Pirates of the Caribbean: At World's End",
                      "http://www.imdb.com/title/tt0449088/",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyNjkxNzEyMl5BMl5BanBnXkFtZTYwMjc3MDE3._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://youtu.be/HKSZtp_OGHY")

darknight = media.Movie("The Dark Knight Rises",
                        "http://www.imdb.com/title/tt1345836/",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://youtu.be/g8evyE9TuYk")

sholmes = media.Movie("Sherlock Holmes",
                      "http://www.imdb.com/title/tt0988045/",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0NjEwNjUxM15BMl5BanBnXkFtZTcwMzk0MjQ5Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://youtu.be/Egcx63-FfTE")

samurai = media.Movie("The Last Samurai",
                      "http://www.imdb.com/title/tt0325710/",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzkyNzQ1Mzc0NV5BMl5BanBnXkFtZTcwODg3MzUzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://youtu.be/T50_qHEOahQ")

gladiator = media.Movie("Gladiator",
                        "http://www.imdb.com/title/tt0172495/",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://youtu.be/ol67qo3WhJk")                                                                                        
#-----------------------------------------------------------------------------------------------

"""the following variable will be called as input for the fresh_tomatoes python page """
movies = [star_trek, interstellar, star_wars, tron, thor, bladerun, pirates, darknight, sholmes, samurai, gladiator]

#-----------------------------------------------------------------------------------------------

"""when fresh_tomatoes is called will open a new page in web browser and will show a list of movies """
fresh_tomatoes.open_movies_page(movies)
