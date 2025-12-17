def countnumberofwords(text):  
    words = text.split()

    num_words = len(words)    
    print(f"Found {num_words} total words") 
def number_of_symbols(text):
    lower_case_text = text.lower()
    symbols = {}
    for char in lower_case_text:
        if char.isalpha():
            if char in symbols:
                symbols[char] += 1
            else:
                symbols[char] = 1
        

    # sort by count descending, then by symbol ascending for ties
    for symbol, count in sorted(symbols.items(), key=lambda item: (-item[1], item[0])):
        print(f"{symbol}: {count}")

    
    
