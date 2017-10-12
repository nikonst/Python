import pandas as pd
import matplotlib.pyplot as plt
import os

def replace_skip_characters(text):
    skip_chars = [".", ",", "?", "!", "(", ")", "&", "[", "]", ";", ":", "'", '"']
    for char in skip_chars:
        text = text.replace(char, "")
    return text

def count_words(text):
    text = text.lower()
    text = replace_skip_characters(text)
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] +=1
        else:
            word_counts[word] = 1
    return word_counts
    # another method to count is Counter object fron collections

def number_of_unique_words(words_dictionary):
    return len(words_dictionary)

def count_all_words(words_dictionary):
    return sum(words_dictionary.values())

def read_book(title_path):
    with open(title_path,"r",encoding="utf-8") as the_file:
        file_text = the_file.read()
        file_text = file_text.replace("\n"," ").replace("\r", " ")
    return file_text

books_table = pd.DataFrame(columns=("BOOK_TITLE","TOTAL_WORDS","UNIQUE_WORDS"))
books_table_row =1

for book_title in os.listdir("JamesJoyceBooks"):
    input_file = "JamesJoyceBooks"+"/"+book_title
    print(input_file)
    book_file_name = input_file
    text_of_book = read_book(book_file_name)
    book_words_dictionary= count_words(text_of_book)

    books_table.loc[books_table_row] = book_title.replace(".txt",""), count_all_words(book_words_dictionary), number_of_unique_words(book_words_dictionary)
    books_table_row += 1

    print("The number of unique words in the book ", book_file_name," is", number_of_unique_words(book_words_dictionary))
    print("The number of total words in the book ", book_file_name," is", count_all_words(book_words_dictionary))

print(books_table)

plt.figure(figsize=(3,3))
subset = books_table[books_table.BOOK_TITLE == "Dubliners"]
plt.loglog(subset.TOTAL_WORDS, subset.UNIQUE_WORDS,"o",label="Dubliners",color="blue")
subset = books_table[books_table.BOOK_TITLE == "Ulysses"]
plt.loglog(subset.TOTAL_WORDS, subset.UNIQUE_WORDS,"o",label="Ulysses",color="red")
subset = books_table[books_table.BOOK_TITLE == "A Portrait of the Artist as a Young Man"]
plt.loglog(subset.TOTAL_WORDS, subset.UNIQUE_WORDS,"o",label="A Portrait of the Artist as a Young Man",color="green")
subset = books_table[books_table.BOOK_TITLE == "Chamber Music"]
plt.loglog(subset.TOTAL_WORDS, subset.UNIQUE_WORDS,"o",label="Chamber Music",color="lightblue")
plt.legend()
plt.title('Books by James Joyce')
plt.xlabel("Total Number of Words")
plt.ylabel("Number of Unique Words")
plt.show()
#plt.savefig('JamesJoyceBooks.png')
