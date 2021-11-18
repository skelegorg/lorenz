rho = float(input("ρ value: "))
sigma = float(input("σ value: "))
betainput = input("β value: ")
if "/" in betainput:
    binputs = betainput.split("/")
    for ind in range(len(binputs)):
        binputs[ind] = binputs[ind].replace(" ", "")
    beta = float(binputs[0]) / float(binputs[1])
else:
    beta = float(betainput)

