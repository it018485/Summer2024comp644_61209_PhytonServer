mioDizionario = {
    "Honda": "Civic",
    "Ford": "Escape",
    "Toyota": "Rav4"
}
print("\n This is a Dictionary: \n" + str(mioDizionario) + "\n")

# I add 2 pairs, in 2 different ways
mioDizionario ["Lexus"] = "c300"
mioDizionario.update({"BMW":"M6", "VW" : "Golf GTI"})
print("\n I added 3 pairs, in two ways: \n" + str(mioDizionario) + "\n")