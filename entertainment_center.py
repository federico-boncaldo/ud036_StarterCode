import media
import fresh_tomatoes

#instantiate all the movies
life_is_beautiful = media.Movie("Life Is Beautiful", "Box Art", "https://www.gstatic.com/tv/thumb/movieposters/22005/p22005_p_v8_aa.jpg", "https://www.youtube.com/watch?v=pAYEQP8gx3w")

a_space_odissey = media.Movie("2001 A Space Odyssey", "Box Art", "https://t0.gstatic.com/images?q=tbn:ANd9GcQdmmLZ7lXsw1WRy7c5qN3mka2e9ANSpHIG2INi53P6OVS8KyJo", "https://www.youtube.com/watch?v=UgGCScAV7qU")

pulp_fiction = media.Movie("Pulp Fiction", "Box Art", "https://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

dr_strange_love = media.Movie("Dr. Strange Love", "Box Art", "https://t0.gstatic.com/images?q=tbn:ANd9GcRh424VS2g2AvU1K703L7gL66S60OM7s4FfBYkPTWDM3pTpyK2G", "https://www.youtube.com/watch?v=IutX5AGEYZc")

gattaca = media.Movie("Gattaca", "Box Art", "https://t3.gstatic.com/images?q=tbn:ANd9GcTJCzakHOgglpJK1AqgI1HICJx9dFsEwZtDW5rQB69oM9cvz-Fu", "https://www.youtube.com/watch?v=BpzVFdDeWyo")

fear_and_loathing_in_las_vegas = media.Movie("Fear and Loathing in Las Vegas", "Box Art", "https://www.gstatic.com/tv/thumb/movieposters/20996/p20996_p_v8_ae.jpg", "https://www.youtube.com/watch?v=8m662obIvhY")


movies = [life_is_beautiful, a_space_odissey, pulp_fiction, dr_strange_love, gattaca, fear_and_loathing_in_las_vegas]

#display the movies page in the browser
fresh_tomatoes.open_movies_page(movies)
