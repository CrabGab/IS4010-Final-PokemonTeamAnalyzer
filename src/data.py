# This file contains the data pools that you can customize.

# --------------------------
# POKÉMON AVAILABILITY
# --------------------------
# Add the names of Pokémon confirmed to be available in Pokémon Legends: Z-A.
# The names should be lowercase strings.
# --------------------------
Z_A_POKEMON = [
    "abra", "aegislash", "alakazam", "altaria", "ampharos", "arbok", "ariados", "aromatisse", "audino",
    "barbaracle", "bayleef", "beedrill", "bellsprout", "binacle", "budew", "buneary", "bunnelby",
    "camerupt", "chikorita", "clefable", "clefairy", "cleffa", "croconaw", "dedenne", "diggersby",
    "doublade", "drilbur", "eevee", "ekans", "electrike", "emboar", "espeon", "espurr", "excadrill",
    "feraligatr", "flaaffy", "flabébé", "flareon", "fletchinder", "fletchling", "floette", "florges",
    "gallade", "garbodor", "gardevoir", "gastly", "gengar", "glaceon", "gogoat", "gyarados",
    "haunter", "hippopotas", "hippowdon", "honedge", "houndoom", "houndour", "jolteon", "kadabra",
    "kakuna", "kirlia", "krokorok", "krookodile", "leafeon", "litleo", "lopunny", "machoke",
    "machop", "magikarp", "manectric", "mareep", "medicham", "meditite", "meganium", "meowstic",
    "numel", "pancham", "pangoro", "panpour", "pansage", "pansear", "patrat", "pidgeot",
    "pidgeotto", "pidgey", "pignite", "pikachu", "pichu", "pyroar", "raichu", "ralts", "roselia",
    "roserade", "sandile", "scatterbug", "scolipede", "shuppet", "simipour", "simisage",
    "simisear", "skiddo", "slurpuff", "spewpa", "spinarak", "spritzee", "starmie", "staryu",
    "swablu", "swirlix", "sylveon", "talonflame", "tepig", "totodile", "trubbish", "umbreon",
    "vanillish", "vanillite", "vanilluxe", "vaporeon", "venipede", "victreebel", "vivillon",
    "watchog", "weedle", "weepinbell", "whirlipede"
]

# --------------------------
# BOSS BATTLE DATA
# --------------------------
# Define the major boss battles to simulate against.
# This is a simplified format where you only need to provide the Pokémon names and levels.
# The script will fetch the rest of the data from the PokéAPI.
# --------------------------
KALOS_BOSSES = {
    'Early Trainers': {
        'Andi the Backpacker': [('pancham', 4)],
        'Brigitte the Waitress': [('cleffa', 4), ('bunnelby', 4)],
        'Urbain/Taunie of Team MZ (Chikorita)': [('totodile', 5), ('tepig', 5)],
        'Urbain/Taunie of Team MZ (Totodile)': [('tepig', 5), ('chikorita', 5)],
        'Urbain/Taunie of Team MZ (Tepig)': [('chikorita', 5), ('totodile', 5)],
        'Zach the Driver': [('slowpoke', 8), ('pidgey', 9), ('pikachu', 9)]
    },
    'Mid Trainers': {
        'Josee of the Fist of Justice': [('machop', 10), ('meditite', 11)],
        'Detective Emma': [('mareep', 15)],
        'Yvon the Office Worker': [('spritzee', 15), ('swirlix', 15), ('vivillon', 16)],
        'Naveen of Team MZ': [('spinarak', 16), ('sableye', 16), ('scraggy', 17)],
        'Xavi the Grade-Schooler': [('venipede', 20), ('roselia', 20), ('kadabra', 21), ('furfrou', 21)],
        'Lida of Team MZ': [('clauncher', 22), ('vanillite', 22), ('staryu', 23)],
        'Rintaro': [('simisage', 24), ('simipour', 24), ('simisear', 24)],
        'Urbain/Taunie of Team MZ (Chikorita - Mid)': [('croconaw', 25), ('pignite', 25), ('manectric-mega', 26)],
        'Urbain/Taunie of Team MZ (Totodile - Mid)': [('pignite', 25), ('bayleef', 25), ('manectric-mega', 26)],
        'Urbain/Taunie of Team MZ (Tepig - Mid)': [('bayleef', 25), ('croconaw', 25), ('manectric-mega', 26)],
        'Vinnie of Quasartico Inc.': [('houndoom', 30), ('sharpedo', 30), ('buneary', 30), ('drampa-mega', 32)]
    },
    'Syndicate Trainers': {
        'Rust Syndicate Grunt': [('garbodor', 44), ('lairon', 44)],
        'Philippe of the Rust Syndicate': [('steelix', 46), ('scizor', 46), ('skarmory-mega', 47)],
        'Gwynn of the Fist of Justice': [('banette', 45), ('gourgeist-average', 46), ('gengar', 46), ('chandelure-mega', 47)],
        'Francois of the SBC': [('gabite', 47), ('sliggoo', 47)],
        'Vivica of the SBC': [('aromatisse', 48), ('slurpuff', 48)],
        'Representative of Lumiose Safety Group': [('pinsir', 48), ('onix', 48), ('glalie', 49)],
        'Corbeau of the Rust Syndicate': [('arbok', 50), ('gyarados', 51), ('roserade', 51)]
    }
}
