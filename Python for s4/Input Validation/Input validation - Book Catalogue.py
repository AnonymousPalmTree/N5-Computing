#input validation

print("""
Your choices are:
                   1. Add Book
                   2. View Catalogue
                   3. Search Books
                   4. Exit
""")

choice = int(input("Enter either 1, 2, 3 or 4 to choose: "))

if choice>4 :
    print("ERROR!! PLEASE SELECT A VALID OPTION!!")

if choice<1 :
    print("ERROR!! PLEASE SELECT A VALID OPTION!!")