book = {
    "wemmbu": "055567384",
    "flame": "0658484845",
    "sherlock": "0658484845",
    "harry potter": "0658484845",
}
name = input("Enter the name: ")
if name in book:
    print(book[name])
else:
    print("Name not found in the book.")