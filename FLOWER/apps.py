from django.apps import AppConfig
import nltk

nltk.download("stopwords")

class FlowerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FLOWER'
