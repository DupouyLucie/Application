import flet as ft

# def main(page: ft.Page) :
#     page.title= "Visualisation de l'Algorithme"
#     page.theme_mode= ft.ThemeMode.LIGHT
#     page.padding=20
#     title=ft.Text("Visualisation de l'Algorithme", size=24, weight="bold")
#     button=ft.ElevatedButton("Cliquez-moi", on_click=lambda e: print("test"))
#     page.add(ft.Column([title,button]))

def main(page: ft.Page) :
    page.title= "Visualisation de l'Algorithme"
    page.theme_mode= ft.ThemeMode.LIGHT
    page.padding=20
    title=ft.Text("Paramètres de l'algorithme", size=24, weight="bold")
    Nb_noeuds=ft.TextField(label="Nombre de noeuds", value="20", width=150)
    Nb_fourmis=ft.TextField(label="Nombre de fourmis", value="15", width=150)
    Nb_iterations=ft.TextField(label="Nombre d'itérations", value="100", width=150)
    Zone_graphique=ft.Container(width=600, height=500, bgcolor="lightblue", border=ft.border.all(2, "blue"))
    texte=ft.Text("Prêt à démarrer", size=16, color="green")
    sep=ft.Divider()
    page.add(ft.Column([title,ft.Row([Nb_noeuds,Nb_fourmis,Nb_iterations]),sep,texte,Zone_graphique]))

    
ft.app(target=main)