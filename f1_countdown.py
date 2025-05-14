import sys
from datetime import datetime, timezone, timedelta
from dateutil import parser

from rich.console import Console
from rich.table import Table
from rich.align import Align

# --- Static 2025 F1 Calendar ---
RACE_CALENDAR =[
    {"raceName": "Australian Grand Prix", "Circuit": {"circuitName": "Albert Park Circuit"}, "date": "2025-03-16", "time": "05:00:00Z"},
    {"raceName": "Chinese Grand Prix", "Circuit": {"circuitName": "Shanghai International Circuit"}, "date": "2025-03-23", "time": "07:00:00Z"},
    {"raceName": "Japanese Grand Prix", "Circuit": {"circuitName": "Suzuka International Racing Course"}, "date": "2025-04-06", "time": "05:00:00Z"},
    {"raceName": "Bahrain Grand Prix", "Circuit": {"circuitName": "Bahrain International Circuit"}, "date": "2025-04-13", "time": "15:00:00Z"},
    {"raceName": "Saudi Arabian Grand Prix", "Circuit": {"circuitName": "Jeddah Corniche Circuit"}, "date": "2025-04-20", "time": "18:00:00Z"},
    {"raceName": "Miami Grand Prix", "Circuit": {"circuitName": "Miami International Autodrome"}, "date": "2025-05-04", "time": "19:30:00Z"},
    {"raceName": "Emilia Romagna Grand Prix", "Circuit": {"circuitName": "Autodromo Enzo e Dino Ferrari"}, "date": "2025-05-18", "time": "13:00:00Z"},
    {"raceName": "Monaco Grand Prix", "Circuit": {"circuitName": "Circuit de Monaco"}, "date": "2025-05-25", "time": "14:00:00Z"},
    {"raceName": "Spanish Grand Prix", "Circuit": {"circuitName": "Circuit de Barcelona-Catalunya"}, "date": "2025-06-01", "time": "14:00:00Z"},
    {"raceName": "Canadian Grand Prix", "Circuit": {"circuitName": "Circuit Gilles Villeneuve"}, "date": "2025-06-15", "time": "18:00:00Z"},
    {"raceName": "Austrian Grand Prix", "Circuit": {"circuitName": "Red Bull Ring"}, "date": "2025-06-29", "time": "13:00:00Z"},
    {"raceName": "British Grand Prix", "Circuit": {"circuitName": "Silverstone Circuit"}, "date": "2025-07-06", "time": "14:00:00Z"},
    {"raceName": "Belgian Grand Prix", "Circuit": {"circuitName": "Circuit de Spa-Francorchamps"}, "date": "2025-07-27", "time": "14:00:00Z"},
    {"raceName": "Hungarian Grand Prix", "Circuit": {"circuitName": "Hungaroring"}, "date": "2025-08-03", "time": "13:00:00Z"},
    {"raceName": "Dutch Grand Prix", "Circuit": {"circuitName": "Circuit Zandvoort"}, "date": "2025-08-31", "time": "13:00:00Z"},
    {"raceName": "Italian Grand Prix", "Circuit": {"circuitName": "Monza Circuit"}, "date": "2025-09-07", "time": "14:00:00Z"},
    {"raceName": "Azerbaijan Grand Prix", "Circuit": {"circuitName": "Baku City Circuit"}, "date": "2025-09-21", "time": "12:00:00Z"},
    {"raceName": "Singapore Grand Prix", "Circuit": {"circuitName": "Marina Bay Street Circuit"}, "date": "2025-10-05", "time": "13:00:00Z"},
    {"raceName": "United States Grand Prix", "Circuit": {"circuitName": "Circuit of the Americas"}, "date": "2025-10-19", "time": "19:00:00Z"},
    {"raceName": "Mexico City Grand Prix", "Circuit": {"circuitName": "Autódromo Hermanos Rodríguez"}, "date": "2025-10-26", "time": "18:00:00Z"},
    {"raceName": "São Paulo Grand Prix", "Circuit": {"circuitName": "Interlagos Circuit"}, "date": "2025-11-09", "time": "17:00:00Z"},
    {"raceName": "Las Vegas Grand Prix", "Circuit": {"circuitName": "Las Vegas Strip Circuit"}, "date": "2025-11-22", "time": "01:00:00Z"},
    {"raceName": "Qatar Grand Prix", "Circuit": {"circuitName": "Lusail International Circuit"}, "date": "2025-11-30", "time": "14:00:00Z"},
    {"raceName": "Abu Dhabi Grand Prix", "Circuit": {"circuitName": "Yas Marina Circuit"}, "date": "2025-12-07", "time": "14:00:00Z"},
]

def fetch_schedule():
    """Returns the static calendar list"""
    return RACE_CALENDAR


def get_next_race(races):
    now = datetime.now(timezone.utc) 
    for race in races:
        # Parse date and time into a UTC datetime
        race_dt = parser.isoparse(f"{race['date']}T{race['time']}")
        if race_dt > now:
            return race, race_dt
    return None, None


def format_countdown(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds 


def display_countdown(race, race_dt):
    console = Console()
    delta = race_dt - datetime.now(timezone.utc)
    days, hours, minutes, seconds = format_countdown(delta)

    table = Table(title="Next F1 Grand Prix Countdown", show_edge=False)
    table.add_column("Event", justify="left")
    table.add_column("Time Remaining", justify="right")

    race_name = f"{race['raceName']} ({race['Circuit']['circuitName']})"
    countdown_str = f"{days}d {hours}h {minutes}m {seconds}s"

    table.add_row(race_name, f"[bold green]{countdown_str}[/]")

    data_str = race_dt.strftime('%Y-%m-%d %H:%M UTC')
    table.caption = f"Scheduled on: {data_str}"

    console.print(Align.center(table)) 


def main():
    races = fetch_schedule()
    next_race, race_dt = get_next_race(races)
    if not next_race:
        Console().print("[bold yellow]No upcoming races found for 2025.[/]")
        sys.exit(0)
    display_countdown(next_race, race_dt)
    
    
if __name__ == "__main__":
    main()