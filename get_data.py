#gets data of multiple stocks from alphavantage

def fetch_multistock_daily(self, symbols:list):
        results = {}
        for symbol in symbols:
            request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={self.api_key}&datatype=csv"
            df = read_csv(request_url)
            results[symbol] = df.to_dict("records")
            # TODO: consider implementing some kind of validation or re-attempt in case one or more requests goes bad
        return results #> {"MSFT": [], "GOOGL": [], "NFLX": []}


def test_fetch_multistock_daily():
    alpha = AlphavantageService()

    # with valid symbol, returns the data:
    result = alpha.fetch_multistock_daily(symbols=["IBM", "NFLX"])
    assert isinstance(result, dict)
    assert list(result.keys()) == ["IBM", "NFLX"]

    data = result["IBM"]
    assert isinstance(data, list)
    assert len(data) >= 100
    assert list(data[0].keys()) == ['timestamp', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']

    data = result["NFLX"]
    assert isinstance(data, list)
    assert len(data) >= 100
    assert list(data[0].keys()) == ['timestamp', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']
