"""
File: caesar.py
Name:傅冠鈞
------------------------------
This program demonstrates the idea of the Caesar cipher.

The user is first asked to enter a number that determines
how much the alphabet should be shifted to form a cipher
table. After that, any input string will be encrypted
using the generated cipher.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    old_s = ALPHABET
    sec_num = int(input("Secret number: "))
    """
    輸入要移動幾個字母
    """
    ans = create_new(old_s, sec_num)
    c_string = input("Whats the cipher string: ")
    """
    輸入新的密碼
    """
    ps = decipher(ans, c_string, old_s)
    print(ps)


def create_new(old_s, sec_num):
    ans = ''
    ans = ans + old_s[len(old_s)-sec_num:]
    """
    把留下的部分往前移
    """
    ans = ans + old_s[0:len(old_s)-sec_num]
    """
    把剪下的部分往後貼
    """
    """
    做一個新的解讀碼
    """
    return ans


def decipher(ans, c_string, old_s):
    ps = ''
    new_c_string = c_string.upper()
    """
    改成全部大寫
    """
    for j in range(len(new_c_string)):
        i = ans.find(new_c_string[j])
        if new_c_string[j] == " ":
            ps = ps + " "
        else:
            ps = ps + old_s[i]
        """
        找在新的密碼中，他的序號對應哪個舊密碼，如果遇到空格則維持空格
        """
    return ps








# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
