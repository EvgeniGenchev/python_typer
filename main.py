import py_cui

counter = 0
lw = ""
txt_s = "Some random words that you should write"
txt = txt_s.split(" ")
size = len(txt)

def get_input():
    global inp, out, txt, lw, counter, size
    ti = inp.get()
    inp.clear()
    if ti.startswith("\n"):
        ti = ti[1:]
    
    if ti.strip() == txt[0].strip():
        txt = txt[1:]
        out.set_text(" ".join(txt))
        counter += 1
        lw = ""
    else:
        lw = ti
        out.set_text(f"needed:{txt[0]} \n written: {ti}")    
    
    inp.set_text("")

    if counter == size:
        exit(0)


def edit_input():
    global lw, inp
    if (len(inp.get().strip()) == 0) and len(lw):
        inp.set_text(lw)


root = py_cui.PyCUI(5,5, auto_focus_buttons=False)
root.set_title('Ptyter')
inp = root.add_text_block(title="Input", row=0, column_span=5, column=0, initial_text="Enter text here!")
out = root.add_text_block(title="Text to write", row=1, row_span=4, column_span=5, column=0, initial_text=txt_s)

inp.add_key_command(py_cui.keys.KEY_SPACE, get_input)
inp.add_key_command(py_cui.keys.KEY_ENTER, get_input)
inp.add_key_command(py_cui.keys.KEY_BACKSPACE, edit_input)

root.start()
