"""Grid states and grid-related helper functions for OutbreakSim."""
SUSCEPTIBLE = "S"
INFECTED = "I"
RECOVERED = "R"
VACCINATED = "V"

SYMBOLS = {
    SUSCEPTIBLE: "S",
    INFECTED: "I",
    RECOVERED: "R",
    VACCINATED: "V",
}

def empty_grid(size):
    """Create a size x size grid of susceptible cells."""
    return [[SUSCEPTIBLE for _ in range(size)] for _ in range(size)]

def count_states(grid):
    """Return counts for all four population states."""
    counts = {SUSCEPTIBLE: 0, INFECTED: 0,
              RECOVERED: 0, VACCINATED: 0}
    for row in grid:
        for state in row:
            counts[state] += 1
    return counts

def neighbours(size, row, col):
    """Yield valid four-directional neighbour coordinates."""
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size:
            yield nr, nc

def print_grid(grid, day):
    """Print a text snapshot of the population grid."""
    size = len(grid)
    print(f"\nGRID - DAY {day}  (S=Susceptible, I=Infected, "
          "R=Recovered, V=Vaccinated)")
    print("   " + " ".join(f"{col:2}" for col in range(size)))
    for row_index, row in enumerate(grid):
        print(f"{row_index:2} " + "  ".join(SYMBOLS[state] for state in row))
