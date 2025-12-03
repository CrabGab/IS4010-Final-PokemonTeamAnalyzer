import click
from rich.console import Console
from rich.table import Table

from src.api_client import fetch_pokemon_data
from src.analyzer import check_availability, analyze_team_defenses, analyze_boss_matchups, ALL_TYPES
from src.data import KALOS_BOSSES

@click.command()
@click.argument('pokemon_names', nargs=-1, required=True)
def planner(pokemon_names):
    """
    Analyzes a Pokémon team for Pokémon Legends: Z-A.

    Provide 1 to 6 Pokémon names as arguments.
    """
    console = Console()

    if not 1 <= len(pokemon_names) <= 6:
        console.print("[bold red]Error: Please provide between 1 and 6 Pokémon names.[/bold red]")
        return

    with console.status("[bold green]Fetching Pokémon data...") as status:
        team_data = []
        valid_pokemon_names = []
        for name in pokemon_names:
            data = fetch_pokemon_data(name)
            if data:
                team_data.append(data)
                valid_pokemon_names.append(name)
            else:
                console.print(f"Could not retrieve data for '{name}'. Skipping.")

        if not team_data:
            console.print("[bold red]Error: Could not retrieve data for any of the Pokémon provided.[/bold red]")
            return

    console.print(
        "\n[bold cyan]================================\n"
        "Legends: Z-A Team Planner\n"
        "================================[/bold cyan]"
    )

    # 1. Availability Check
    console.print("\n[bold]Step 1: Pokémon Availability[/bold]")
    availability = check_availability(valid_pokemon_names)
    for name, is_available in availability.items():
        if is_available:
            console.print(f"- {name.capitalize()}: [green]✔ Confirmed for Legends: Z-A[/green]")
        else:
            console.print(f"- {name.capitalize()}: [yellow]❓ Not yet confirmed for Legends: Z-A[/yellow]")

    # 2. Team Structural Analysis
    console.print("\n[bold]Step 2: Team Defensive Analysis[/bold]")
    coverage = analyze_team_defenses(team_data)
    
    table = Table(title="Team Defensive Coverage")
    table.add_column("Attacking Type", style="cyan")
    table.add_column("Weak", style="red")
    table.add_column("Neutral")
    table.add_column("Resist", style="yellow")
    table.add_column("Immune", style="green")

    for type_name in ALL_TYPES:
        info = coverage[type_name]
        table.add_row(
            type_name.capitalize(),
            str(info['weak']),
            str(info['neutral']),
            str(info['resist']),
            str(info['immune'])
        )
    console.print(table)
    
    # 3. Boss Battle Simulations
    console.print("\n[bold]Step 3: Boss Battle Simulations[/bold]")
    if not KALOS_BOSSES:
        console.print("[yellow]No boss data found. Please add bosses to 'src/data.py'.[/yellow]")
    else:
        analyze_boss_matchups(team_data, KALOS_BOSSES)


if __name__ == "__main__":
    planner()
