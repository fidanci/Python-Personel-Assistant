from system_module import clear_console
from input_module import take_input
from process_module import process
from output_module import output

clear_console()

while(True):
    
    i = take_input()
    o = process(i)
    output(o)