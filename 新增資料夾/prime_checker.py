"""
File: prime_checker.py
Name:傅冠鈞
-----------------------
This program asks the user to enter a number and checks whether
the number is a prime number.

When the program starts, it first prints a welcome message to
the console. It then repeatedly prompts the user to enter an
integer greater than 1 and determines whether the number is prime.

The program will stop running when the user enters the EXIT value.
"""

QUIT = -100
"""
定義-100為中止程式之輸入條件
"""


def main():
	print("Welcome to the prime checker")
	a = int(0)
	"""
	一開始定義0個因數
	"""
	while True:
		n = int(input("n: "))
		"""
		輸入要詢問的數字
		"""
		if n == QUIT:
			print("Have a good one!")
			"""
			當輸入-100時，程式中止
			"""
			break
		for i in range(n):
			if n % (i + 1) == 0:
				a = a + 1
				"""
				確認總共有幾個因數
				"""
		if a == 2:
			print(str(n) + " is a prime number.")
			"""
			如果因數只有自己跟1，共2個因數，則為質數
			"""
		else:
			print(str(n) + " is not a prime number.")
			"""
			如果因數有除了自己跟1之外的其他數字，共超過2個因數，則為合數
			"""
		a = 0
		"""
		在開始新的迴圈時，因數總數都要重新定義為0
		"""



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
