import os
import sys

if len(sys.argv) <= 1:
    print("Expected argument")
    print(f"usage: python3 {sys.argv[0]} [filename]")
    exit(1)

filename = sys.argv[1]

# Function from https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte
def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break
inside = 0
for byte in bytes_from_file(filename):
    if inside:
        inside -= 1
        continue
    print("\033[91m{:02x}\033[0m".format(byte)) 

    op = lookup[byte]
    inside = op[1]
    print(op[0], end=" ")

