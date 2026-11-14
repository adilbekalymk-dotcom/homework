book = {
    "wemmbu": "0547 485 758",
    "azat": "0567 675 667",
    "nick": "0567 584 684",
    "aras": "0567 664 638",

}
name = input("enter the name")
if name in book:
    print(book[name])
else:
    print("not found")