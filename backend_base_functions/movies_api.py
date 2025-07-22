import requests


class MoviesApiFunction:
    def __init__(self, base_url="", proxyconfig=None, requestlibrary: object = requests):
        self.base_url = base_url
        self.proxyconfig = proxyconfig
        self.requestlibrary = requestlibrary

    def get_movie_by_id(self, movie_id):
        url = f"{self.base_url}/api/films/{movie_id}"

        payload = {}
        headers = {}

        try:
            response = self.requestlibrary.request("GET", url, headers=headers, proxies=self.proxyconfig, verify=False)
            if response.status_code != 200:
                print("%s I am unable to reach the server to retrieve a movie record ", response.status_code)

            elif response is None:
                print("Invalid request with Null response captured")
            return response.json()
        except Exception as e:
            print('%s Error encountered :', {e})

    def get_all_movies(self):
        url = f"{self.base_url}/api/films"
        headers = {}

        try:
            response = self.requestlibrary.request("GET", url, headers=headers, proxies=self.proxyconfig, verify=False)
            if response.status_code != 200:
                print("%s I am unable to reach the server to all movies", response.status_code)
            elif response is None:
                print("Invalid request with Null response captured")
            return response.json()
        except Exception as e:
            print('%s Error encountered :', {e})
