from tkinter import filedialog as fd

def open_file_selection()-> str:
    filetypes = (
        ("Audio files", "*.ogg"),
        ("Audio files", "*.wav"),
        ("Audio files", "*.mp3"),
        )
    file = fd.askopenfilename(filetypes=filetypes)
    print(file)
    return file