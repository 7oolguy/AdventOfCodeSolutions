import re

def calculate_mul_sum(file_path):
    try:
        # Read the file
        with open(file_path, 'r') as file:
            data = file.read()

        # Regex to extract valid mul(X,Y) instructions
        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, data)

        # Calculate the sum of all valid multiplications
        total_sum = sum(int(x) * int(y) for x, y in matches)

        return total_sum

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Input file path
file_path = "3/input.txt"
result = calculate_mul_sum(file_path)

if result is not None:
    print(f"The sum of all valid mul(X,Y) results is: {result}")
