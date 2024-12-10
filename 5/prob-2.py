from collections import defaultdict, deque

def read_input(file):
    """
    Reads the input file and parses rules and updates.

    Args:
        file (str): The path to the input file.

    Returns:
        tuple: A list of rules (as lists of two integers) and a list of updates (as lists of integers).
    """
    rules = []
    updates = []
    try:
        with open(file, 'r') as txt:
            lines = txt.readlines()

        for line in lines:
            line = line.strip()  # Remove any leading/trailing whitespace
            if not line:  # Skip blank lines
                continue
            elif "|" in line:  # Line contains a rule
                try:
                    div = line.split('|')
                    rules.append([int(num) for num in div])  # Parse integers
                except ValueError:
                    raise ValueError(f"Invalid rule format: {line}")
            elif "," in line:  # Line contains an update
                try:
                    up = line.split(',')
                    updates.append([int(num) for num in up])  # Parse integers
                except ValueError:
                    raise ValueError(f"Invalid update format: {line}")
            else:
                raise ValueError(f"Unrecognized line format: {line}")

    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return [], []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []

    return rules, updates

def is_valid_order(update, rules):
    # Check if an update follows all applicable rules
    positions = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in positions and y in positions and positions[x] > positions[y]:
            return False
    return True

def topological_sort(update, rules):
    # Sort the update pages using topological sorting
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)

    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def find_middle_page(update):
    # Return the middle page of an update
    return update[len(update) // 2]

def solve_part_two(file):
    # Read input file and solve part two
    rules, updates = read_input(file)

    total = 0
    for update in updates:
        if not is_valid_order(update, rules):
            # Fix the order if it's invalid
            corrected_update = topological_sort(update, rules)
            total += find_middle_page(corrected_update)

    return total

# Example usage
if __name__ == "__main__":
    input_file = "5/input.txt"  # Replace with your file path
    result = solve_part_two(input_file)
    print(f"The total sum of middle pages after fixing is: {result}")
