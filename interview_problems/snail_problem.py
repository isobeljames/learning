# A snail climbs a wall, it starts at the bottom and climbs n meters a day
# It slides down m meters a day
# Given the height of the wall H, write a program to calculate number of days
# required for the snail to reach the top of the wall
# input = 3 non-negative integers separated by a space (no comma)

input_list = input().split(" ")
n = int(input_list[0])
m = int(input_list[1])
H = int(input_list[2])

def snail_progress(n, m, H):
    days = 0
    snail_height = 0
    if m > n:
        print("FAIL")
    while snail_height < H:
        snail_height += n-m
        days += 1
    return days

print(snail_progress(n, m, H))
