import time
import statistics
start = time.time()

hands = []

file = open('poker')
data = file.read().split('\n')
file.close()
for val in data:
    data_list = val.split(' ')
    hands.append(data_list)


def high_card(player):
    player = list(''.join(player))
    suit = player[1], player[3], player[5], player[7], player[9]
    valu = player[0], player[2], player[4], player[6], player[8]
    values = []
    for x in valu:
        if x.upper() == 'K':
            values.append(13)
        elif x.upper() == 'A':
            values.append(14)
        elif x.upper() == 'T':
            values.append(10)
        elif x.upper() == 'Q':
            values.append(12)
        elif x.upper() == 'J':
            values.append(11)
        else:
            values.append(x)
    value = sorted(list(map(int, values)))
    return max(value)


def poker_hand(player):
    player = list(''.join(player))
    suit = player[1], player[3], player[5], player[7], player[9]
    valu = player[0], player[2], player[4], player[6], player[8]
    values = []
    for x in valu:
        if x.upper() == 'K':
            values.append(13)
        elif x.upper() == 'A':
            values.append(14)
        elif x.upper() == 'T':
            values.append(10)
        elif x.upper() == 'Q':
            values.append(12)
        elif x.upper() == 'J':
            values.append(11)
        else:
            values.append(x)
    values = sorted(list(map(int, values)))

    if values == [10, 11, 12, 13, 14]:
        return 10
    if len(set(suit)) == 1 and values == list(range(min(values), max(values) + 1)):
        return 9
    if len(set(values)) == 2:
        for x in set(values):
            if values.count(x) == 4:
                return 8, x
    if len(set(values)) == 2:
        house = []
        for y in set(values):
            house.append(values.count(y))
        if sorted(house) == [2, 3]:
            return 7, statistics.mode(values)
    if len(set(suit)) == 1:
        return 6
    if values == list(range(min(values), max(values) + 1)):
        return 5
    if len(set(values)) == 3:
        for x in set(values):
            if values.count(x) == 3:
                return 4, x
    if len(set(values)) == 3:
        t_pairs = []
        for x in set(values):
            t_pairs.append(values.count(x))
        if sorted(t_pairs) == [1, 2, 2]:
            return 3
    if len(set(values)) == 4:
        for x in set(values):
            if values.count(x) == 2:
                return 2, x
    return 1, max(values)


wins = 0
for cards in hands:
    player_one = cards[0:5]
    player_two = cards[5:]
    one = poker_hand(player_one)
    two = poker_hand(player_two)
    try:
        if len(one) == 2 and len(two) == 2:
            if one == two:
                if high_card(one) > high_card(two):
                    wins += 1
            elif one[0] > two[0]:
                wins += 1
            elif one[0] == two[0]:
                if one[1] > two[1]:
                    wins += 1
    except TypeError:
        try:
            if len(one) == 2 and len(str(two)) == 1:
                if one[0] > two:
                    wins += 1
        except TypeError:
            try:
                if len(str(one)) == 1 and len(two) == 2:
                    if one > two[0]:
                        wins += 1
            except TypeError:
                continue
print(wins)
end = time.time()
print("Time", end - start)
