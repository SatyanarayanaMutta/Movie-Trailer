import media,fresh_tomatoes

toy_story=media.Movie("Toy Story","A story of Boys and his Toys that come to Life.",
                      "https://cdn.europosters.eu/image/3d/15473.gif",
                      "https://www.youtube.com/watch?v=v-PjgYDrg70")

#print(toy_story.storyline)

#toy_story.show_trailer()

avatar=media.Movie("AVATAR","When his brother is killed in a robbery, paraplegic Marine Jake Sully decides to take his place in a mission on the distant world of Pandora.",
                   "https://image.slidesharecdn.com/presentation-avatarfilmposteranalysis-150303060114-conversion-gate01/95/avatar-film-poster-analysis-1-638.jpg?cb=1425363082",
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8")


movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
