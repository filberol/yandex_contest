input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

cards_a_count, cards_b_count, change_count = map(int, input_file.readline().split(' '))
cards_a_set = {}
cards_b_set = {}

for card in map(int, input_file.readline().split(' ')):
    cards_a_set[card] = cards_a_set.get(card, 0) + 1

for card in map(int, input_file.readline().split(' ')):
    cards_b_set[card] = cards_b_set.get(card, 0) + 1

differing_cards = {}

for non_crossing_key in set(cards_a_set) ^ set(cards_b_set):
    if non_crossing_key in cards_a_set:
        differing_cards[non_crossing_key] = cards_a_set[non_crossing_key]
    else:
        differing_cards[non_crossing_key] = cards_b_set[non_crossing_key]

for crossed_key in set(cards_a_set) & set(cards_b_set):
    differing_cards[crossed_key] = abs(cards_a_set[crossed_key] - cards_b_set[crossed_key])

res = []

changes_verified = 0
while changes_verified < change_count:
    change = input_file.readline().split(' ')
    changed_set = cards_a_set if change[1] == "A" else cards_b_set
    else_set = cards_a_set if change[1] == "B" else cards_b_set
    new_card = int(change[2])

    if int(change[0]) == 1:
        changed_set[new_card] = changed_set.get(new_card, 0) + 1
        if new_card not in else_set:
            differing_cards[new_card] = differing_cards.get(new_card, 0) + 1
        else:
            differing_cards[new_card] = abs(cards_a_set[new_card] - cards_b_set[new_card])
    else:
        changed_set[new_card] = max(0, changed_set.get(new_card, 0) - 1)
        if new_card in else_set:
            differing_cards[new_card] = abs(cards_a_set[new_card] - cards_b_set[new_card])
        else:
            differing_cards[new_card] = changed_set[new_card]

    res.append(sum(differing_cards.values()))
    changes_verified += 1

line = ' '.join(str(x) for x in res)
output_file.write(line)
