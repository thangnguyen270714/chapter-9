"""
Author: Nguyen Duc Thang
Date: 26/09/2021
Program: page_132_project_02.py
Problem: Write a script that inputs a line of encrypted text and a distance value and outputs
    plaintext using a Caesar cipher. The script should work for any printable characters
Solution:
    ....
"""
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - (distance - (ord('a') - ordvalue - 1))
    plainText += chr(cipherValue)
print(plainText)