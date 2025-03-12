def count_chars(s):
    vowels = "aeiouAEIOU"
    vowels_count = consonants_count = blanks_count = 0
    
    for char in s:
        if char in vowels:
            vowels_count += 1
        elif char.isalpha():  # Checks if it's a letter (consonant)
            consonants_count += 1
        elif char == " ":
            blanks_count += 1
    
    return vowels_count, consonants_count, blanks_count

def main():
    user_input = input("Enter a string: ")
    vowels, consonants, blanks = count_chars(user_input)
    print(f"Vowels: {vowels}, Consonants: {consonants}, Blanks: {blanks}")

if __name__ == "__main__":
    main()