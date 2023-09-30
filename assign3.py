def most_frequent(input_string):
    
    letter_frequency = {}

    
    for char in input_string:
        if char.isalpha():
            char = char.lower()  
            letter_frequency[char] = letter_frequency.get(char, 0) + 1

    
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

    
    for char, freq in sorted_frequency:
        print(f"'{char}': {freq} times")


input_string = input("Enter a string: ")

most_frequent(input_string)
