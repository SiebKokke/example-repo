replace = "The!quick!brown!fox!jumps!over!the!lazy!dog"
print(replace) 
space = replace.replace("!", " ")
print(space)

capitalized_replace = space.upper()
print(capitalized_replace)

reversed = capitalized_replace [::-1]
print(reversed)