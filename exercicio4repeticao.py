paísA = 80000
paísB = 200000
anos = 0

while paísA <= paísB :
    paísA = paísA + (paísA * 0.03)
    paísB = paísB + (paísB * 0.015)
    anos = anos + 1

print ("Levará", anos, "anos para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.")