# Investment Portfolio

## Video Demo:  https://youtu.be/MZXWuFO9QUA

## :question: What is the Investment Portfolio

The **Investment Portfolio** is a Python terminal programme that allows users to calculate the value of their investments. The programme is intended to replace spreadsheets for tracking investment portfolios.

For the CS50P Final Project the scope of the **Investment Portfolio** is limited to the terminal. The plan is to iterate over time to add a database for data storage and advanced data analysis and visualisation, and a Graphical User Interface (GUI).

### :package: Features

Users can:

- Add assets (including multiple assets)
- Remove assets
- View a table summary
- View the value of their portfolio
- Export a CSV summary
- Exit the programme

## :dna: Design

The Investment Portfolio project contains the following files:

- `asset.py`
- `portfolio.py`
- `project.py`
- `test_project.py`

### asset.py

A package that contains a class called `Asset`. An `Asset` object represents an asset such as a stock or share. `Assets` are initialised in the `__init__` method with the following attributes:

- `name`: The name of the asset
- `symbol`: The ticker symbol used by `yfinance` for getting the price
- `asset_type`: The type of asset e.g. stock, fund, bond
- `quantity`: The number of units held of the asset

The class includes two property decorators acting as attributes, rather than instance methods. This approach was chosen because the value returned represents an attribute and it's cleaner than calling methods.

- `price`: Uses the `yfinance` library to get the previous closing price for the assets symbol, return it as a float value.
- `value`: Returns the total value of the asset by multiplying `quantity * price`.

These properties are dynamically calculated each time they're accessed, ensuring up-to-date values.

### portfolio.py

A package that contains a class called `Portfolio`. A `Portfolio` object represents the Investment Portfolio, holding all stocks, funds, bonds. The `__init__` method creates an empty list called `assets` to store portfolio holdings. The file imports `Asset` class via `from asset import Asset`.

The class includes two instance methods:

- `add_asset`: Prompts the user for the number of assets to add, then loops through collecting asset details (name, symbol, type, quantity) from user input. Creates `Asset` objects and appends them to the portfolio's `assets` list.
- `remove_asset`: Displays all assets with their index numbers and names, prompts the user to select which asset to remove by index, then uses `pop()` to remove the selected asset from the list.

The class includes one property decorator acting as a attribute:

- `value`: Returns the total portfolio value by iterating over all assets and adding the asset value to the portfolio value.

The property is dynamically calculated each time it's accessed, ensuring up-to-date portfolio valuation.

### project.py

`project.py` orchestrates the Investment Portfolio programme and calls five functions.

#### Libraries

Libraries called in `project.py`

```python
from portfolio import Portfolio
import sys
from pyfiglet import Figlet
from tabulate import tabulate
import csv
from colorama import Fore, Style
```

Libraries not built into Python are defined in the `requirements.txt` file.

`project.py` contains five functions:

- `main()`: The entry point that runs the program. Creates a `Portfolio` object, calls `get_title()` to display the programme banner, and then calls `main_menu(portfolio)` passing the created portfolio object as an parameter to start the interactive menu.
- `get_title()`: Uses the `Figlet` library to generate and display an ASCII art banner of "INVESTMENT PORTFOLIO" using the `term` font style, providing a visual programme title.
- `main_menu(portfolio)`: The core interactive feature that presents users with menu options and handles their selections. Runs in a continuous `while` loop until the user exits, allowing multiple actions per session. Takes a `Portfolio` object as a parameter and offers 6 menu options:
  - `1. Add asset`: Calls `portfolio.add_asset()` to add new investments to the portfolio.
  - `2. Remove asset`: Calls `portfolio.remove_asset()` to remove existing investments.
  - `3. Asset dashboard`: Calls `get_asset_dashboard(portfolio)` to display a tabular view of all assets.
  - `4. Portfolio value`: Displays the total portfolio value in £ (formatted to 2 decimal places, and displayed in green) using the `portfolio.value` property.
  - `5. Export CSV`: Calls `export_csv(portfolio)` to save portfolio data to a CSV file.
  - `6. Exit`: Terminates the programme gracefully using `sys.exit()` with a friendly farewell message.
- `get_asset_dashboard`: Uses the `tabulate` library to display a formatted table of all portfolio assets. Takes a `Portfolio` object as a parameter, iterates through each asset in `portfolio.assets`, and extracts asset attributes (name, symbol, type, quantity, price, value) into rows. Returns a formatted table using the `fancy_grid` style with column headers for easy viewing of portfolio holdings.
- `export_csv`: Creates a CSV file called `portfolio.csv` using Python's `csv.DictWriter`. Takes a `Portfolio` object as a parameter and writes asset data with column headers (name, symbol, type, quantity, price, value). Iterates through each asset in the portfolio, converting asset attributes to dictionary format for CSV rows. Provides confirmation message upon successful export, allowing users to analyze portfolio data in external applications like Excel.

The `main()` function is called with:

```python
if __name__ == "__main__":
    main()
```

### test_project.py

Contains unit tests for `project.py` functions using the `pytest` framework:

- `main_menu()`: Uses monkeypatch to simulate user input "6" (exit option) and verifies the program exits cleanly via `sys.exit()`.
- `get_title()`: Asserts that the function returns the expected title string "INVESTMENT PORTFOLIO".
- `get_asset_dashboard()`: Creates a mock portfolio with test assets, converts it to a table format, and verifies that specific asset names ("Apple") and symbols ("SMT.L") appear in the correct table columns.

The tests use `pytest` fixtures and mocking to isolate functionality and simulate user interactions without requiring actual user input.

## :key: Opportunities

Ideas to improve the **Investment Portfolio** in the future.

- :white_check_mark: Improve input validation including regex
- Improve error checking
- Add SQL database for data retention
- Add Data analysis
- Add Data visualisation
- Build a Graphical User Interface
- Build a Web App
