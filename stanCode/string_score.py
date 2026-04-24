"""
File: string_score.py
Name:傅冠鈞
------------------------------
This program calculates a score for a given string based on
the types of characters it contains.

Digits are worth 1 point, uppercase letters are worth 2 points,
and lowercase letters are worth 3 points. The score() function
iterates through each character in the string, adds up the
corresponding points, and prints the final total score.
"""


def main():
    """
    TODO:
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    a = int(0)
    for i in range(len(string)):
        if string[i].isdigit():
            a = a+1
            """
            如果是數字，則分數+1
            """
        if string[i].islower():
            a = a+3
            """
            如果是小寫字母，則分數+3
            """
        if string[i].isupper():
            a = a+2
            """
            如果是大寫字母，則+2
            """
    return print(a)



if __name__ == '__main__':
    main()