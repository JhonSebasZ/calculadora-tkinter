import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('350x380')
        self.resizable(0,0)
        self.title('Calculadora')
        #self.iconbitmap('icono.ico')
        self.expresion = ''
        self.entrada = None
        self.entrada_text = tk.StringVar()
        self.crear_calculadora()
    
    def crear_calculadora(self):
        
        separador_frame = tk.Frame(height=10)
        separador_frame.pack()
        
        entrada_frame = tk.Frame(self, width=334, height=50, bg='white')
        entrada_frame.pack(side=tk.TOP)

        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_text, width=25, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)
        
        separador_frame = tk.Frame(height=15)
        separador_frame.pack()

        botones_frame = tk.Frame(self, width=300, height=450, bg='grey')
        botones_frame.pack()

        # Fila 1
        boton_limpiar = tk.Button(botones_frame, text='C', width='22', height=3, bg='white', cursor='hand2', command=self.Evento_limpiar)
        boton_limpiar.grid(row=0, columnspan=2, column=0,  padx=1, pady=1)
        
        boton_eliminar = tk.Button(botones_frame, text='<=', width='10', height=3, bg='White', cursor='hand2', command=self.Evento_eliminar)
        boton_eliminar.grid(row=0, column=2)

        boton_dividir = tk.Button(botones_frame, text='/', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click('/')).grid(row=0, column=3, padx=1, pady=1)

        #Fila 2
        boton_siete = tk.Button(botones_frame, text='7', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(7))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)

        boton_ocho = tk.Button(botones_frame, text='8', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(8))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)

        boton_nueve = tk.Button(botones_frame, text='9', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(9))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)

        boton_multiplicar = tk.Button(botones_frame, text='*', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)

        #Fila 3
        boton_cuatro = tk.Button(botones_frame, text='4', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        boton_resta = tk.Button(botones_frame, text='-', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click('-'))
        boton_resta.grid(row=2, column=3, padx=1, pady=1)

        #Fila 4
        boton_uno = tk.Button(botones_frame, text='1', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text='2', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        boton_suma = tk.Button(botones_frame, text='+', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)

        #Fila 5
        boton_cero = tk.Button(botones_frame, text='0', width='22', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click(0))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        boton_punto = tk.Button(botones_frame, text='.', width='10', height=3, bg='white', cursor='hand2', command=lambda:self.Evento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)

        boton_resultado = tk.Button(botones_frame, text='=', width='10', height=3, bg='white', cursor='hand2', command=self.Evento_resultado)
        boton_resultado.grid(row=4, column=3, padx=1, pady=1)

    def Evento_eliminar(self):
        self.expresion = self.expresion[:-1]
        self.entrada_text.set(self.expresion)

    def Evento_limpiar(self):
        self.expresion=''
        self.entrada_text.set(self.expresion)

    def Evento_click(self, elemento):
        self.expresion=f'{self.expresion}{elemento}'
        self.entrada_text.set(self.expresion)

    def Evento_resultado(self):
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_text.set(resultado)
                self.expresion = resultado
        except:
            messagebox.showerror('Error')
            self.expresion = ''
            self.entrada_text.set('')

llamar_calculadora = Calculadora()

llamar_calculadora.mainloop()