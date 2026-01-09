'''
Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

Example 4:
Input: s = "((()))"
Output: True



'''

opening_brackets = ['(', '{', '[', '<']
closing_brackets = [')', '}', ']']
bracket_dict = {
    '}': '{',
    ']': '[',
    ')': '('
}

def is_valid(characters):
    stack = []
    for bracket in characters:
        if bracket == '{' and '<' in stack:
            return False
        elif bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            popped_bracket = stack.pop()
            if popped_bracket != bracket_dict.get(bracket):
                return False
    
    return True


print(f"Example 1: {is_valid("()")}")
print(f"Example 2: {is_valid("()[]{}")}")
print(f"Example 3: {is_valid("(]")}")
print(f"Example 4: {is_valid("((()))")}")
# print(f"Example 4: {is_valid("<<()>>")
print(f"Example 5: {is_valid("<<{}>>")}")

