import requests

class Spotify:
    BASE_URL = "https://api.spotify.com/v1/me/player/{}"

    def __init__(self, token: str):
        self.session = requests.session()
        self.token = token
    
    def get_currently_playing(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer '.join(self.token)
        }

        req = self.session.get(self.BASE_URL.format("current-playing"), headers=headers)

        if not req or req.status_code != 200:
            return
        
        return req.json()