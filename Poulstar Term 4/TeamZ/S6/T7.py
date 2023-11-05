class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

def main():
    first_student = Student(name="Saman",house="Golsar")
    print(f"{first_student.name} from {first_student.house}")
    
if __name__ == "__main__":
    main()