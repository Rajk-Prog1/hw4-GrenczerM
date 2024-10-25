def find_a_string(original_str: str, substr: str) -> int:
    count = 0
    start = 0
    flag = True
    while flag:
        value = original_str.find(substr, start)
        if value == -1:
            flag = False
        else:
            count = count + 1
            start = value + 1
    return count

    pass

#source: https://stackoverflow.com/questions/11476713/determining-how-many-times-a-substring-occurs-in-a-string-in-python