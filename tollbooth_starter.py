import phantom_tollbooth
# I searched the internet for ways to remove special characters and other things and was able to  find the regular expression function in which I implemented to remove the special characters to make words such as I'll into 'I' 'll'.
import re  
# I also searched up the internet to find ways to count words in a string and found the counter function which stores the elements of the string into dictionary keys and their counts into values.
from collections import Counter
def main():
    book = phantom_tollbooth.get_text()
    # Convert the book's text to lowercase
    book = book.lower()

    # Remove punctuation and special characters
    # r: This is a prefix indicating a raw string literal in Python. It's used to avoid the interpretation of backslashes as escape characters.
    # \W+: This is a regular expression pattern that matches one or more non-word characters. In regular expressions, \W represents any non-word character (equivalent to [^a-zA-Z0-9_]), and + means one or more occurrences.
    # ' ': This is the replacement string. In this case, it's a space. It means that every match of the pattern specified in re.sub() will be replaced with a single space.

    # book: This is the string on which the substitution is being performed.
    book = re.sub(r'\W+', ' ', book)

    # Split the text into words
    words = book.split()

    # Remove articles, prepositions, conjunctions, and pronouns from the words list
    # Also used the internet to find ways to remove certain words in which I found stopwords, which remove high frequency words that are unimportant.
    # The stopwords took the longest to finalize as I had to list down all prepositions, conjunctions, and articles as well as letters that appeared after being seperated from words.  
    stop_words = {'the', 'a', 'an', 'of', 'on', 'over', 'above', 'and', 'but', 'or', 'he', 'her', 'it', 'to', 'you', 'in', 'i', 'as', 'that', 'his', 'for', 'was', 'they', 'at', 'be', 'is', 'from', 'had', 'have', 'we', 'what', 'can', 'them', 'were', 'up', 'are', 's', 'll', 't', 'm', 'd', 'me', 'my', 'by', 'your', 'who'}
    words = [word for word in words if word not in stop_words]

    # Count the occurrences of each word using a dictionary
    word_counts = Counter(words)

    # Used the internet for the lambda key.
    # Sort the dictionary in descending order of word frequency.
    # The lambda key function is a small anonymous function.
    # A lambda function can take any number of arguments, but can only have one expression.
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the top 50 words along with their frequencies
    for word, count in top_words[:50]:
        print(f'{word}: {count}')
if __name__ == '__main__':
    main()