#question 4

students = int(input("Number of students:"))
books = int(input("Number of books:"))
books_per_student = books // students
books_leftover = books % students
print(books_per_student,"books per student, which leaves",books_leftover,"books leftover.")


#question 5
print("\n")
name = input("Your name:")
length = len(name)
print("Your name is",length,"characters long.")
