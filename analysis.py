from codebase import code
from sklearn.linear_model import LogisticRegression
import pandas as pd
import statistics

class Analysis:

	def bollinger_band_analysis(self, stock_name:str):
		candle_avgs = []
		cb = code.Codebase()
		auth_token = cb.get_access_token("authorization_code", cb.open_connection())
		stock_data = cb.get_price_history(auth_token["access_token"], stock_name)

		std_deviations = 2
		upper_band = None
		lower_band = None

		for candle in stock_data.get("candles"):
			candle_avgs.append(((int(candle["high"]) + int(candle["low"])) / 2))

		moving_avg = (sum(candle_avgs) / len(candle_avgs))
		
		upper_band = moving_avg + (std_deviations * statistics.stdev(candle_avgs))
		lower_band = moving_avg - (std_deviations * statistics.stdev(candle_avgs))


		return f"stock name: {stock_name},\n upper band: {upper_band},\n moving average: {moving_avg},\n lower band: {lower_band}"

		# print("#" * 10)
		# print(stock_name)
		# print(upper_band)
		# print(moving_avg)
		
		# print(lower_band)
		
		# print("#" * 10)
		
	def convert_to_df(self, stock_name:str):
		cb = code.Codebase()
		auth_token = cb.get_access_token("authorization_code", cb.open_connection())
		stock_data = cb.get_price_history(auth_token["access_token"], stock_name)

		points = stock_data['candles']

		df = pd.json_normalize(points)

		return df

	def regression_analysis(self, stock_name:str):
		pass




if __name__ == "__main__":
	stocks = ["KO"]
	analysis = Analysis()
	print(analysis.convert_to_df("KO"))

	# for i in stocks:

	# 	print(analysis.bollinger_band_analysis(i))


