import tkinter as tk
from tkinter import filedialog
import shutil

class PhotoUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Uploader")

        self.select_button = tk.Button(self.root, text="Selecionar Foto", command=self.select_photo)
        self.select_button.pack()

    def select_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        
        if file_path:
            # Defina o caminho da pasta onde deseja salvar a foto dentro do banco de dados
            database_photo_folder = "caminho/para/sua/pasta/no/banco/de/dados"

            # Mova o arquivo selecionado para a pasta no banco de dados
            shutil.copy(file_path, database_photo_folder)

            print("Foto movida para a pasta do banco de dados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoUploaderApp(root)
    root.mainloop()
