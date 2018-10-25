import tkinter as tk


def open_message():
    message = tk.Toplevel(root, bg = "light green")
    message.minsize(300, 400)

    keys = 'QWERTYUIOPASDFGHJKLZXCVBNM'

    # frames for the keyboard
    keyboard = tk.Frame(message, bg = "light green")
    row1 = tk.Frame(keyboard)
    row2 = tk.Frame(keyboard)
    row3 = tk.Frame(keyboard)

    row1.pack()
    row2.pack()
    row3.pack()

    # Dynamically creates each button
    # position of button depends on key index
    # using index the button is assinged to the relative row
    # this only includes letters. To add more, add to keys string
    # and change the values to determine the assigned row
    for idx, letter in enumerate(keys):
        if idx < 10:
            btn = tk.Button(row1, text=letter, command=lambda i=idx: get_letter(i))
        elif idx < 19:
            btn = tk.Button(row2, text=letter, command=lambda i=idx: get_letter(i))
        else:
            btn = tk.Button(row3, text=letter, command=lambda i=idx: get_letter(i))

        btn.pack(side = tk.LEFT)


    to_frame = tk.Frame(message, bg = "light green", padx = 40)
    send_frame = tk.Frame(message, bg = "light green", padx = 40)

    tk.Label(to_frame, text="To:", bg="maroon", fg="light green", relief = tk.RAISED).\
                       pack(side = tk.LEFT, ipady = 3)

    recip = tk.Entry(to_frame)
    recip.pack(side = tk.LEFT, fill = tk.BOTH, expand=True)

    chat = tk.Entry(send_frame)
    chat.pack(side = tk.LEFT, fill = tk.BOTH, expand=True)

    send = tk.Button(send_frame, text="send", bg="maroon", fg="light green")
    send.pack(side = tk.LEFT)

    to_frame.pack(fill = tk.X, expand=True)
    # I imagine your text widget would be packed here
    keyboard.pack()
    send_frame.pack(fill = tk.X, expand=True)

    # Nested function to print values using keys
    def get_letter(i):
        # will print the letter depending on the button pressed
        print(keys[i])

root = tk.Tk()

button = tk.Button(root,text="sample", command = open_message)
button.pack()

root.mainloop()