def common_chars(str1, str2):
    common = set(str1) & set(str2)  # Using set intersection to find common characters
    print("Common characters:", ''.join(common))

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    common_chars(str1, str2)

if __name__ == "__main__":
    main()
