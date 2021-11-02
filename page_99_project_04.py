"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_99_project_04.py
Problem:A standard science experiment is to drop a ball and see how high it bounces.
    Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index. For example, if a ball dropped from a height of 10 feet bounces 6 feet
    high, the index is 0.6, and the total distance traveled by the ball is 16 feet after
    one bounce. If the ball were to continue bouncing, the distance after two bounces
    would be 10 ft 6 1 1 1 ft 6 ft 3.6 ft 5 25.6 ft. Note that the distance traveled for
    each successive bounce is the distance to the floor plus 0.6 of that distance as the
    ball comes back up. Write a program that lets the user enter the initial height
    from which the ball is dropped and the number of times the ball is allowed to
    continue bouncing. Output should be the total distance traveled by the ball.
Solution:
    ....
"""
chieucao=float(input("Nhap chieu cao:"))
solannay=float(input("Nhap so lan bong nay: "))
donay=float(input("Nhap do nay cua bong: "))
heso=donay/chieucao
print("He so nay cua bong la:",heso)
if solannay==1:
    quangduong=float(chieucao+donay)
    print("Quang duong sau mot lan nay: ",quangduong)
else:
    quangduong=chieucao+(donay*solannay)+(donay*solannay*heso)
    print("Quang duong bong di duoc sau",solannay,"lan nay la:",quangduong)
