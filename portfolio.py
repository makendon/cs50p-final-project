from asset import Asset


class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self):
        while True:
            try:
                n = int(input("How many assets do you want to add? "))
                break
            except ValueError:
                print("Please enter a postive integer.")
        for _ in range(n):
            name = input("Name: ").upper().strip()
            symbol = input("Symbol: ").upper().strip()
            asset_type = input("Asset Type: ").upper().strip()
            quantity = float(input("Quantity: "))
            self.assets.append(Asset(name, symbol, asset_type, quantity))
            print(f"Added asset: {name}\n")

    def remove_asset(self):
        for index, asset in enumerate(self.assets, 1):
            print(f"{index}: {asset.name}")
        n = int((input("Select an asset number to remove? "))) - 1
        removed_asset = self.assets.pop(n)
        print(f"Removed asset: {removed_asset.name}\n")

    @property
    def value(self):
        self.total = 0
        for asset in self.assets:
            asset.price
            self.total += asset.value
        return self.total
