
# SpotiBot

SpotiBot is a Python-based tool that integrates Spotify and OpenAI's GPT models to generate music recommendations and playlists based on a user's music taste profile.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## Features

- Generate a comprehensive and text based music taste profile based on user's Spotify data.
- Update the existing music taste profile.
- Recommend tracks based on the music taste profile and specific user prompts.
- Generate Spotify playlists with recommended tracks.

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/SpotiBot.git
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. Set up environment variables:
```
export SPOTIPY_CLIENT_ID=your_spotify_client_id
export SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
export SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
export OPENAI_API_KEY=your_openai_api_key
```

## Usage

To use SpotiBot, you can import it in your Python script as follows:

```
from spotibot import SpotiBot
```

Then, you can create an instance of the `SpotiBot` class and start using its methods.

```
bot = SpotiBot()
bot.generate_taste_profile_from_top_artists()
bot.generate_playlist("Something to listen to while coding")
```

This will generate a taste profile based on the recent top artists of your spotify account and create a suitable playlist based on the prompt that is passed to `generate_playlist`. This will create a new playlist under your spotify account with a suitable name.

## Testing

To run the tests, navigate to the project directory and execute:

```
python -m unittest discover tests
```

## Roadmap
### Short-Term Backlog
#### Improvements
* Error Handling: Enhance the robustness of API calls and other critical sections of the code.
* Type Annotations: Add type hints to all functions and classes for better readability and self-documentation.
#### Features
* Prompt Engineering Layers: Expand the layers responsible for generating prompts, keeping all content in JSON format for easier manipulation.
* Prompt Content: Refine the content of the prompts to improve the quality of the generated playlists.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

