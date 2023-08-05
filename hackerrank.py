
def swap_case(s):
    changed = ""
    for ch in s:
        if ch.isupper:
            changed = changed + lower(ch)
        else:
            changed = changed + upper(ch)
    return changed

def split_and_join(line):
    list1 = line.split(" ")
    changed = "-".join(list1)
    return changed
 
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    response = f"Hello {first} {last}! You just delved into python."
    print(response)

def mutate_string(string, position, character):
    response = ""
    response = string[:position] + character + string[position+1:]
    return response