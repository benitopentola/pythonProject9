import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import pypinyin
import pyperclip  # Importa pyperclip para interactuar con el portapapeles

def convertir_a_pinyin():
    texto_entrada = entrada_texto.get("1.0", tk.END)
    lineas_procesadas = []
    for linea in texto_entrada.splitlines():
        pinyin_linea = ' '.join(pypinyin.lazy_pinyin(linea))
        lineas_procesadas.append(pinyin_linea)
    texto_salida = '\n'.join(lineas_procesadas)
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert("1.0", texto_salida)

def copiar_todo():
    texto = salida_texto.get("1.0", tk.END)
    pyperclip.copy(texto)  # Copia el texto al portapapeles

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor Hanzi a Pinyin")

# Creación de los widgets
entrada_texto = ScrolledText(ventana, height=10, width=50)
entrada_texto.pack(pady=10)

boton_convertir = tk.Button(ventana, text="Convertir a Pinyin", command=convertir_a_pinyin)
boton_convertir.pack(pady=5)

salida_texto = ScrolledText(ventana, height=10, width=50)
salida_texto.pack(pady=10)

boton_copiar_todo = tk.Button(ventana, text="Copiar Todo", command=copiar_todo)  # Añade el botón para copiar
boton_copiar_todo.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
