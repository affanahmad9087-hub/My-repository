comp = input("Enter the IUPAC name of the compound : ")
comp = comp.lower()

d = {"meth" : 1, "eth" : 2, "prop" : 3, "but" : 4, "pent" : 5, "hex" : 6,
     "hept" : 7, "oct" : 8, "non" : 9, "dec" : 10, "undec" : 11, "dodec" : 12}


def identify_parent_chain(c1):
