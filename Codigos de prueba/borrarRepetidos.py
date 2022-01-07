with open("test3.txt","r") as f_in:
    norepetidos = set(f_in.readlines())
with open("test3test.txt","w") as f_out:
    f_out.write("".join(norepetidos))