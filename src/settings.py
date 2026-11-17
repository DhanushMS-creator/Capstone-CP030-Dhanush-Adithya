"""Default settings, input validation, and settings menu functions."""
from simulation import OutbreakSimulation

DEFAULT_SETTINGS = {
    "size": 10,
    "days": 20,
    "probability": 0.25,
    "recovery_days": 5,
    "initial_infected": 3,
    "seed": 42,
}

def read_int(prompt, current, minimum, maximum):
    while True:
        raw = input(f"{prompt} [{current}]: ").strip()
        if not raw:
            return current
        try:
            value = int(raw)
            if minimum <= value <= maximum:
                return value
        except ValueError:
            pass
        print(f"Enter a whole number from {minimum} to {maximum}.")

def read_float(prompt, current, minimum, maximum):
    while True:
        raw = input(f"{prompt} [{current}]: ").strip()
        if not raw:
            return current
        try:
            value = float(raw)
            if minimum <= value <= maximum:
                return value
        except ValueError:
            pass
        print(f"Enter a number from {minimum} to {maximum}.")

def show_settings(settings):
    print("\nCURRENT SIMULATION SETTINGS")
    print(f"Grid size             : {settings['size']} x {settings['size']}")
    print(f"Simulation days       : {settings['days']}")
    print(f"Infection probability : {settings['probability']:.2f}")
    print(f"Recovery after        : {settings['recovery_days']} days")
    print(f"Initial infected      : {settings['initial_infected']}")
    print(f"Random seed           : {settings['seed']}")

def update_settings(settings):
    print("\nUPDATE SIMULATION SETTINGS (press Enter to keep current value)")
    settings["size"] = read_int("Grid width/height (3-30)", settings["size"], 3, 30)
    settings["days"] = read_int("Number of days (1-100)", settings["days"], 1, 100)
    settings["probability"] = read_float(
        "Infection probability (0-1)", settings["probability"], 0, 1)
    settings["recovery_days"] = read_int(
        "Days until recovery (1-30)", settings["recovery_days"], 1, 30)
    settings["initial_infected"] = read_int(
        "Initially infected people", settings["initial_infected"], 1,
        settings["size"] * settings["size"])
    settings["seed"] = read_int("Random seed", settings["seed"], 0, 999999)
    print("Settings updated.")

def create_sim(settings, vaccination_percent):
    return OutbreakSimulation(
        size=settings["size"],
        days=settings["days"],
        infection_probability=settings["probability"],
        recovery_days=settings["recovery_days"],
        initial_infected=settings["initial_infected"],
        vaccination_percent=vaccination_percent,
        seed=settings["seed"],
    )
