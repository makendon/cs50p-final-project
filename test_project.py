from portfolio import Portfolio
from asset import Asset
import pytest
from project import main_menu, get_title, get_asset_dashboard


# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
def test_menu_6(monkeypatch):
    portfolio = Portfolio()
    monkeypatch.setattr("builtins.input", lambda _: "6")
    with pytest.raises(SystemExit):
        main_menu(portfolio)


def test_title():
    title = get_title()
    assert title == "INVESTMENT PORTFOLIO\n"


def test_dashboard():
    portfolio = Portfolio()
    portfolio.assets = [
        Asset("Apple", "AAPL", "Share", 1),
        Asset("SMT", "SMT.L", "Trust", 1),
    ]
    table = get_asset_dashboard(portfolio)
    names = [asset[0] for asset in table]
    symbols = [asset[1] for asset in table]
    assert "Apple" in names
    assert "SMT.L" in symbols
    assert len(table) == 2
