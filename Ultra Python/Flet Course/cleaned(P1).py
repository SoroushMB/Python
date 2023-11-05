import flet as ft
import datetime as ti
import psutil

def main(page: ft.Page):
    
    page.theme_mode = (ft.ThemeMode.SYSTEM)
    
    def btn_click(e):
        greetings.controls.append(ft.Text(f"Battery : {psutil.sensors_battery()}",font_family="JetBrains Mono",size=12))
        with open(file="test.txt",mode="w",encoding="utf-8") as file:
            file.write(f"{first_name.value} has logged in {ti.date.today()}")
        first_name.value = ""
        last_name.value = ""
        first_name.label = "Enter again"
        last_name.label = "Enter again"
        page.update()
        first_name.focus()

    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greeting_btn = ft.FloatingActionButton(icon=ft.icons.ASSIGNMENT_RETURNED_OUTLINED,on_click=btn_click,bgcolor=ft.colors.YELLOW_ACCENT_400,width=65)
    greetings = ft.Column()

    page.add(first_name,last_name,greeting_btn,greetings)

ft.app(target=main)