
import unittest
from spotibot import OpenAIWrapper  # Replace 'your_module' with the actual module name


class TestOpenAIWrapper(unittest.TestCase):

    def setUp(self):
        self.wrapper = OpenAIWrapper()

    def test_generate_text(self):
        messages = [
            {
                "role": "system",
                "content": "You are an assistant."
            },
            {
                "role": "user",
                "content": "Who won the world series in 2020?"
            }
        ]
        result = self.wrapper.generate_text(messages)
        self.assertIsInstance(result, str)  # Check if the result is a string

if __name__ == '__main__':
    unittest.main()
