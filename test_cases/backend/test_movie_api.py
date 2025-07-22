import requests

from backend_base_functions.movies_api import MoviesApiFunction

movies_object = MoviesApiFunction(
    base_url="https://swapi-node.vercel.app",
    requestlibrary=requests
)


def test_movie_count():
    res = movies_object.get_all_movies()
    count = res["count"]
    assert count == 6


def test_get_3rd_movie():
    res = movies_object.get_movie_by_id(3)
    movie_director = res["fields"]["director"]
    assert movie_director == "Richard Marquand"


def test_get_5th_movie():
    res = movies_object.get_movie_by_id(5)
    movie_director = res["fields"]["producer"]
    assert movie_director != "Gary Kurtz, George Lucas"
