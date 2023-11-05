def percent_to_float(percent): # "10%" -> "10" -> 10 -> 0.1 ?
    return (int(percent.replace("%","")))/100
tip = percent_to_float(percent="%80")
print(tip)