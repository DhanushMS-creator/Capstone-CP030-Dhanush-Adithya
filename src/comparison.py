"""Single-run and vaccination-scenario comparison workflows."""
from grid import INFECTED, RECOVERED
from settings import read_int, create_sim

def run_single(settings):
    vaccination = read_int("Vaccination percentage (0-100)", 0, 0, 100)
    show = input("Print grid snapshots? (y/n): ").strip().lower() == "y"
    selected_days = None
    if show:
        raw = input(
            f"Enter day numbers separated by commas (0-{settings['days']}), "
            "or press Enter for every day: "
        ).strip()
        if raw:
            try:
                selected_days = {int(value.strip()) for value in raw.split(",")}
                selected_days = {day for day in selected_days
                                 if 0 <= day <= settings["days"]}
            except ValueError:
                print("Invalid day list; grid will be shown every day.")
                selected_days = None
    simulation = create_sim(settings, vaccination)
    simulation.run(show_grid=show, selected_days=selected_days)

def compare_scenarios(settings):
    print("\nSCENARIO COMPARISON")
    print("Both scenarios use the same grid size, disease settings and random seed.")
    print("\n--- SCENARIO A: 0% VACCINATION ---")
    result_a = create_sim(settings, 0).run()
    print("\n--- SCENARIO B: 50% VACCINATION ---")
    result_b = create_sim(settings, 50).run()

    print("\nCOMPARISON SUMMARY")
    print("-" * 58)
    print(f"{'Measure':<28}{'0% vaccinated':>15}{'50% vaccinated':>15}")
    print("-" * 58)
    print(f"{'Peak infected':<28}{result_a['peak_infected']:>15}"
          f"{result_b['peak_infected']:>15}")
    print(f"{'Peak day':<28}{result_a['peak_day']:>15}"
          f"{result_b['peak_day']:>15}")
    print(f"{'Infected on final day':<28}"
          f"{result_a['final'][INFECTED]:>15}"
          f"{result_b['final'][INFECTED]:>15}")
    print(f"{'Recovered on final day':<28}"
          f"{result_a['final'][RECOVERED]:>15}"
          f"{result_b['final'][RECOVERED]:>15}")
    print("\nNote: This is an educational model, not a real-world disease forecast.")
