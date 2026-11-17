"""Core epidemic simulation engine."""
import random
from copy import deepcopy

from grid import (
    SUSCEPTIBLE, INFECTED, RECOVERED, VACCINATED,
    empty_grid, count_states, neighbours, print_grid,
)

class OutbreakSimulation:
    def __init__(self, size=10, days=20, infection_probability=0.25,
                 recovery_days=5, initial_infected=3, vaccination_percent=0,
                 seed=42):
        self.size = size
        self.days = days
        self.infection_probability = infection_probability
        self.recovery_days = recovery_days
        self.initial_infected = initial_infected
        self.vaccination_percent = vaccination_percent
        self.seed = seed
        self.grid = []
        self.infection_age = {}
        self.history = []

    def setup(self):
        rng = random.Random(self.seed)
        total = self.size * self.size
        cells = [(row, col) for row in range(self.size)
                 for col in range(self.size)]
        rng.shuffle(cells)

        vaccinated_count = round(total * self.vaccination_percent / 100)
        vaccinated = set(cells[:vaccinated_count])
        remaining = [position for position in cells if position not in vaccinated]
        infected_count = min(self.initial_infected, len(remaining))
        infected_positions = set(remaining[:infected_count])

        self.grid = empty_grid(self.size)
        self.infection_age = {}

        for row, col in vaccinated:
            self.grid[row][col] = VACCINATED
        for row, col in infected_positions:
            self.grid[row][col] = INFECTED
            self.infection_age[(row, col)] = 0

        self.history = [self.count_states()]

    def count_states(self):
        return count_states(self.grid)

    def step(self, rng):
        new_grid = deepcopy(self.grid)
        new_age = dict(self.infection_age)
        new_infections = []

        # Determine new infections from the current day's grid.
        for (row, col), age in self.infection_age.items():
            for nr, nc in neighbours(self.size, row, col):
                if self.grid[nr][nc] == SUSCEPTIBLE:
                    if rng.random() < self.infection_probability:
                        new_infections.append((nr, nc))

        # Age infected cells and recover them when their duration ends.
        for (row, col), age in list(self.infection_age.items()):
            next_age = age + 1
            if next_age >= self.recovery_days:
                new_grid[row][col] = RECOVERED
                new_age.pop((row, col), None)
            else:
                new_age[(row, col)] = next_age

        # Apply new infections after all current infections are checked.
        for row, col in set(new_infections):
            if self.grid[row][col] == SUSCEPTIBLE:
                new_grid[row][col] = INFECTED
                new_age[(row, col)] = 0

        self.grid = new_grid
        self.infection_age = new_age
        self.history.append(self.count_states())

    def run(self, show_grid=False, selected_days=None):
        self.setup()
        rng = random.Random(self.seed + 1000)
        print("\nDaily population counts")
        print("-" * 68)
        print(f"{'Day':<6}{'Susceptible':>14}{'Infected':>12}"
              f"{'Recovered':>12}{'Vaccinated':>14}")
        print("-" * 68)
        self.print_counts(0, self.history[0])
        if show_grid and (selected_days is None or 0 in selected_days):
            print_grid(self.grid, 0)

        for day in range(1, self.days + 1):
            self.step(rng)
            counts = self.history[-1]
            self.print_counts(day, counts)
            if show_grid and (selected_days is None or day in selected_days):
                print_grid(self.grid, day)

        peak_day, peak_count = max(
            enumerate([item[INFECTED] for item in self.history]),
            key=lambda item: item[1]
        )
        final = self.history[-1]
        print("-" * 68)
        print(f"Peak infections: {peak_count} on day {peak_day}")
        print(f"Final infected: {final[INFECTED]}")
        print(f"Final recovered: {final[RECOVERED]}")
        return {
            "history": self.history,
            "peak_day": peak_day,
            "peak_infected": peak_count,
            "final": final,
        }

    @staticmethod
    def print_counts(day, counts):
        print(f"{day:<6}{counts[SUSCEPTIBLE]:>14}{counts[INFECTED]:>12}"
              f"{counts[RECOVERED]:>12}{counts[VACCINATED]:>14}")
