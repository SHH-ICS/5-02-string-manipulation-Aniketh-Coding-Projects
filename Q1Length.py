while True:
    word = input("Enter a word (or type 'quit' to exit): ")
    if word.lower() == 'quit':
        print("Exiting program. Goodbye!")
        break
    print(f"The length of the word '{word}' is {len(word)} characters.")