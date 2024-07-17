immutable_var = (1, "call", True)
print(immutable_var)

#immutable_var[0] = 2
#print(immutable_var)

mutable_list = [1, "call", True]
mutable_list.append("back")
mutable_list.extend("reroll")
mutable_list[0] = 2
print(mutable_list)