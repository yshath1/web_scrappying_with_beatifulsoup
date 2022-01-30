from bs4 import BeautifulSoup
import lxml
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
movies = response.text
soup = BeautifulSoup(movies, "lxml")
best_movies = soup.find_all(name="h3", class_="title")
best_movies_list = []
for tag in reversed(best_movies):
    best_movies_list.append(tag.getText())

num = 0
for x in best_movies_list:
    if num >= 1:
        with open("movies.txt", mode="a") as film:
            film.write(f'\n{x}')
    else:
        with open("movies.txt", mode="w") as film:
            film.write(f'{x}')
    num += 1
