# Please install required libraries with: pip install tk pydub
import os
from tkinter import Tk, Label, Button, filedialog
from pydub import AudioSegment

class RingtoneConverter:
    def __init__(self, master):
        self.master = master
        master.title("Arlen's Ringtone Converter")

        self.label = Label(master, text="Select an MP3 file")
        self.label.pack()

        self.select_button = Button(master, text="Select MP3", command=self.select_mp3)
        self.select_button.pack()

        self.convert_button = Button(master, text="Convert to Ringtone", command=self.convert_to_ringtone)
        self.convert_button.pack()

    def select_mp3(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.mp3_path = file_path
            self.label.config(text=f"Selected MP3 file: {os.path.basename(self.mp3_path)}")

    def convert_to_ringtone(self):
        if hasattr(self, 'mp3_path'):
            mp3_file = AudioSegment.from_mp3(self.mp3_path)
            m4r_file = os.path.splitext(self.mp3_path)[0] + ".m4r"
            mp3_file.export(m4r_file, format="mp4")  # Change format to mp4
            self.label.config(text=f"Conversion complete! Ringtone saved as {os.path.basename(m4r_file)}")
        else:
            self.label.config(text="Please select an MP3 file first")


if __name__ == "__main__":
    root = Tk()
    app = RingtoneConverter(root)
    root.mainloop()
