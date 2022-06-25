def instadownloader(link):
    import requests
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url":link}
    headers = {
        "X-RapidAPI-Key": "9d51372fefmshbfca66e3e2180ecp1d0d1djsn1daeffa7b097",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    import json
    rest = json.loads(response.text)
    return rest
