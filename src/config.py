from typing import Dict, List
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from google.generativeai.types import GenerationConfig


class TelethonSettings(BaseModel):
    api_id: int
    api_hash: str
    channel_id: int
    test_channel_id: int

    system_version: str = "4.16.30-vx3364"


class GeminiSettings(BaseModel):
    generation_config: GenerationConfig = GenerationConfig(
        temperature=1, max_output_tokens=4096
    )
    safety_settings: List[Dict[str, str]] = [
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]
    generative_model_name: str = "gemini-pro"
    api_key: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__")

    debug_mode: bool
    telethon: TelethonSettings
    gemini: GeminiSettings


settings = Settings()  # type: ignore
