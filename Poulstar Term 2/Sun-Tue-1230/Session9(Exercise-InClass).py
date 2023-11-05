question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().replace("-","").replace("_","")
if question == "fortytwo" or question == "42":
    print("Yes")
else:
    print("No")