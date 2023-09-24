"""
This module contains a wrapper class for the Spotipy library.
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from datetime import datetime, timedelta
import os


CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')
SCOPE = "user-library-read playlist-modify-public user-top-read playlist-modify-private"


class SpotipyWrapper:
    """
    A wrapper class for the Spotipy library.
    """

    def __init__(self, client_id=None, client_secret=None, redirect_uri=None, scope=None):
        """
        Parameters
        ----------
        client_id : str
            Spotify client ID.
        client_secret : str
            Spotify client secret.
        redirect_uri : str
            Spotify redirect URI.
        scope : str
            Spotify scope.
        """
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id or CLIENT_ID,
                                                            client_secret=client_secret or CLIENT_SECRET,
                                                            redirect_uri=redirect_uri or REDIRECT_URI,
                                                            scope=scope or SCOPE))

    def get_liked_tracks(self, time_range_days, track_limit):
        """
        Get a list of liked tracks from the current user's Spotify library.

        Parameters
        ----------
        time_range_days : int
            Number of days to look back for liked tracks.
        track_limit : int
            Maximum number of tracks to return.

        Returns
        -------
        pd.DataFrame
            A Pandas DataFrame containing the liked tracks.
        """
        time_range_start = (datetime.utcnow() - timedelta(days=time_range_days)).date()

         # Initialize empty list to hold track data
        track_data = []

        # Fetch the first batch of liked tracks
        results = self.sp.current_user_saved_tracks()
        while results:
            for item in results['items']:
                track = item['track']
                track_name = track['name']
                date_liked = datetime.strptime(item['added_at'], '%Y-%m-%dT%H:%M:%SZ').date()

                artists = ', '.join([artist['name'] for artist in track['artists']])
                #album = track['album']['name']
                release_date = track['album']['release_date']

                #audio_features = sp.audio_features([track['id']])[0]
                #danceability = audio_features['danceability']
                #energy = audio_features['energy']

                track_data.append([track_name, artists, release_date, date_liked])
            
            if len(track_data) >= track_limit:
                track_data = track_data[:track_limit]
                break

            if results['next']:
                results = self.sp.next(results)
            else:
                results = None

        # Create a Pandas DataFrame
        df = pd.DataFrame(track_data, columns=['Track Name', 'Artists', 'Release Date', 'Date Liked'])
        df = df[df['Date Liked'] >= time_range_start]
        return df
    
    def get_current_user_top_artist_names(self, time_range='medium_term', limit=30):
        """
        Get a list of the current user's top artists.

        Parameters
        ----------
        time_range : str
            Time range for top artists. Valid values are 'short_term', 'medium_term', and 'long_term'.
        limit : int
            Maximum number of artists to return.

        Returns
        -------
        list
            A list of the current user's top artists.
        """
        results = self.sp.current_user_top_artists(time_range=time_range, limit=limit)
        return [item['name'] for item in results['items']]

    def search_tracks(self, track_query_list):
        """
        Search for tracks on Spotify and return top results.

        Parameters
        ----------
        track_query_list : list
            A list of track queries.

        Returns
        -------
        list
            A list of track URIs.
        """
        track_uris = []
        for track_query in track_query_list:
            results = self.sp.search(q=track_query, type='track', limit=1)
            if results['tracks']['items']:
                track_uris.append(results['tracks']['items'][0]['uri'])
        return track_uris
    
    def search_tracks_from_json(self, tracks_json):
        """
        Search for tracks on Spotify and return top results.

        Parameters
        ----------
        tracks_json : list
            A list of track JSON objects.

        Returns
        -------
        list
            A list of track URIs.
        """
        track_query_list = [
            " ".join([f"{key}:{value}" for key, value in track_json.items()])
            for track_json in tracks_json
        ]
        return self.search_tracks(track_query_list)

    def create_playlist(self, name, description, track_uris):
        """
        Create a playlist on Spotify.
        
        Parameters
        ----------
        name : str
            Name of the playlist.
        description : str
            Description of the playlist.
        track_uris : list
            A list of track URIs.

        Returns
        -------
        str
            The playlist ID.
        """
        playlist = self.sp.user_playlist_create(user=self.sp.me()['id'], name=name, public=True, collaborative=False, description=description)
        self.sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
        return playlist['id']

    def create_playlist_from_json(self, name, description, tracks_json):
        """
        Create a playlist on Spotify.
        
        Parameters
        ----------
        name : str
            Name of the playlist.
        description : str
            Description of the playlist.
        tracks_json : list
            A list of track JSON objects.
        
        Returns
        -------
        str
            The playlist ID.
        """
        track_uris = self.search_tracks_from_json(tracks_json)
        if len(track_uris) == 0:
            return None
        return self.create_playlist(name, description, track_uris)

    def delete_playlist(self, playlist_id):
        """
        Delete a playlist on Spotify.

        Parameters
        ----------
        playlist_id : str
            The playlist ID.
        """
        self.sp.user_playlist_unfollow(user=self.sp.me()['id'], playlist_id=playlist_id)
