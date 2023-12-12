input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

rows, columns, queries = map(int, input_file.readline().split())
col_names = input_file.readline().split()
col_set = set(col_names)
col_dict = {col: col_names.index(col) for col in col_set}

table = [list(map(int, input_file.readline().split())) for _ in range(rows)]

min_val = -1 * 10**9 - 1
max_val = 10**9 + 1
column_ranges = {}
for i in range(queries):
    conditions = input_file.readline().split()
    col_ind = col_dict[conditions[0]]
    op = conditions[1]
    col_range = column_ranges.get(col_ind, (min_val, max_val))
    value = int(conditions[2])
    if op == '>':
        new_min = max(col_range[0], value)
        if new_min >= col_range[1]:
            print(0)
            exit(0)
        column_ranges[col_ind] = (new_min, col_range[1])
    else:
        new_max = min(col_range[1], value)
        if new_max <= col_range[0]:
            print(0)
            exit(0)
        column_ranges[col_ind] = (col_range[0], new_max)

table_iter = iter(table)
for col_ind in column_ranges.keys():
    col_range = column_ranges[col_ind]
    table_iter = (row for row in table_iter if col_range[0] < row[col_ind] < col_range[1])

summ = 0
for row in table_iter:
    summ += sum(row)
output_file.write(str(summ))
