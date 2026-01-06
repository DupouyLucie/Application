import flet as ft

def main(page: ft.Page) :
    page.title= "Visualisation de l'Algorithme"
    page.theme_mode= ft.ThemeMode.LIGHT
    page.padding=20
    title=ft.Text("Visualisation de l'Algorithme", size=24, weight="bold")
    button=ft.ElevatedButton("Cliquez-moi", on_click=lambda e: print("test"))
    page.add(ft.Column([title,button]))
 
    
ft.app(target=main)