def grade_book(grade):
    try:
        if grade > 90:
            return "A+"        
        elif grade > 80:
            return "A"
        elif grade > 70:
            return "B"
        elif grade > 50:
            return "C"
        elif grade > 0:
            return "F"
    except:
        return "Error"
result = grade_book(grade=75) # result = "B"
print(f"Final Score : {result}")