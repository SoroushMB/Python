def main():
    pasted_info = get_info()
    print(f"""{pasted_info[0]} 
from 
{pasted_info[1]}""")

def get_info():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()