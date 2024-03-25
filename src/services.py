import re
import aiofiles
from google.generativeai import GenerativeModel


class TopicGenerator:
    def __init__(self, model: GenerativeModel) -> None:
        self._model = model

    async def generate(self) -> str:
        async with aiofiles.open("previous_topics.txt", "r") as file:
            previous_topics = await file.readlines()

        if len(previous_topics) > 10:
            del previous_topics[0]

        async with aiofiles.open("prompts/generate_topic.txt", "r") as file:
            generate_topic_prompt = await file.read()
            generate_topic_prompt = generate_topic_prompt.replace(
                "<<ПРЕДЫДУЩИЕ_ТЕМЫ>>", str(previous_topics)
            )

        topic = await self._model.generate_content_async(generate_topic_prompt)
        
        await self._write_topic_to_previous_topics(topic.text)

        return topic.text

    async def _write_topic_to_previous_topics(self, topic: str) -> None:
        async with aiofiles.open("previous_topics.txt", "a") as file:
            await file.write(topic + "\n")


class PostGenerator:
    def __init__(self, model: GenerativeModel, topic: str) -> None:
        self._model = model
        self._topic = topic

    async def generate(self, topic: str) -> str:
        async with aiofiles.open("prompts/generate_post.txt", "r") as file:
            generate_post_prompt = await file.read()
            generate_post_prompt = generate_post_prompt.replace("<<ТЕМА>>", topic)

        post = await self._model.generate_content_async(generate_post_prompt)
        post = re.sub(r"(```.+\n)", "```", post.text)

        return post
