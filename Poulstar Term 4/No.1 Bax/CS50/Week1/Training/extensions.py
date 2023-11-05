user_entered_format = input("File Name: ")

try:
    name,extension = user_entered_format.split(".")
    if extension in ["jpeg","gif","png"]:
        print(f"image/{extension}")
    elif extension in ["pdf","zip"]:
        print(f"application/{extension}")
    elif extension == "txt":
        print("text/plain")
except Exception:
    print("application/octet-stream")
