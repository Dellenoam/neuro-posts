import asyncio
import time
import google.generativeai as genai
from telethon import TelegramClient
from services import PostGenerator, TopicGenerator
from config import settings


async def main():
    genai.configure(api_key=settings.gemini.api_key)

    model = genai.GenerativeModel(
        settings.gemini.generative_model_name,
        generation_config=settings.gemini.generation_config,
        safety_settings=settings.gemini.safety_settings,
    )

    telegram_client = TelegramClient(
        "my_account",
        api_id=settings.telethon.api_id,
        api_hash=settings.telethon.api_hash,
    )

    while True:
        topic_generator = TopicGenerator(model)
        topic = await topic_generator.generate()

        post_generator = PostGenerator(model, topic)
        post = await post_generator.generate(topic)

        async with telegram_client:
            if settings.debug_mode:
                await telegram_client.send_message(
                    settings.telethon.test_channel_id, post
                )
            else:
                await telegram_client.send_message(settings.telethon.channel_id, post, parse_mode="markdown")

        print(f"Generated post: {topic}")
        print(f"Time: {time.ctime()}")
        print(f"Next post will be generated at {time.ctime(time.time() + 10800)}")
        print()

        if settings.debug_mode:
            if (
                input('Press Enter to continue or type "stop" to stop the script: ')
                == "stop"
            ):
                print("Stopping the script...")
                break
            print()
            continue

        await asyncio.sleep(10800)


if __name__ == "__main__":
    asyncio.run(main())
