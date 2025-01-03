file = open("text_II.dat","wb")
file.write("01001000 01101001 00101100 00100000 01001001 00100111 01101101 00100000 01110011 01100001 01111001 01100001 01101110")
file.close()

file = open("text_II.dat0","rb")
EVM = file.read()
print(EVM)