def get_even_numbers(numbers):

    even_numbers = [x for x in numbers if x % 2 == 0]

    return even_numbers

my_dict = {'apple': 3, 'banana': 1, 'orange': 5, 'grape': 2}

# Sort the items by value and convert the result back to a dictionary
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# print(my_dict.items())


def plusMinus(arr):
    # Write your code here
    plus = []
    minus = []
    zero = []
    total = len(arr)
    
    for element in arr:
        if element > 0:
            plus.append(element)
        elif element < 0:
            minus.append(element)
        else:
            zero.append(element)
            
    print(f"{(len(plus)/total):.6f}")
    print(f"{(len(minus)/total):.6f}")
    print(f"{(len(zero)/total):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
