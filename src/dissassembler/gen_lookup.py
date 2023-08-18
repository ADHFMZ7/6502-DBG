
print("lookup = {")

def op_info(op):
    return ("PNE",2)

for i in range(256):
    if i >= 15 and not i % 16:
        print()
    print(f"{hex(i)}: {op_info(i)}", end="")
    if i == 255:
        print("}")
        break
    print(end=", ")

