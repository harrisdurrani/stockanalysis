from codebase import code
from sklearn.linear_model import LogisticRegression
import statistics

class Analysis:

	def bollinger_band_analysis(self, stock_name:str):
		candle_avgs = []
		#typical_price = []
		cb = code.Codebase()
		x = cb.get_access_token("authorization_code", cb.open_connection())
		stock_data = cb.get_price_history(x["access_token"], stock_name)


		std_deviations = 2
		upper_band = None
		lower_band = None
		

		for candle in stock_data.get("candles"):
			candle_avgs.append(((int(candle["high"]) + int(candle["low"])) / 2))
			#typical_price.append(((int(candle["high"]) + int(candle["low"]) + int(candle["close"])) / 3))

		# typical_plus_smoothing = (i * float(smoothing) for i in typical_price)

		moving_avg = (sum(candle_avgs) / len(candle_avgs))
		
		# for i in typical_plus_smoothing:
		upper_band = moving_avg + (std_deviations * statistics.stdev(candle_avgs))
		lower_band = moving_avg - (std_deviations * statistics.stdev(candle_avgs))

		print("#" * 10)
		print(upper_band)
		print(moving_avg)
		
		print(lower_band)
		
		print("#" * 10)
		

		# upper_band = (sum(avg_highs_lows) / len(avg_highs_lows)) * (i * float(smoothing) for i in typical_price) + (std_deviations * statistics.stdev(typical_price))

		# lower_band = (sum(avg_highs_lows) / len(avg_highs_lows)) * (i * smoothing for i in typical_price) - (std_deviations * statistics.stdev(typical_price))


		# print(upper_band)
		# print(lower_band)



analysis = Analysis()

print(analysis.bollinger_band_analysis("KO"))


