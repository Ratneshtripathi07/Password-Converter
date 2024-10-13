import tkinter as tk
from tkinter import messagebox

# Custom dictionary for password conversion
password_dict = {
'q':'',
'w':'',
'e':'',
'r':'',
't':'',
'y':'',
'u':'',
'i':'',
'o':'',
'p':'',
'a':'',
's':'',
'd':'',
'f':'',
'g':'',
'h':'',
'j':'',
'k':'',
'l':'',
'z':'',
'x':'',
'c':'',
'v':'',
'b':'',
'n':'',
'm':'',
'Q':'',
'W':'',
'E':'',
'R':'',
'T':'',
'Y':'',
'U':'',
'I':'',
'O':'',
'P':'',
'A':'',
'S':'',
'D':'',
'F':'',
'G':'',
'H':'',
'J':'',
'K':'',
'L':'',
'Z':'',
'X':'',
'C':'',
'V':'',
'B':'',
'N':'',
'M':'',
'1':'',
'2':'',
'3':'',
'4':'',
'5':'',
'6':'',
'7':'',
'8':'',
'9':'',
'0':'',
'!':'',
'@':'',
'#':'',
'$':'',
'%':'',
'^':'',
'&':'',
'*':'',
'(':'',
')':'',
'_':'',
'+':'',
'=':'',
'{':'',
'}':'',
'[':'',
']':'',
':':'',
}

def convert_password():
    original_password = input_password.get()
    complex_password = ''.join(password_dict.get(char, char) for char in original_password)
    output_password.delete(0, tk.END)
    output_password.insert(0, complex_password)

def clear_fields():
    input_password.delete(0, tk.END)
    output_password.delete(0, tk.END)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_password.get())
    messagebox.showinfo("Copied", "Complex password fuckingg copied to clipboard!")

root = tk.Tk()
root.title("Password Converter")

# Input frame
input_frame = tk.Frame(root)
input_label = tk.Label(input_frame, text="Enter Password:")
input_label.pack(side=tk.LEFT)
input_password = tk.Entry(input_frame, width=30)
input_password.pack(side=tk.LEFT)
input_frame.pack(pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert Password", command=convert_password)
convert_button.pack(pady=10)

# Output frame
output_frame = tk.Frame(root)
output_label = tk.Label(output_frame, text="Complex Password:")
output_label.pack(side=tk.LEFT)
output_password = tk.Entry(output_frame, width=30)
output_password.pack(side=tk.LEFT)
output_frame.pack(pady=10)

# Additional buttons
button_frame = tk.Frame(root)
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)
copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=5)
button_frame.pack(pady=10)

root.mainloop()