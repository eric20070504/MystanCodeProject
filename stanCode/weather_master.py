"""
File: weather_master.py
Name:傅冠鈞
-----------------------
This program implements a console-based application that
asks the user to enter weather data and computes summary
statistics based on the inputs.

The program calculates the average, highest, and lowest
temperatures, as well as the number of cold days. The
output format should match the sample run shown in the
Assignment 2 handout.
"""

QUIT = -100
"""
定義-100為中止程式條件
"""


def main():
	print('stanCode "Weather Master 4.0"!')
	temperature = int(input("temp: "))
	maxtemp = int(0)
	mintemp = int(0)
	average = int(0)
	days = int(1)
	cold = int(0)
	"""
	將要確認的數值都先定義為0，天數除外(必須有第一天)
	"""
	while True:
		if temperature == QUIT:
			print("no data")
			"""
			當輸入-100時，印出"no data"，程式中止
			"""
			break
		else:
			maxtemp = temperature
			"""
			將初始輸入的值，定義為定義為目前最高溫度
			"""
			mintemp = temperature
			"""
			將初始輸入的值，定義為定義為目前最低溫度
			"""
			average = temperature
			"""
			將初始輸入的值，定義為定義為目前平均溫度
			"""
			if temperature < 16:
				cold = cold+1
				"""
				如果初始輸入值<16時，則cold+1
				"""
			while True:
				temperature = int(input("temp: "))
				if temperature == QUIT:
					"""
					當之後的輸入值為-100時，程式中止
					"""
					break
				if temperature > maxtemp:
					maxtemp = temperature
					"""
					如果之後的輸入值>最高溫度，則輸入值為最高溫度
					"""
				if temperature < mintemp:
					mintemp = temperature
					"""
					如果之後的輸入值<最低溫度，則輸入值為最低溫度
					"""
				if temperature < 16:
					cold = cold+1
					"""
					如果之後輸入值有<16者，則cold+1
					"""
				average = average + temperature
				days = +days+1
				"""
				計算溫度加總共多少，並記錄記錄了多少天
				"""
			average = average/days
			"""
			由溫度加總 / 總天數 =平均溫度 
			"""
			print("Highest temperature= " + str(maxtemp))
			print("Lowest temperature= " + str(mintemp))
			print("Average= " + str(average))
			print(str(cold)+" cold day(s)")
			"""
			輸出全部所求數值
			"""
			break





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
