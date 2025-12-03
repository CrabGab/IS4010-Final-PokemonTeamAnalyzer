import pytest
from src.analyzer import check_availability, analyze_team_defenses

def test_check_availability():
    """
    Tests the check_availability function.
    """
    # Test with a mix of available and unavailable Pokémon
    pokemon_to_check = ["pikachu", "charizard", "squirtle"]
    availability = check_availability(pokemon_to_check)

    assert availability["pikachu"] is True
    assert availability["charizard"] is False
    assert availability["squirtle"] is False

def test_analyze_team_defenses():
    """
    Tests the analyze_team_defenses function.
    """
    # Mock team data
    team_data = [
        {
            "name": "charizard",
            "types": [
                {"type": {"name": "fire"}},
                {"type": {"name": "flying"}}
            ]
        },
        {
            "name": "blastoise",
            "types": [
                {"type": {"name": "water"}}
            ]
        },
        {
            "name": "venusaur",
            "types": [
                {"type": {"name": "grass"}},
                {"type": {"name": "poison"}}
            ]
        }
    ]

    coverage = analyze_team_defenses(team_data)

    # Test a few key types
    assert coverage["rock"]["weak"] == 1
    assert coverage["water"]["resist"] == 2
    assert coverage["electric"]["weak"] == 2
    assert coverage["ground"]["immune"] == 1