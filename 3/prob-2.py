import re

def calculate_conditional_mul_sum(file_path):
    try:
        # Read the file
        with open(file_path, 'r') as file:
            data = file.read()

        # Regex patterns for instructions using named groups
        pattern = r"mul\((?P<mul_x>\d+),(?P<mul_y>\d+)\)|(?P<do>do\(\))|(?P<dont>don't\(\))"

        # Find all instructions in order
        instructions = re.finditer(pattern, data)

        # Initialize state and result
        is_enabled = True  # Initially, mul is enabled
        total_sum = 0

        # Process instructions sequentially
        for match in instructions:
            if match.group("mul_x") and match.group("mul_y"):  # mul(X, Y)
                if is_enabled:
                    total_sum += int(match.group("mul_x")) * int(match.group("mul_y"))
            elif match.group("do"):  # do()
                is_enabled = True
            elif match.group("dont"):  # don't()
                is_enabled = False

        return total_sum

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Input file path
file_path = "3/input.txt"
result = calculate_conditional_mul_sum(file_path)

if result is not None:
    print(f"The sum of all valid mul(X,Y) results is: {result}")
