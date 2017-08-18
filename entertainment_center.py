'''
Here are defined all the instances of the class Movie,
once all the movies are created the fresh_tomatoes
module is used to create the HTML of the website
and display it in the browser
'''
import media
import fresh_tomatoes

# Life is beautiful movie: movie title, box art, poster image, youtube trailer
life_is_beautiful = media.Movie(
    "Life Is Beautiful",
    "Box Art",
    "https://www.gstatic.com/tv/thumb/movieposters/22005/p22005_p_v8_aa.jpg",  # NOQA
    "https://www.youtube.com/watch?v=pAYEQP8gx3w")

# A space odissey movie: movie title, box art, poster image, youtube trailer
a_space_odissey = media.Movie(
    "2001 A Space Odyssey",
    "Box Art",
    "https://t0.gstatic.com/images?q=tbn:ANd9GcQdmmLZ7lXsw1WRy7c5qN3mka2e9ANSpHIG2INi53P6OVS8KyJo",  # NOQA
    "https://www.youtube.com/watch?v=UgGCScAV7qU")

# Pulp fiction movie: movie title, box art, poster image, youtube trailer
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "Box Art",
    "https://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg",  # NOQA
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Dr. Strange Love movie: movie title, box art, poster image, youtube trailer
dr_strange_love = media.Movie(
    "Dr. Strange Love",
    "Box Art",
    "https://t0.gstatic.com/images?q=tbn:ANd9GcRh424VS2g2AvU1K703L7gL66S60OM7s4FfBYkPTWDM3pTpyK2G",  # NOQA
    "https://www.youtube.com/watch?v=IutX5AGEYZc")

# Gattaca movie: movie title, box art, poster image, youtube trailer
gattaca = media.Movie(
    "Gattaca",
    "Box Art",
    "https://t3.gstatic.com/images?q=tbn:ANd9GcTJCzakHOgglpJK1AqgI1HICJx9dFsEwZtDW5rQB69oM9cvz-Fu",  # NOQA
    "https://www.youtube.com/watch?v=BpzVFdDeWyo")

# Fear and Loathing in Las Vegas movie:
# movie title, box art, poster image, youtube trailer
fear_and_loathing_in_las_vegas = media.Movie(
    "Fear and Loathing in Las Vegas",
    "Box Art",
    "https://www.gstatic.com/tv/thumb/movieposters/20996/p20996_p_v8_ae.jpg",  # NOQA
    "https://www.youtube.com/watch?v=8m662obIvhY")

# Array with all the movies present in the web page
movies = [
    life_is_beautiful,
    a_space_odissey,
    pulp_fiction,
    dr_strange_love,
    gattaca,
    fear_and_loathing_in_las_vegas
    ]

# Generate the HTML file with all the movies and open it the webbrowser
fresh_tomatoes.open_movies_page(movies)
