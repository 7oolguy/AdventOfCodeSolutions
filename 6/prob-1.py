def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lst = []
        for line in lines:
            corridor = line
            lst.append([step for step in corridor])

    return lst

line = read_input('6/input.txt')
print(line)
