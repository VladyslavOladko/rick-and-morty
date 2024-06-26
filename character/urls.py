from django.urls import path

from character.views import get_random_character_view, CharacterListView

app_name = "character"

urlpatterns = [
    path("characters/random/", get_random_character_view, name="character-random"),
    path("characters/", CharacterListView.as_view(), name="character-list"),
]
