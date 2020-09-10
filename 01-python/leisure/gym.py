def draw_gym():
    data = [['+---------------------+'], ['| Welcome to Gym 506! |'],
            ['+---------------------+'], ['|        _ _  hey     |'],
            ['|        | |  O/      |'], ['|        ||| /|       |'],
            ['|        | |  /\      |'], ['+---------------------+']]

    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print "".join(word.ljust(col_width) for word in row)


draw_gym()
