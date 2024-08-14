#love calculator
boyfriend = input("Enter your boyfriend name: ").lower()
girlfriend = input("Enter your girlfriend name: ").lower()
string = (boyfriend + girlfriend)

T = int(string.count("t"))
R = int(string.count("r"))
U = int(string.count("u"))
E = int(string.count("e"))

a = T+R+U+E

L = int(string.count("l"))
O = int(string.count("o"))
V = int(string.count("v"))
E = int(string.count("e"))

b = L+O+V+E


print(str(a)+ "" +str(b))
