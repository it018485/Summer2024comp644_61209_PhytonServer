# Variabili
miaLista = ["Books", 3.14, "Pencils", "Cars", "Balloons"]
subLista = [1,2,3, "Yahoo"]

miaLista = [miaLista, subLista, True]
print("\n This list contains 2 nested Lists, and a Boolean: \n" + str(miaLista) + "\n")

#First, I remove the Boolean item
miaLista.remove(True)

# looping in the list and print items
for subLista in miaLista:
    for item in subLista:
        print(item)
        
print("\n")