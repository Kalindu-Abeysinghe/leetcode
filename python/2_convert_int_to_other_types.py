decimal_hex_dict = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def print_formatted(number):
    # your code goes here
    binary_val_char_count = len(get_value(number=number, base=2))
    
    for index in range(1, number + 1):
        decimal = add_padding(binary_val_char_count, str(index))
        octal = add_padding(binary_val_char_count, get_value(number=index, base=8))
        hex = add_padding(binary_val_char_count, get_value(number=index, base=16))
        binary = add_padding(binary_val_char_count, get_value(number=index, base=2))
        
        print(f"{decimal} {octal} {hex} {binary}")

def get_value(number, base):
    val = ""
    curr = number
    while curr >= 1:
        rem = curr % base
        # means a hex value
        if rem > 9:
            rem = decimal_hex_dict[rem]
        curr = curr // base
        val = str(rem) + val
        
    return val
    
def add_padding(full_length, val): 
    empty_spaces = full_length - len(val)
    padding = " "
    for index in range(empty_spaces):
        padding += " "
        # print(f"{padding}|")
    return padding + val

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)