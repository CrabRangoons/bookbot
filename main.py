
def sort_on(dict):
    return dict["num"]

def main(): 
    
     
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    pass


    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()  # blank line for formatting

    
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    
    




    char_list = []
    for char in chars:
        if char.isalpha():  # only include letters
            char_list.append({"letter": char, "num": chars[char]})

# Sort the list
    char_list.sort(reverse=True, key=sort_on)

# Print each character's count
    for char_dict in char_list:
        print(f"The '{char_dict['letter']}' character was found {char_dict['num']} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()