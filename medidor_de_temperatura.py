import tkinter as tk
from tkinter import ttk

# Clase para el conversor de temperatura
class TransTemperatura:
    def __init__(self, root):
        self.root = root
        self.root.title('Transformador de temperatura')

        self.valor_temp = tk.DoubleVar()
        self.unidad_entrada = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entrada de la temperatura
        tk.Label(self.root, text="Ingrese la temperatura:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.valor_temp).grid(row=0, column=1)

        # Menú para seleccionar la unidad de entrada
        tk.Label(self.root, text="Unidad de entrada:").grid(row=1, column=0)
        opciones = ["Kelvin", "Celsius", "Fahrenheit"]
        tk.OptionMenu(self.root, self.unidad_entrada, *opciones).grid(row=1, column=1)

        # Botón para convertir
        tk.Button(self.root, text="Convertir", command=self.convertir).grid(row=2, column=0, columnspan=2)

        # Salidas
        tk.Label(self.root, text="Temperatura en Celsius:").grid(row=3, column=0)
        self.salida_celsius = tk.Label(self.root, text="")
        self.salida_celsius.grid(row=3, column=1)

        tk.Label(self.root, text="Temperatura en Fahrenheit:").grid(row=4, column=0)
        self.salida_fahrenheit = tk.Label(self.root, text="")
        self.salida_fahrenheit.grid(row=4, column=1)

        tk.Label(self.root, text="Temperatura en Kelvin:").grid(row=5, column=0)
        self.salida_kelvin = tk.Label(self.root, text="")
        self.salida_kelvin.grid(row=5, column=1)

    def convertir(self):
        try:
            valor = self.valor_temp.get()
            unidad = self.unidad_entrada.get()

            if unidad == "Kelvin":
                celsius = valor - 273.15
                fahrenheit = (valor - 273.15) * 9 / 5 + 32
                kelvin = valor
            elif unidad == "Celsius":
                celsius = valor
                fahrenheit = valor * 9 / 5 + 32
                kelvin = valor + 273.15
            elif unidad == "Fahrenheit":
                celsius = (valor - 32) * 5 / 9
                fahrenheit = valor
                kelvin = (valor - 32) * 5 / 9 + 273.15
            else:
                celsius = fahrenheit = kelvin = 0  # Por si no se selecciona una unidad válida

            self.salida_celsius.config(text=f"{celsius:.2f} °C")
            self.salida_fahrenheit.config(text=f"{fahrenheit:.2f} °F")
            self.salida_kelvin.config(text=f"{kelvin:.2f} K")
        except Exception as e:
            self.salida_celsius.config(text="Error")
            self.salida_fahrenheit.config(text="Error")
            self.salida_kelvin.config(text="Error")

# Lógica principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TransTemperatura(root)
    root.mainloop()

