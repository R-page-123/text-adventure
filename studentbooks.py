numb = int(input("numer of books "))
nums = int(input("number of students "))
spb = numb // nums
extr = numb % nums
print(spb, "book(s) per person with", extr, "left over")