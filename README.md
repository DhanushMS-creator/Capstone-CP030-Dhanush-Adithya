# OutbreakSim: Grid-Based Epidemic Spread Simulation Model

**Problem ID:** CP_030

## Team Members

1. **Name:** Dhanush Kumar M  
   **USN:** 1AT24CS053

2. **Name:** Adithya S  
   **USN:** 1AT25CS400

## How to Run the Program

### Prerequisites

- Python 3.10 or above installed on the system.
- IntelliJ IDEA or any Python-supported code editor.
- No additional external Python libraries are required.

### Steps

1. Clone or download this repository.
2. Extract the project folder.
3. Open the project folder in IntelliJ IDEA.
4. Open the terminal in the project directory.
5. Run the following command:

```bash
python3 src/main.py
```

6. The main menu of OutbreakSim will appear.
7. Select the required option and follow the instructions displayed on the screen.

**Note:** On Windows, use:

```bash
python src/main.py
```

## Features Implemented

1. **Grid-Based Population Model:** Represents the population using a two-dimensional grid in which each cell represents an individual.

2. **Infection Spread:** Simulates the spread of infection between neighbouring individuals using a specified infection probability.

3. **Recovery Mechanism:** Automatically changes infected individuals to the recovered state after a fixed recovery period.

4. **Daily Population Statistics:** Displays the daily counts of susceptible, infected, recovered and vaccinated individuals.

5. **Vaccination Simulation:** Allows users to specify the vaccination percentage and observe its effect on disease transmission.

6. **Scenario Comparison:** Compares epidemic outcomes under 0% and 50% vaccination scenarios.

7. **Grid Visualization:** Displays the population grid at selected simulation stages using different symbols for each population state.

8. **Peak Infection Analysis:** Identifies the peak infection day and the maximum number of infected individuals.

9. **Interactive Menu:** Provides options to run simulations, modify settings, compare scenarios and view project information.

## Sample Run

**Input:**

```text
Enter your choice: 1

Vaccination percentage (0-100) [0]: 40

Print grid snapshots? (y/n): y
```

**Output:**

```text
CP-030 OUTBREAKSIM
GRID-BASED EPIDEMIC SPREAD SIMULATOR

Daily Population Counts

Day    Susceptible    Infected    Recovered    Vaccinated
---------------------------------------------------------
0          57            3           0             40
1          56            4           0             40
2          55            5           0             40
3          53            7           0             40
4          50           10           0             40
5          48            9           3             40
6          46           10           4             40
7          45           10           5             40
8          43           10           7             40
9          43            7          10             40
10         43            5          12             40
```

*Note: The sample output is illustrative of one simulation run. Actual results may vary because infection spread involves probability and randomness.*

## Project Structure

```text
CP-030_OutbreakSim/
│
├── src/
│   ├── main.py
│   ├── simulation.py
│   ├── grid.py
│   ├── settings.py
│   ├── comparison.py
│   └── __init__.py
│
├── README.md
└── .gitignore
```

## Conclusion

OutbreakSim demonstrates how an infectious disease can spread through a population using a grid-based simulation model. It helps illustrate the importance of vaccination in controlling disease transmission by comparing different vaccination scenarios. The project uses Python programming concepts such as two-dimensional arrays, probability, loops, functions and modular programming to simulate epidemic behaviour.