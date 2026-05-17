import flet as ft
from plyer import tts

def main(page: ft.Page):
    page.title = "AuraWay TTS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    page.theme = ft.Theme(
        color_scheme_seed="#00e676"
    )
    page.appbar = ft.AppBar(
        title=ft.Text("AuraWay TTS", weight="bold", color="white"),
        center_title=True,
        bgcolor="#00e676"
    )
    
    inp = ft.TextField(label="Enter the text here", multiline=True)
    
    # Fixed function: It receives the event 'e' from Flet when clicked
    def baak(e):
        if inp.value:
            tts.speak(inp.value)

    # Fixed on_click: Pass the function name without parentheses ()
    bt = ft.FilledButton("Speak", width=200, on_click=baak, height=50)
    
    page.add(inp, bt)

if __name__ == "__main__":
    # Clean Flet launch syntax for modern 1.0 builds
    ft.run(main)
    