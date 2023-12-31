from cpu import CPU
from bus import BUS
import sys


def main():
    bus = BUS()
    cpu = CPU(bus) 
     
    cpu.reset() 
         
    bus.load_rom("s.bin", 0x8000) 
    
    print("6502 Debugger")
   
    
    bus.dump_memory_at_addr(0x8000)
    command = "" 
    while 1:
        # print(f"{hex(cpu.address)} {hex(cpu.data)} {bus.r}")
        clear_last_lines(11)
        bus.dump_memory_at_addr(cpu.pc)
        print()
        inp = input("\33[2K\r\033[31m>>>\033[0m ")
        if inp: 
            command = inp
        if command in ["h", "help"]:
            print_help()
        elif command in ["n", "next"]:
            cpu.clock()
        elif command in ["p", "print"]:
            cpu.print_registers()
        elif command[0] in ["d", "display"]: 
            try:
                address = int(command.split()[1], 16)
                bus.dump_memory_at_addr(address)
            except:
                print("Invalid address")
        elif command in ["q", "quit"]:
            print("quitting debugger")
            exit(0)
        elif command in ["r", "reset"]:
            cpu.reset()
        elif command in ["s", "set"]:
            try:
                bus.memory[int(command.split()[1], 16)] = int(command.split()[2], 16)
            except:
                print("Invalid address or data")
        else:
            print("Invalid command")
            print("Type 'h' or 'help' for full list of commands")
                

def clear_last_lines(num_lines=9):
    # Move the cursor up `num_lines` times
    sys.stdout.write('\033[F' * num_lines)

    # Clear each line
    for _ in range(num_lines):
        sys.stdout.write('\033[K')  # Clear the line

    # Move the cursor back to the beginning of the first cleared line
    sys.stdout.write('\r')

def print_help():
    print("h, help: print this help message")
    print("n, next: execute next instruction")
    print("p, print: print cpu state")
    print("d, display: display memory")
    print("q, quit: quit debugger")
    


if __name__ == '__main__':
    main()
