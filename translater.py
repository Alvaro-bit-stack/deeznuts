imapping = {
    "ADDY":0b00000000,
    "SUBBY":0b01000000,
    "STUR": 0b10000000,
    "LDUR":0b11000000,
    "X0":[0b00000000,0b00000000,0b00000000],
    "X1" :[0b00010000,0b00000100, 0b00000001],
    "X2":[0b00100000,0b00001000,0b00000010]}

def decoder(instruction):
    machinecode = 0b00000000
    position = -1
    instruction = instruction.split(" ")
    for part in instruction:
        if part not in imapping:
            machinecode |= int(format(int(part,2),"08b"),2)
            continue
        if position >= 0:
            machinecode |= imapping[part][position]
        else:
            machinecode |= imapping[part]
        position +=1
    return machinecode
def decoding(instructions):
    with open("image_file.txt", "w") as file:
        for address,instruction in enumerate(instructions):
            decoded = decoder(instruction)
            file.write(f"{hex(address)}:{hex(decoded)}\n")

instructions = []       

with open("program.txt","r") as file:
    for line in file:
        instruction = line.strip()
        instructions.append(instruction)

decoding(instructions)
