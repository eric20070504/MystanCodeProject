"""
File: complement.py
Name:傅冠鈞
----------------------------
This program uses string manipulation to solve a real-world
problem: finding the complementary strand of a DNA sequence.

The program provides different DNA sequences as Python strings.
These strings are case-sensitive, and your task is to generate
and output the correct complementary strand for each sequence.
"""


def main():
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):

    result = ""
    if dna == "":
        return "DNA strand is missing"
        """輸入空字串則回覆"""
    else:
        for i in range(len(dna)):
            ch = dna[i]
            if ch == "A":
                ch = "T"
                result = result + ch
                """
                如果本來的鹼基為A，則對應為T
                """
            elif ch == "T":
                ch = "A"
                result = result + ch
                """
                如果本來的鹼基為T，則對應為A
                """
            elif ch == "C":
                ch = "G"
                result = result + ch
                """
                如果本來的鹼基為C，則對應為G
                """
            else:
                ch = "C"
                result = result + ch
                """
                如果本來的鹼基為G，則對應為C
                """
        return result




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
