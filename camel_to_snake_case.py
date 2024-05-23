"""
Convert a camelCase string into snake_case
someOtherWord --> some_other_word
"""

def camel_to_snake_case(s):
    words_in_snake_case = []
    start = 0
    for end,c in enumerate(s):
        if c.isupper():
            words_in_snake_case.append(s[start:end].lower())
            start = end
    # last word in snake case 
    words_in_snake_case.append(s[start:len(s)].lower())
    print(words_in_snake_case)
    return '_'.join(words_in_snake_case)

if __name__ == "__main__":
    assert camel_to_snake_case('camelCase') == 'camel_case'
    assert camel_to_snake_case('someOtherWord') == 'some_other_word'
