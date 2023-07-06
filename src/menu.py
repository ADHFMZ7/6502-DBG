import sys, os
import curses
from cpu import CPU
from bus import BUS


def init_cpu(filename, addr=0x8000):
    bus = BUS()
    cpu = CPU(bus)
    
    bus.load_rom(filename, addr)

    return cpu 
    

def draw(stdscr):
    """
    Draw the user interface for the debugger
    
    It will allow the user to have multiple panes:
    - One of the CPU registers
    - One of the memory at the current PC
    - One of the disassembled code at the current PC
    It will also give the user a prompt to enter commands at the bottom
    """
    k = 0
    cpu = init_cpu(sys.argv[1]) 
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()  
    
    
    
    while cpu.pc < 0xFFFF:
        pass        
        
    
    
def main():
    curses.wrapper(draw)
    return 0

if __name__ == "__main__":
    main()







