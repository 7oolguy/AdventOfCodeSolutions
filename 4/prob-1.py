def read_file_as_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

# Exemplo de uso
filename = "4/input.txt"
grid = read_file_as_grid(filename)

counter = 0
for i in range(0, len(grid)):
    row = grid[i]
    for j in range(0, len(row)):
        character = row[j]

        #Horizontal
        if character == 'X' and (j + 3) < len(row):
            #Forwards
            X = character
            M = row[j + 1]
            A = row[j + 2]
            S = row[j + 3]
            XMAS = f'{X}{M}{A}{S}'
            if XMAS == 'XMAS':
                counter += 1
