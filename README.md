# MuffinBot

This is a work-in progress Discord Bot for Star Citizen organizations developed using the [interactions](https://discord-py-slash-command.readthedocs.io/en/latest/index.html) and [OpenAI](https://beta.openai.com/) libraries.

## Installation

1. Clone the repository

$ git clone https://github.com/<username>/python-discord-bot
$ cd python-discord-bot


2. Install the dependencies

$ pip install -r requirements.txt

3. Replace the `token` value in `main.py` with your own Discord API key.

4. Replace the `openai.api_key` value with your OpenAI API key.

## Usage

Start the bot by running the following command in the terminal:

$ python main.py


In a Discord channel, use the following commands to interact with the bot:

- `/creed_thoughts` - Retrieve a quote from Creed Bratton
- `/dunmiff` - Retrieve a quote from The Office
- `/test_ai` - Generates a response based on your input text
- `/server_status` - Retrieve information about the server status
- `/rules` - Retrieve the rules for the server

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
