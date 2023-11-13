import flet as ft
import math
import statistics
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    
    c1 = ft.Column()
     
    pesos = [50.3, 50.5, 50.8, 51.3, 51.7, 51.3, 51.1, 51.4, 51.3, 51.6, 50.2, 50.5, 50.7, 50.0, 51.1, 50.4, 50.6, 51.2, 50.4, 50.8, 50.2, 50.6, 51.2, 50.4, 50.8, 50.2, 50.6, 49.4, 49.6, 50.8, 49.9, 50.4, 50.1, 51.0, 49.3, 49.5, 49.1, 50.9, 49.6, 49.8, 49.5, 49.7, 50.0, 51.1, 49.7, 50.3, 50.4, 50.8, 49.9, 51.7, 50.0, 50.2, 49.2, 49.1, 49.2, 51.1, 50.8, 49.7, 50.5, 50.4, 49.5, 49.7, 50.5, 50.3, 50.0, 50.1, 49.1, 51.4, 50.9, 49.1, 50.6, 50.4, 50.6, 49.7, 49.2, 50.1, 49.9, 49.6, 50.7, 49.3, 50.2, 50.7, 49.3, 49.3, 50.3, 49.1, 49.9, 49.8, 50.3, 50.1, 50.5, 49.5, 50.8, 50.0, 50.7, 50.5, 49.4, 50.7, 49.1, 50.8, 50.6, 49.1, 49.3]
    
    data_input=ft.TextField(label=str(pesos))
    
    # Calcula la suma de los elementos del grupo de datos
    suma = sum(pesos)

    #Numero de n elementos en el grupo de datos
    longitud = len(pesos)
    
    # Calcula la media aritmetica del grupo de datos
    media = suma/longitud

    # Calcula la moda
    moda = statistics.mode(pesos)
    #calcula la mediana
    mediana = statistics.median(pesos)

    # Calcula la suma de los cuadrados de las diferencias
    suma_cuadrados_diferencias = sum((x - media) ** 2 for x in pesos)

    # Calcula la varianza
    varianza = suma_cuadrados_diferencias / len(pesos)

    # Calcula la desviacion estandar
    desviacion_estandar = math.sqrt(varianza)

    dlg = ft.AlertDialog(
        title=ft.Text("Estadística Descriptiva"), on_dismiss=lambda e: print("Dialog dismissed!"),
        content=ft.Text("Moda: " + str(moda) + "\n" + "Media: " + str(media) + 
                        "\n" + "Varianza: " + str(varianza) + "\n" + "Desviacion Estandar: " + str(desviacion_estandar) + 
                        "\n" + "Mediana: " + str(mediana) +
                        "\n" + "Suma: " + str(suma) + "\n" + "Longitud: " + str(len(pesos)) + "\n" + "Datos: " + str(pesos)),

    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

         
        

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()



    def btn_click(e):
        fig, ax = plt.subplots()
        fig.set_visible(True)
        fig.set_dpi(100)
        ax.hist(pesos, bins=15, color='orange')
        ax.set_title('Distribución de Pesos de Cupcakes')
        ax.set_xlabel('Pesos (g)')
        ax.set_ylabel('Frecuencia')
        '''
        c1.controls.clear()
        c1.controls.append(ft.Text("Estadística Descriptiva"  ))
        c1.controls.append(ft.Text("Suma: " + str(suma) ))
        c1.controls.append(ft.Text("Longitud: " + str(len(pesos)) ))
        c1.controls.append(ft.Text("Moda: " + str(moda) ))
        c1.controls.append(ft.Text("Media: " + str(media) ))
        c1.controls.append(ft.Text("Varianza: " + str(varianza) ))
        c1.controls.append(ft.Text("Desviacion Estandar: " + str(desviacion_estandar) ))
        '''
        print("La suma del  grupo de datos:   es: ", str(suma))
        print("La longitud del grupo de datos:   es: ", str(len(pesos)))
        print("La moda del grupo de datos:   es: ", str(moda))
        print("La media del grupo de datos:    es: ", str(media))
        print("La varianza del grupo de datos:   es: ", str(varianza))
        print("La desviacion estandar del grupo de datos:    es: ", str(desviacion_estandar))

        open_dlg(e)

        page.add(MatplotlibChart(fig, expand=True))
    
        page.update()
         

    page.add(
        ft.Text("Datos:"+str(pesos)),
        c1,
        ft.ElevatedButton("Obtener Estadistica Descriptiva!", 
        on_click=btn_click) ,
       # ft.ElevatedButton("Obtener Histograma!",on_click=open_dlg_modal) ,
    )

ft.app(target=main)


