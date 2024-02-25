import tkinter as tk

class VoiceAssistantApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Assistant")

        self.label = tk.Label(master, text="Voice Assistant")
        self.label.pack(pady=10)

        self.text_area = tk.Text(master, height=10, width=50)
        self.text_area.pack()

        self.input_label = tk.Label(master, text="Enter command:")
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(master, width=40)
        self.input_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.process_command)
        self.submit_button.pack(pady=5)

    def process_command(self):
        command = self.input_entry.get()
        self.text_area.insert(tk.END, f"\nYou said: {command}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()
