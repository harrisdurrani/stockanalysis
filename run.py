from analysis import Analysis


if __name__ == "__main__":
    stocks = ["MSFT", "AMC", "ABBV", "ABT", "NVDA", "AAPL"]
    analysis = Analysis()
    # stock = analysis.convert_to_df("KO")
    # print(stock)

    # plt.figure(figsize=(16,8))
    # plt.plot(stock['close'], label = 'Close price history')
    # plt.show()

    for i in stocks:

        print(analysis.bollinger_band_analysis(i)+"\n")
