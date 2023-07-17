class instruction:
    def __init__(self) -> None:
        self.opcode = None
        self.mnemonic = None
        self.length = None
        self.cycles = None
        self.flags = None
        self.addr = None
        self.group = None
        self.operandOne = None
        self.operandTwo = None

import json
with open('C:\\Users\\Adrian\\Documents\\GameBoy\\emulator\\src\\opcodes.json') as f:
    data = json.load(f)
    instructions = []
    instructionPrefixed = []
    for code, details in data['unprefixed'].items():
        newInstr = instruction()
        newInstr.opcode = code

        newInstr.mnemonic = details['mnemonic']
        newInstr.length = details['length']
        newInstr.cycles = details['cycles']
        newInstr.flags = details['flags']
        newInstr.addr = details['addr']
        newInstr.group = details['group']
        newInstr.operandOne = details.get('operand1')
        newInstr.operandTwo = details.get('operand2')
        instructions.append(newInstr)
    for code, details in data['cbprefixed'].items():
        newInstr = instruction()
        newInstr.opcode = code

        newInstr.mnemonic = details['mnemonic']
        newInstr.length = details['length']
        newInstr.cycles = details['cycles']
        newInstr.flags = details['flags']
        newInstr.addr = details['addr']
        newInstr.group = details['group']
        newInstr.operandOne = details.get('operand1')
        newInstr.operandTwo = details.get('operand2')
        instructionPrefixed.append(newInstr)

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

root = tk.Tk()
root.geometry("500x500")
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=20)





# Keep track of the currently displayed instruction
current_index = 0
prefixed = tk.IntVar()


def display_instruction(index):
    global current_index, prefixed
    current_index = index
    if prefixed.get() == 1:
        instruction = instructionPrefixed[index]
    else:
        instruction = instructions[index]
    text = f"""
    Opcode: {instruction.opcode}
    Mnemonic: {instruction.mnemonic}
    Length: {instruction.length}
    Cycles: {instruction.cycles}
    Flags: {instruction.flags}
    Addr: {instruction.addr}
    Group: {instruction.group}
    Operand One: {instruction.operandOne}
    Operand Two: {instruction.operandTwo}
    """
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, text)

def search_opcode():
    opcode = "0x" + opcode_entry.get()
    for index, instruction in enumerate(instructions):
        if instruction.opcode == opcode:
            display_instruction(index)
            return
    messagebox.showinfo("Error", "Opcode not found")

def next_instruction():
    global current_index
    if current_index < len(instructions) - 1:
        display_instruction(current_index + 1)
    else:
        messagebox.showinfo("Error", "No next instruction")

def previous_instruction():
    global current_index
    if current_index > 0:
        display_instruction(current_index - 1)
    else:
        messagebox.showinfo("Error", "No previous instruction")

def update():
    global current_index
    display_instruction(current_index)

# Sort instructions by opcode
instructions.sort(key=lambda instr: int(instr.opcode, 16))

search_frame = tk.Frame(root)
search_frame.pack(side=tk.TOP, fill=tk.X)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(side=tk.TOP, fill=tk.X)

opcode_label = tk.Label(search_frame, text="0x")
opcode_label.pack(side=tk.LEFT)

opcode_entry = tk.Entry(search_frame)
opcode_entry.pack(side=tk.LEFT)

previous_button = tk.Button(button_frame, text="Previous", command=previous_instruction)
previous_button.pack(side=tk.LEFT)

search_button = tk.Button(button_frame, text="Search", command=search_opcode)
search_button.pack(side=tk.LEFT)

next_button = tk.Button(button_frame, text="Next", command=next_instruction)
next_button.pack(side=tk.LEFT)

c1 = tk.Checkbutton(checkbox_frame, text='prefixed',variable=prefixed, onvalue=1, offvalue=0, command=update)
c1.pack()

result_text = tk.Text(root, font=('Helvetica', '20'))
result_text.pack()
root.after_idle(update)
root.mainloop()
