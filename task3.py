rows, columns, queries = list(map(lambda x: int(x), input().split(' ')))
col_names = input().split(' ')
col_dict = {}
for col in range(columns):
    col_dict[col_names[col]] = col

table = []
for row in range(rows):
    table.append(list(map(lambda x: int(x), input().split(' '))))

conditions_checked = 0
while conditions_checked < queries:
    conditions = input().split(' ')
    col_ind = col_dict[conditions[0]]
    value = int(conditions[2])
    new_table = []
    if conditions[1] == '>':
        for row in table:
            if row[col_ind] > value:
                new_table.append(row)
    else:
        for row in table:
            if row[col_ind] < value:
                new_table.append(row)
    conditions_checked += 1
    table = new_table

summ = 0
for row in table:
    summ += sum(row)
print(summ)

