
import fresh_tomatoes
import media

# First instance of class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to his life.",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


# Second instance of class Movie
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://conversationsabouther.net/wp-content/uploads/2015/06/f7bc7b19e7f8555ba0f36aa3f2bc5dcd.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


# Third instance of class Movie
A_walk_to_remember = media.Movie("A walk to remember",
                                 "The story of two North Carolina teens,"
                                 " who are thrown together after "
                                 " Landon gets into trouble and "
                                 " is made to do community service",
                                 "http://nicholassparks.com/wp-content/uploads/2013/07/200201-a-walk-to-remember.jpeg",  # NOQA
                                 "https://www.youtube.com/watch?v=i72wRvPw_ik")


# Fourth instance of class Movie
predestination = media.Movie("Predestination", "time travel",
                             "http://www.soundfirm.com/admin/wp-content/uploads/32d9bd181d51b1be26b4ded7c4dc8ebe975bc922.jpg__620x465_q85_crop_upscale.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=UVOpfpYijHA")


# Fifth instance of class Movie
gravity = media.Movie("Gravity", "Dr. Ryan Stone (Sandra Bullock) "
                      "is a biomedical engineer "
                      " aboard the NASA space shuttle Explorer for "
                      " her first space mission, STS-157."
                      " Veteran astronaut Matt Kowalski (George Clooney) "
                      " is commanding his final mission.",
                      "http://highwaytomars.com/wp-content/uploads/2016/03/gravity.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=OiTiKOy59o4")


# Sixth instance of class Movie
avengers = media.Movie("Avengers", "Avengers, is a 2012 American "
                       "superhero film based on the Marvel Comics superhero"
                       " team of the same name, produced by Marvel Studios "
                       " and distributed by Walt Disney"
                       "Studios Motion Pictures.",
                       "https://i.ytimg.com/vi/48fKIXlxaXk/maxresdefault.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# List of movies in the variable 'movies'
movies = [toy_story, avatar, A_walk_to_remember,
          predestination, gravity, avengers]

# Calling the function open_movies_page in fresh_tomatoes module with
# argument 'movies' that contains the list of movies
fresh_tomatoes.open_movies_page(movies)
