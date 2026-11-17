"""Entry point and interactive menu for CP-030 OutbreakSim."""
from settings import DEFAULT_SETTINGS, show_settings, update_settings
from comparison import run_single, compare_scenarios

def main():
    settings = DEFAULT_SETTINGS.copy()

    while True:
        print("\n" + "=" * 58)
        print("              CP-030 OUTBREAKSIM")
        print("       GRID-BASED EPIDEMIC SPREAD SIMULATOR")
        print("=" * 58)
        print("1. Run a single outbreak simulation")
        print("2. Compare 0% and 50% vaccination scenarios")
        print("3. Change simulation settings")
        print("4. View current settings")
        print("5. About this project")
        print("6. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            run_single(settings)
        elif choice == "2":
            compare_scenarios(settings)
        elif choice == "3":
            update_settings(settings)
        elif choice == "4":
            show_settings(settings)
        elif choice == "5":
            print("\nOutbreakSim models a population using a 2D grid.")
            print("S = Susceptible | I = Infected | R = Recovered | V = Vaccinated")
            print("Infected cells can infect their four direct neighbours.")
            print("Infection is probabilistic; infected people recover after")
            print("the configured number of days. Vaccinated cells are protected.")
            print("\nThis is a simplified educational simulation only.")
        elif choice == "6":
            print("\nThank you for using CP-030 OutbreakSim. Stay safe!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")

        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
