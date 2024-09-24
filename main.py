def main():
    global letters
    letters = [
        {"letter": "a", "count": 26743},
        {"letter": "b", "count": 5026},
        {"letter": "c", "count": 9243},
        {"letter": "d", "count": 16863},
        {"letter": "e", "count": 46043},
        {"letter": "f", "count": 8731},
        {"letter": "g", "count": 5974},
        {"letter": "h", "count": 19725},
        {"letter": "i", "count": 24613},
        {"letter": "j", "count": 504},
        {"letter": "k", "count": 1755},
        {"letter": "l", "count": 12739},
        {"letter": "m", "count": 10604},
        {"letter": "n", "count": 24367},
        {"letter": "o", "count": 25225},
        {"letter": "p", "count": 6121},
        {"letter": "q", "count": 324},
        {"letter": "r", "count": 20818},
        {"letter": "s", "count": 21155},
        {"letter": "t", "count": 30365},
        {"letter": "u", "count": 10407},
        {"letter": "w", "count": 7638},
        {"letter": "v", "count": 3833},
        {"letter": "x", "count": 677},
        {"letter": "y", "count": 7914},
        {"letter": "z", "count": 19725}
    ]

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def word_count():
    with open("books/frankenstein.txt") as f:
        words = f.read().split()
        count = len(words)
        print(f"There are {count} words in this book")

def character_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}  # Initialize counts for a-z

        for char in file_contents:
            if char in letter_counts:
                letter_counts[char] += 1

        for letter, count in letter_counts.items():
            print(f"There are {count} '{letter}'s in this book")

def book_report():
    total_words = sum(letter["count"] for letter in letters)  # Calculate total occurrences
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")
    
    # Sort letters by count in descending order
    letters.sort(key=lambda x: x["count"], reverse=True)
    
    # Print character counts
    for letter in letters:
        print(f"The '{letter['letter']}' character was found {letter['count']} times")
    
    print("--- End report ---")

# Execute functions
main()
word_count()
character_count()
sorted_letters = book_report()
print(sorted_letters)
