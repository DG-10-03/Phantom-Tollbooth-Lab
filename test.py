import phantom_tollbooth
from phantom_tollbooth import get_text
def main():
    # assign book's text to a string variable
    book_text = get_text()

# make everything lowercase to ensure uniformity
    book_text = book_text.lower()

# split the text into words
    words = book_text.split()

# word groups to exclude
    exclude_words = {'the', 'a', 'an', 'of', 'on', 'over', 'above', 'and', 'but', 'or', 'he', 'her', 'it'}

# count word frequency
    word_count = {}
    for word in words:
        if word not in exclude_words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

# get top 50 most common words
    top_50_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:50]

# print top 50 most common words
    for word, count in top_50_words:
        print(f"{word}: {count}")


if __name__ == '__main__':
    main()