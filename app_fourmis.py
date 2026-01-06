import flet as ft
import random
import math 

def main(page: ft.Page) :
    page.title= "Visualisation de l'Algorithme"
    page.theme_mode= ft.ThemeMode.LIGHT
    page.padding=20
    title=ft.Text("Visualisation de l'Algorithme", size=24, weight="bold")
    button=ft.ElevatedButton("Cliquez-moi", on_click=lambda e: print("test"))
    page.add(ft.Column([title,button]))

def main_2(page: ft.Page) :
    page.title= "Visualisation de l'Algorithme"
    page.theme_mode= ft.ThemeMode.LIGHT
    page.padding=20
    title=ft.Text("Paramètres de l'algorithme", size=24, weight="bold")
    nodes_field=ft.TextField(label="Nombre de noeuds", value="20", width=150)
    Nb_fourmis=ft.TextField(label="Nombre de fourmis", value="15", width=150)
    Nb_iterations=ft.TextField(label="Nombre d'itérations", value="100", width=150)
    graph_container=ft.Container(width=600, height=500, bgcolor="lightblue", border=ft.border.all(2, "blue"))
    texte=ft.Text("Prêt à démarrer", size=16, color="green")
    sep=ft.Divider()
    nodes=[]

    def generer_nodes():
        n=int(nodes_field.value)
        for _ in range(n):
            x=random.uniform(50,550)
            y=random.uniform(50,450)
            nodes.append([x,y])
        print(nodes)
        dessiner_graph()


    def dessiner_graph():
        shapes= []
        for i in range(len(nodes)):
            x,y=nodes[i]
            rond=ft.Container( width=20, height=20,left=x-10, top=y-10, content=ft.Text(str(i), size=10, color="white"),alignment=ft.Alignment(0,0),bgcolor="green")
            shapes.append(rond)
        graph_container.content=ft.Stack(controls=shapes, width=600, height=500)
        page.update()
    button=ft.Button("Generer le Gaphe", on_click=lambda e: generer_nodes())
    page.add(ft.Column([title,ft.Row([nodes_field,Nb_fourmis,Nb_iterations]), button, sep,texte,graph_container]))


    


ft.run(main_2)