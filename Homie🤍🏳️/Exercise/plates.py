def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")
i = 0
def is_valid(s):
	global i

	if len(s) < 2 or len(s) > 6:
		return False
	if s[0:2].isdigit():
		return False

	for c in s:
		if c in ['.',' ','!','?']:
			return False

	while i < len(s):
		i += 1
		if s[i].isdigit() and s[i:].startswith("0") == True:
			return False
		else:
			return True
	return True

main()
