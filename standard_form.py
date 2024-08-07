# A program to convert numbers to standard forms

# y = 5000
# is (y / 10 > 1) YES => 5000 / 10 | x = 1, y = 500
# is (y / 10 > 1) YES => 500  / 10 | x = 2, y = 50
# is (y / 10 > 1) YES => 50   / 10 | x = 3, y = 5
# is (y / 10 > 1) NO => STOP
# OUTPUT => 5 x 10^3

# y = 5432
# is (y / 10 > 1) YES => 5432  / 10 | x = 1, y = 543.2
# is (y / 10 > 1) YES => 543.2 / 10 | x = 2, y = 54.32
# is (y / 10 > 1) YES => 54.32 / 10 | x = 3, y = 5.432
# is (y / 10 > 1) NO => STOP
# OUTPUT => 5.432 x 10^3


# -6500
# -6.5 x 10^3
# -0.05


def standardForm(y):
    x = 0
    # 0 to < 1 (ex: 0.0234)
    if (y < 1 and y > 0):
        while (y * 10 < 10):
            x -= 1
            y = y * 10
    # -1 to 0 (ex: -0.566)
    elif (y > -1 and y < 0):
        while (y * 10 > -10):
            x -= 1
            y = y * 10
    # -1 to -infinity (ex: -555666600000)
    elif (y < -1):
        while (y / 10 < -1):
            x += 1
            y = y/10
    else:
        while (y / 10 > 1):
            x += 1
            y = y/10

    print("{} x 10^{}".format(y, x))

standardForm(5000)
standardForm(-5432)
standardForm(0.00045)
standardForm(-0.056)