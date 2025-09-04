from portfolio import Portfolio
import sys
from pyfiglet import Figlet
from tabulate import tabulate
import csv
from colorama import Fore, Style


def main():
    print()
    print("👋 Hey, welcome to your")
    print(get_title())
    portfolio = Portfolio()
    main_menu(portfolio)


def get_title():
    figlet = Figlet()
    figlet.setFont(font="term")
    text = "INVESTMENT PORTFOLIO"
    art = figlet.renderText(text)
    return art


def main_menu(portfolio):
    """Main menu for the terminal application"""
    while True:
        print()
        print(
            "Menu\n1. Add asset\n2. Remove asset\n3. Asset dashboard\n4. Portfolio value\n5. Export CSV\n6. Exit"
        )
        try:
            action = int(input("Select an action (1-6): "))
            print()
        except ValueError:
            print("Please enter an integer 1-6.")
            continue
        if action == 1:
            print("Add asset: ")
            portfolio.add_asset()
        elif action == 2:
            print("Remove asset:")
            portfolio.remove_asset()
        elif action == 3:
            print("Asset dashboard:")
            get_asset_dashboard(portfolio)
        elif action == 4:
            print(f"Portfolio value: {Fore.GREEN}£{portfolio.value:.2f}{Style.RESET_ALL}\n")
        elif action == 5:
            export_csv(portfolio)
        elif action == 6:
            sys.exit("👋 Keep investing! 📈")
        else:
            print("Invalid action. Please enter an integer 1-6.")


def get_asset_dashboard(portfolio):
    """Table summary for each asset"""
    table = []
    for asset in portfolio.assets:
        table.append(
            [
                asset.name,
                asset.symbol,
                asset.asset_type,
                asset.quantity,
                asset.price,
                asset.value,
            ]
        )
    headers = ["Name", "Symbol", "Asset type", "Quantity", "Price (p)", "Value (£)"]
    print(tabulate(table, headers=headers, numalign="right", tablefmt="fancy_grid"))
    return table


def export_csv(portfolio):
    """CSV summary listing each asset as a row"""
    try:
        print("Exporting to CSV...")
        export = "portfolio.csv"
        with open(export, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Name",
                    "Symbol",
                    "Asset type",
                    "Quantity",
                    "Price (p)",
                    "Value (£)",
                ],
            )
            writer.writeheader()
            for asset in portfolio.assets:
                writer.writerow(
                    {
                        "Name": asset.name,
                        "Symbol": asset.symbol,
                        "Asset type": asset.asset_type,
                        "Quantity": asset.quantity,
                        "Price (p)": asset.price,
                        "Value (£)": asset.value,
                    }
                )

        print(f"✅ Portfolio successfully exported to {export}")

    except PermissionError:
        print("❌ Error: Cannot write to portfolio.csv")


if __name__ == "__main__":
    main()
