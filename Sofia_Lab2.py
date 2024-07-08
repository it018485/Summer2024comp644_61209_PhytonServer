# Variabili
miaLista = ["Books", 3.14, "Pencils", "Cars", "Balloons"]
subLista = [1,2,3]

miaLista = [miaLista, subLista, "Yahoo", True]
print("\n This list contains 2 Lists, a Char, and a Boolean: \n" + str(miaLista))

# Or you can add the values one at the time
miaLista = ["Books", 3.14, "Pencils", "Cars", "Balloons"]
miaLista.append(subLista)
miaLista.append("Yahoo")
miaLista.append(True)
print("\n This list contains Values, 1 List, a Char, and a Boolean: \n" + str(miaLista))

# Now I remove the 2nd Item
miaLista.remove(3.14)
print("\n I deleted the number from the list with the REMOVE method: \n" + str(miaLista) + "\n")