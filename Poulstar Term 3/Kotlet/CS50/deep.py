Annanaz = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").replace("_","").replace("-","").replace(" ","").lower()

if Annanaz in ["fortytwo", "42"]:
    print("Yes")
else:
    print("No")