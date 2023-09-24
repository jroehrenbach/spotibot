
import unittest
from spotibot import SpotiBot  # Replace 'your_package' with the actual package name


class TestSpotiBot(unittest.TestCase):

    def setUp(self):
        self.spotibot = SpotiBot()

    def test_initiate_taste_profile(self):
        self.spotibot.initiate_taste_profile("Test User Data")
        self.assertIsNotNone(self.spotibot.taste_profile)

    def test_update_taste_profile(self):
        self.spotibot.taste_profile = "Existing Mocked Taste Profile"
        self.spotibot.update_taste_profile("Test User Data")
        self.assertIsNotNone(self.spotibot.taste_profile)

    def test_generate_taste_profile_from_top_artists(self):
        self.spotibot.generate_taste_profile_from_top_artists()
        self.assertIsNotNone(self.spotibot.taste_profile)

    def test_recommend_tracks(self):
        result = self.spotibot.recommend_tracks("I like rock music")
        self.assertIsNotNone(result)

    def test_generate_playlist(self):
        result = self.spotibot.generate_playlist("I like rock music")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
