a= "amaan"
b="AMAAN"
print(len(a)) 
print("make the string into lower case :",b.lower())
print("make the string into upper case :",a.upper())



a="!!!!amaan khan !!!!!!"
print(a.rstrip("!"))



a="amaan khan !!!!$"
print(a.replace("!!!!$","waris"))



a="amaan ullah waris khan , 1,2,3,@,#,$" 
print(a.split( "    "))



a="amaanullajkhan"
print(a.capitalize())

a="amaanullajkhan"
print(a.center(10))
print(len(a.center(10)))


a="amaan ullah khan he io  good boy amaan  amaan"
print(a.count("amaan"))
print(a.count("a"))



a="amaan ullah khan he io  good boy amaan  amaan"
print(a.endswith("a"))
print(a.startswith("a"))
print(a.startswith("a",3,9))


a="amaan ullah khan he io  good boy amaan  amaan"
print(a.find("z"))


a="amaan ullah khan he io  good boy amaan  amaan"
print(a.index("l"))


a="amaanullahkhanhe23456789DFGHJK"
print(a.isalnum())
print(a.isalpha())



a="amaanullahkhanh"
print(a.islower())

a= "AMAANKHANULLAH"
print(a.isupper())


a= "amaanullahkhanh\n"
b= "amaanullahkhanh"
print(a.isprintable())
print(b.isprintable())
a="         "
print(a.isspace())

a= "amaanullahkhanh"
b= "Amaanullahkhanh"
print(a.istitle())
print(b.istitle())

a= "amaanullahkhanh"
print(a.swapcase())
a= "amaan ullah khan"
print(a.title())
