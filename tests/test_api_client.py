import pytest
from src.api_client import fetch_pokemon_data

def test_fetch_pokemon_data():
    """
    Tests the fetch_pokemon_data function.
    """
    # Test with a valid Pokémon
    data = fetch_pokemon_data("pikachu")
    assert data is not None
    assert data["name"] == "pikachu"

    # Test with an invalid Pokémon
    data = fetch_pokemon_data("not-a-pokemon")
    assert data is None
