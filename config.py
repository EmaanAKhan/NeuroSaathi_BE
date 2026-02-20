import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH_MB", 50)) * 1024 * 1024
    ALLOWED_AUDIO_EXTENSIONS = set(
        os.getenv("ALLOWED_AUDIO_EXTENSIONS", "wav,mp3,ogg,m4a,webm").split(",")
    )
    ALLOWED_IMAGE_EXTENSIONS = set(
        os.getenv("ALLOWED_IMAGE_EXTENSIONS", "png,jpg,jpeg,webp").split(",")
    )
    GEMINI_API_KEY   = os.getenv("GEMINI_API_KEY", "")
    MEDGEMMA_API_KEY = os.getenv("MEDGEMMA_API_KEY", "")

class DevelopmentConfig(BaseConfig):
    DEBUG   = True
    TESTING = False

class TestingConfig(BaseConfig):
    DEBUG   = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG   = False
    TESTING = False

config_map = {
    "development": DevelopmentConfig,
    "testing":     TestingConfig,
    "production":  ProductionConfig,
}