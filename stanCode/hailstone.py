"""
File: hailstone.py
Name:傅冠鈞
-----------------------
This program implements a console-based simulation of the
Hailstone sequence, as defined by Douglas Hofstadter.

Starting from a user-provided number, the program repeatedly
applies the Hailstone rules and prints each step. The output
format should match the sample run shown in the Assignment 2 handout.
"""


def main():
    print("This program computes Hailstone sequences")
    num = int(input("Please enter a number: "))
    """
    input數字
    """
    step = int(0)
    """
    一開始0步驟
    """
    while num != 1:
        """
        當num=1時結束流程
        """
        if num % 2 == 1:
            print(str(int(num))+' is odd, so I make 3n+1: '+str(int(num*3 + 1)))
            num = num*3 + 1
            step = step + 1
            """
            if num為奇數，則將num*3 + 1，並將step(步驟)+1
            """
        else:
            print(str(int(num))+' is even, so I take half: '+str(int(num / 2)))
            step = step + 1
            num = num / 2
            """
            if num為偶數，則將num / 2，並將step(步驟)+1
            """
    print("It took "+str(step)+" steps to reach 1.")
    """
    列出花幾步驟才回到1
    """






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
