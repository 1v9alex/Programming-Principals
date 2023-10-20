prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p != 'Q' and p!= 'O':
        print(p + suffix)
    elif p == 'Q':
        print('Quack')
    elif p == 'O':
        print('Ouack')