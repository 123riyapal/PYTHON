# match is like a switch case

name=input("Enter your name and find your maths grade :")
match name :
    case "Riya" | "purnima"|"shagun":
        print("90 grade")
    case "ishita":
        print("80 grade")
    case "lavanya":
        print("70 grade")
    case _:
        print("you are not the student of this college")