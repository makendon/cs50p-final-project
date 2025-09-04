import yfinance as yf


class Asset:
    def __init__(self, name, symbol, asset_type, quantity):
        self.name = name
        self.symbol = symbol
        self.asset_type = asset_type
        self.quantity = quantity

    @property
    def price(self):
        info = yf.Ticker(self.symbol)
        return float(info.info.get("previousClose"))

    @property
    def value(self):
        return (self.quantity * self.price) / 100
