from code_engine import MorseDictionary
from tkinter import *
from tkinter import ttk
from morse_player import MorsePlayer
from threading import Thread

morse = MorseDictionary()
m_player = MorsePlayer()
ui_font = ('Terminal', 16)
answer_font = ('Tekton Pro', 20, 'bold')


class MorseUi:
    def __init__(self):
        def clipboard_copy():
            self.window.clipboard_clear()
            self.window.clipboard_append(self.answer.cget('text'))

        def show_morse():
            stop_player()
            if len(self.input.get()) > morse.MAX_INPUT:
                self.answer_message.config(text=f"Message too long! Must be shorter than {str(morse.MAX_INPUT)} characters.")
                self.copy_btn.grid_remove()
                self.m_play_btn.grid_remove()
                self.answer_message.grid(row=3, column=0)
                self.answer.config(text="")
                return
            self.answer.config(text=f"{morse.coded_msg}")
            self.answer_message.config(text="Coded message:   ")
            self.answer_message.grid(row=3, column=0)
            self.copy_btn.grid(row=3, column=2)
            self.m_play_btn.grid(row=3, column=3)

        def show_decoded():
            self.answer.config(text=f"{morse.decoded_msg}")
            self.answer_message.config(text="Decoded message:   ")
            self.answer_message.grid(row=3, column=0)
            self.copy_btn.grid(row=3, column=2)

        def change_drctn():
            self.direction *= -1
            if self.direction == -1:
                self.action_btn.config(text="Decode", command=lambda: [morse.decoder(self.input.get()), show_decoded()])
                self.ui_message.config(text="Please enter Morse to decode:   ")
                self.answer.config(text="")
                self.copy_btn.grid_remove()
                self.m_play_btn.grid_remove()
                self.answer_message.grid_remove()
                self.input.delete(0, 'end')
                self.direction_label.config(text="Text  ⇦  Morse")
                stop_player()
            elif self.direction == 1:
                self.action_btn.config(text="Encode", command=lambda: [morse.coder(self.input.get()), show_morse()])
                self.ui_message.config(text="Please enter message to encode:   ")
                self.answer.config(text="")
                self.copy_btn.grid_remove()
                self.m_play_btn.grid_remove()
                self.answer_message.grid_remove()
                self.input.delete(0, 'end')
                self.direction_label.config(text="Text  ⇨  Morse")
                stop_player()

        def color_answer(index):
            self.answer_colored.config(text=f"{morse.coded_msg[:index]}", foreground='red')

        def morse_player():
            if not m_player.run:
                self.m_play_btn.config(text="⏹️", command=stop_player)
                m_player.play_code(code=morse.coded_msg, code_highlight=color_answer)
                self.answer_colored.config(text="")

        def stop_player():
            m_player.run = False
            self.m_play_btn.config(text="▶️", command=sound_thread)
            self.answer_colored.config(text="")

        def sound_thread():
            thread = Thread(target=morse_player)
            thread.start()

        # Window elements init
        self.window = Tk()
        self.window.title("Morse Code Encoder/Decoder")
        self.window.minsize(950, 200)
        self.window.maxsize(950, 200)
        self.window.config(padx=40, pady=20)

        # Center main window
        self.window.update_idletasks()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        size = tuple(int(_) for _ in self.window.geometry().split('+')[0].split('x'))
        x = screen_width / 2 - size[0] / 2
        y = screen_height / 2 - size[1] / 2
        self.window.geometry("+%d+%d" % (x, y))

        # Ui window layout Frames
        self.frame1 = ttk.Frame(self.window, padding=10)
        self.frame1.grid()
        self.frame2 = ttk.Frame(self.window)
        self.frame2.grid()

        # Frame 1

        self.action_btn = ttk.Button(self.frame1, text="Encode", command=lambda: [morse.coder(self.input.get()), show_morse()])
        self.ui_message = ttk.Label(self.frame1, text="Please enter message to encode:   ", width=25, font=ui_font)
        self.direction_btn = ttk.Button(self.frame1, text="Change Direction", command=change_drctn)
        self.direction = 1
        self.direction_label = ttk.Label(self.frame1, text="Text  ⇨  Morse", font=ui_font)
        self.input = ttk.Entry(self.frame1, width=50)

        # Frame 2
        self.answer = ttk.Label(self.frame2, text="", font=answer_font)
        self.answer_colored = ttk.Label(self.frame2, text="", font=answer_font)
        self.answer_message = ttk.Label(self.frame2, text="", font=ui_font)
        self.copy_btn = ttk.Button(self.frame2, text="📋", width=2, command=clipboard_copy)
        self.m_play_btn = ttk.Button(self.frame2, text="▶️", width=2, command=sound_thread)

        # Griding elements
        self.direction_label.grid(row=0, column=0)
        self.direction_btn.grid(row=0, column=2)
        self.ui_message.grid(row=1, column=0)
        self.input.grid(row=1, column=1)
        self.action_btn.grid(row=2, column=0)
        self.answer.grid(row=3, column=1)
        self.answer_colored.grid(row=3, column=1)
        self.answer_colored.place(x=139, y=0)

        self.window.mainloop()


