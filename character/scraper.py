import requests

from django.conf import settings
from character.models import Character


def scrape_characters() -> list[Character]:

    next_url_to_scrape = requests.get(
        settings.RICK_AND_MORTY_API_CHARACTERS_URL
    )
    characters = []

    while next_url_to_scrape is not None:

        character_response = next_url_to_scrape.json()

        for character_dict in character_response["result"]:

            characters.append(
                Character(
                    api_id=character_dict["id"],
                    name=character_dict["name"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )

        next_url_to_scrape = character_response["info"]["next"]

    return characters


def save_characters(characters: list) -> None:
    for character in characters:
        character.save()


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
