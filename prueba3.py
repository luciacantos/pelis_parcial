import requests

url = "https://api.themoviedb.org/3/account/21660008/favorite/movies?language=en-US&page=1&sort_by=created_at.asc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMmRjMzIzYWI2NmU1NDk1YzI3NzkxZWE2NDY5ZTU1ZSIsIm5iZiI6MTczMjg5ODc5MC40MzcsInN1YiI6IjY3NDllZmU2MDkzNmI2ZTRmYjlmYTdhYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._1EC6VLF2wavTLLqKYSw4Ch5gMkekIPS40GTU8F4hXo"
}

response = requests.get(url, headers=headers)

print(response.text)