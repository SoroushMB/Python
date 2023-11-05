import flet as ft
import time as ti

def main(window: ft.Page):
    window.theme_mode = (ft.ThemeMode.LIGHT)
    first_txt = ft.Text(value="Hello, World!",
                        color="blue",
                        font_family="JetBrains Mono",
                        size=20)
    first_btn = ft.ElevatedButton(text="Say my name!")
    window.add(first_btn)
    window.controls.append(first_txt)
    # window.update()

    second_txt = ft.Text()
    window.add(second_txt)
    for i in range(10):
        second_txt.value = f"Step {i}"
        window.update()
        ti.sleep(1)

ft.app(target=main)
