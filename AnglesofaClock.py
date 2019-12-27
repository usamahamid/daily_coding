# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
import math


def calc_angle(h, m):
    h = h + (m / 60)
    hour_angle = h * 30
    if hour_angle >= 360:
        hour_angle = hour_angle - 360
    minute_angle = m * 6
    return math.fabs(hour_angle - minute_angle)


if __name__ == '__main__':
    print(calc_angle(3, 30))  # 75
    print(calc_angle(12, 30))  # 165
    print(calc_angle(5, 10))  # 95
    print(calc_angle(6, 00))  # 180
    print(calc_angle(9, 00))  # 270
    print(calc_angle(1, 50))  # 245
