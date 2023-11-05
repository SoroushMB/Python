# E = mc**2
# Mass * (Light Speed ** 2) = Energy
def formula(mass):
    return mass * (300000000 ** 2)
user_mass = int(input("m: "))
final_result = formula(mass=user_mass)
print(f"E: {final_result}")