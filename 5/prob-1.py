def read_input(file):
    with open(file, 'r') as txt:
        lines = txt.readlines()
    rules = []
    updates = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        elif "|" in line:
            div = line.split('|')
            rules.append([int(num) for num in div])  # Convert to int immediately
        elif "," in line:
            up = line.split(',')
            updates.append([int(num) for num in up])  # Convert to int immediately

    return rules, updates

def is_valid_update(rules, update):
    for rule in rules:
        page, page2 = rule
        if page in update and page2 in update:
            page_index = update.index(page)
            page2_index = update.index(page2)
            if page_index > page2_index:  # Check if the order is correct
                return False
    return True

def get_the_middle_pages(rules, updates):
    middle_pages = []
    for update in updates:
        if is_valid_update(rules, update):
            middle_pages.append(update[len(update) // 2])  # Get the middle page
    return middle_pages

def sum_list(lst):
    return sum(lst)

input_path = '5/input.txt'
rules, updates = read_input(input_path)  # Read rules and updates
pages = get_the_middle_pages(rules, updates)  # Get the valid updates' middle pages
num = sum_list(pages)  # Sum of all middle pages
print(num)
