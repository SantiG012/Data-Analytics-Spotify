import json
#gets the JSON top artists data from the user-json folder
def get_top_artists_json()->dict:
    with open('user-json/user_top_artists.json', 'r') as archivo:
        return json.load(archivo)

#opens the JSON top artists data and returns a dict with the artist name and a default value of 0
def get_top_artists_dict()->dict:
    top_artists_json = get_top_artists_json()
    top_artists_dict = {}
    for artist in top_artists_json['items']:
        top_artists_dict[artist['name']] = 0
    return top_artists_dict

#gets the JSON top tracks data from the user-json folder
def get_top_tracks_json()->dict:
    with open('user-json/user_top_tracks.json', 'r') as archivo:
        return json.load(archivo)
    
#gets the JSON saved tracks data from the user-json folder
def get_saved_tracks_json()->dict:
    with open('user-json/user_liked_tracks.json', 'r') as archivo:
        return json.load(archivo)
    
#opens the JSON top tracks data and counts the artists in the top tracks and adds them to the top artists dict
def get_top_tracks_dict(top_artists_dict:dict)->dict:
    top_tracks_json = get_top_tracks_json()
    for track in top_tracks_json['items']:
        for artist in track['artists']:
            top_artists_dict[artist['name']] += 1
    return top_artists_dict

#opens the JSON saved tracks data and counts the artists in the saved tracks and adds them to the top artists dict
def get_saved_tracks_dict(top_artists_dict:dict)->dict:
    saved_tracks_json = get_saved_tracks_json()
    for track in saved_tracks_json['items']:
        for artist in track['track']['artists']:
            top_artists_dict[artist['name']] += 1
    return top_artists_dict