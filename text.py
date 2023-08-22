import tkinter as tk

class AppMain:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo Principal")

        # Crie um frame para conter o botão redondo
        self.button_frame = tk.Frame(self.root, background='#023535')
        self.button_frame.place(relx=0.9, rely=0.9, anchor="center")

        # Crie um botão redondo usando um label com fundo circular
        self.close_button = tk.Label(self.button_frame, text="Fechar", font=("Inter", 10), relief="ridge", background="#D8FFDB")
        self.close_button.pack(ipadx=10, ipady=5, padx=10, pady=5, anchor="center")
        self.close_button.bind("<Button-1>", self.close_app)

    def close_app(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMain(root)
    root.mainloop()
