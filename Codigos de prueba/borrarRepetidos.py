with open("Valdivia1.txt","r") as f_in:
    norepetidos = set(f_in.readlines())
with open("ValdiviaNR.txt","w") as f_out:
    f_out.write("".join(norepetidos))