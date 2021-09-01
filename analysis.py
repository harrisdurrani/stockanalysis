from codebase import code
from sklearn.linear_model import LogisticRegression
import pandas as pd
import statistics
import matplotlib.pyplot as plt

class Analysis:

    def bollinger_band_analysis(self, stock_name:str):
        ''' runs analysis on the bollinger bands of stock data, checks within 2 standard deviations'''
        candle_avgs = []
        cb = code.Codebase() #import the codebase
        auth_token = cb.get_access_token() #get auth code
        stock_data = cb.get_price_history(auth_token["access_token"], stock_name) #get stock history

        std_deviations = 2
        upper_band = None
        lower_band = None

        for candle in stock_data.get("candles"):
            candle_avgs.append(((int(candle["high"]) + int(candle["low"])) / 2))

        moving_avg = (sum(candle_avgs) / len(candle_avgs)) #calculate the moving average between the candles
        
        upper_band = moving_avg + (std_deviations * statistics.stdev(candle_avgs)) #calculate the upper band
        lower_band = moving_avg - (std_deviations * statistics.stdev(candle_avgs)) #calculate the lower band


        return f"stock name: {stock_name},\n upper band: {upper_band},\n moving average: {moving_avg},\n lower band: {lower_band}"

        # print("#" * 10)
        # print(stock_name)
        # print(upper_band)
        # print(moving_avg)
        
        # print(lower_band)
        
        # print("#" * 10)
        
    def convert_to_df(self, stock_name:str):
        cb = code.Codebase() #call the codebase class
        auth_token = cb.get_access_token("authorization_code", cb.get_code()) #get auth token
        stock_data = cb.get_price_history(auth_token["access_token"], stock_name) #get stock data and its history

        points = stock_data['candles']

        df = pd.json_normalize(points) #converts the json stock data to a pandas df

        df['datetime'] = pd.to_datetime(df['datetime'], unit = 'ms') #converts date time column from epoch to human readable time
        return df

    def regression_analysis(self, stock_name:str):
        pass




if __name__ == "__main__":
    stocks = ["KO"]
    analysis = Analysis()
    # stock = analysis.convert_to_df("KO")

    # plt.figure(figsize=(16,8))
    # plt.plot(stock['close'], label = 'Close price history')
    # plt.show()

    for i in stocks:

    	print(analysis.bollinger_band_analysis(i))


