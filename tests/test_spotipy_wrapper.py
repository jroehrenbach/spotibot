
import unittest
from spotibot import SpotipyWrapper  # Replace with the actual module name


def check_playlist_exists(spotipy_instance, playlist_id):
    try:
        playlist = spotipy_instance.playlist(playlist_id)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class TestSpotipyWrapper(unittest.TestCase):

    def setUp(self):
        self.wrapper = SpotipyWrapper()

    def test_get_liked_tracks(self):
        df = self.wrapper.get_liked_tracks(30, 10)
        self.assertIsNotNone(df)
        self.assertTrue('Track Name' in df.columns)
        self.assertTrue('Artists' in df.columns)

    def test_get_current_user_top_artist_names(self):
        artist_names = self.wrapper.get_current_user_top_artist_names()
        self.assertIsNotNone(artist_names)
        self.assertTrue(isinstance(artist_names, list))

    def test_search_tracks(self):
        track_uris = self.wrapper.search_tracks(['track:Imagine artist:John Lennon'])
        self.assertIsNotNone(track_uris)
        self.assertTrue(len(track_uris) > 0)

    def test_create_and_delete_playlist(self):
        # Create a playlist and add a track to it
        playlist_id = self.wrapper.create_playlist('Test Playlist', 'Test Description', ['spotify:track:3n3Ppam7vgaVa1iaRUc9Lp'])
        self.assertIsNotNone(playlist_id)

        # Validate that the playlist was actually created
        self.assertTrue(check_playlist_exists(self.wrapper.sp, playlist_id))

        # Cleanup: Delete the test playlist
        self.wrapper.delete_playlist(playlist_id)


if __name__ == '__main__':
    unittest.main()
