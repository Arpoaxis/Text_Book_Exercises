length = float(input("What is the length of the row?"))
endPost = float(input("How much space does an end-post assembly take?"))
space = float(input("How much space between each vine do you need?"))

numberOfVines = (length - (2 * endPost))/space

print(int(numberOfVines), "vine(s) will fit in the row.")
