imapping = {
    "SUBBY":0b00000000000000,
    "LDUR":0b01000000000000,
    "STUR": 0b10000000000000,
    "ADDY":0b11000000000000,
    "X0":[0b00000000000000,0b00000000000000,0b00000000000000],
    "X1" :[0b00010000000000,0b00000100000000, 0b00000001000000],
    "X2":[0b00100000000000,0b00001000000000,0b00000010000000]}

def decoder(instruction):
    machinecode = 0b00000000000000
    position = -1
    instruction = instruction.split(" ")
    for part in instruction:
        if part not in imapping:
            machinecode |= int(format(int(part),"014b"))
            continue
        if position >= 0:
            machinecode |= imapping[part][position]
        else:
            machinecode |= imapping[part]
        position +=1
    return machinecode
def decoding(instructions):
    with open("image_file.txt", "w") as file:
        file.write("v3.0 hex words addressed\n")
        newLine = True
        for address,instruction in enumerate(instructions):
            decoded = decoder(instruction)
            if address % 16 == 0 and address != 0:
                file.write(f"{decoded:02x}\n")
                newLine = True
            elif newLine:
                file.write(f"{address:02x}: {decoded:02x} ")
                newLine = False
            else:
                file.write(f"{decoded:02x} ")
                

instructions = []       

with open("program.txt","r") as file:
    for line in file:
        instruction = line.strip()
        instructions.append(instruction)

decoding(instructions)
print("done")
