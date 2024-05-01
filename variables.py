#Find the type of variable
x=5
y="Areesha"
print(type(y))

#assign values to multiple variables
x,y,z="chocolate",2,5
print(x,y,z)

#assign one value to multiplevariables
x=y=z="apple"
print(x,y,z)

#python allows us to extract data from list and stores into variables
Fruits=["apple", "banana"]
fruitlist=Fruits
l,m=fruitlist
print(l,m)

Vegetables=( "potatoes","tomatoes","peas","onions","bringels","chillis",("spanish","corrineder","mint"))
vegetablelist=Vegetables
a,b,c,d,e,f,g=vegetablelist
print(g)

green,red,yellow,green,blue,orange,black=Vegetables
print(green,red,yellow,green,blue,black)

#Global Variables
x="areesha" #x is a global variable which can be access anyware in the program
def myfun():
    print (x +" "+"hamza")

myfun()

f="Sonia"
def myfunction():
    global q #global keyword make the scope globally
    q="ayat"
    print(q, f +" "+"shahid") 
myfunction()   
print(q)