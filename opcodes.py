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

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

# Keep track of the currently displayed instruction
current_index = -1

def display_instruction(index):
    global current_index
    current_index = index
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

# Sort instructions by opcode
instructions.sort(key=lambda instr: int(instr.opcode, 16))

root = tk.Tk()
root.geometry("800x400")
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=20)

opcode_label = tk.Label(root, text="0x")
opcode_label.pack(side=tk.LEFT)

opcode_entry = tk.Entry(root)
opcode_entry.pack(side=tk.LEFT)

previous_button = tk.Button(root, text="Previous", command=previous_instruction)
previous_button.pack(side=tk.LEFT)

search_button = tk.Button(root, text="Search", command=search_opcode)
search_button.pack(side=tk.LEFT)

next_button = tk.Button(root, text="Next", command=next_instruction)
next_button.pack(side=tk.LEFT)

result_text = tk.Text(root, font=('Helvetica', '20'))
result_text.pack()

root.mainloop()
