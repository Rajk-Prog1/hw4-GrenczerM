def swap_case(s: str) -> int: #a kimeneti eredménynek nem str kéne hogy legyen?
    results = ""
    for char in s:
        results += char.swapcase() 
    return results  
    pass

#source: https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/isalpha/python-string-isalpha/