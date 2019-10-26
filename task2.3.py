text = input("Enter the text: ").split(" ")
text.sort(key=len)
print(" ".join(text))


