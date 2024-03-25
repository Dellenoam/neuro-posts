# neuro-posts

Script that uses the Gemini API to generate the post and Telethon to send the post to the channel

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Dellenoam/neuro-posts.git
    ```

2. Change into the project directory:

    ```bash
    cd neuro-posts
    ```

3. Set up a virutal environment:

    For Windows

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    For Linux/MacOS

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install [poetry](https://python-poetry.org/docs#installation)

5. Install dependencies using poetry:

    ```bash
    poetry install --only main
    ```

6. Get you Gemini API key [here](https://ai.google.dev/)

7. Set up your telegram application [here](https://my.telegram.org/) to get your api id and api hash

8. Create an .env file in the project root and configure there these options

    ```
    TELETHON__API_ID = YOUR_APPLICATION_API_ID
    TELETHON__API_HASH = "YOUR_APPLICATION_API_HASH"
    TELETHON__CHANNEL_ID = ORIGINAL_CHANNEL_ID
    TELETHON__TEST_CHANNEL_ID = TEST_CHANNEL_ID
    GEMINI__API_KEY = "YOUR_API_KEY"
    DEBUG_MODE = False
    ```

    If you want to test first, set DEBUG_MODE to True

9. (Optionally) Change prompts

    You can change the promts that create a topic and the post itself on that topic. 
    To do this, make changes to the files in the prompts folder

    If you don't, your posts will be on IT topics and they will be in Russian language

9. Run the script

    ```bash
    python src/main.py
    ```

## Contributing

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.
