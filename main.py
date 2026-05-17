import flet as ft
import pyttsx3

def main(page: ft.Page):
    page.title = "AuraWay TTS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    page.theme = ft.Theme(color_scheme_seed="#00e676")
    
    page.appbar = ft.AppBar(
        title=ft.Text("AuraWay TTS", weight="bold", color="white"),
        center_title=True,
        bgcolor="#00e676"
    )
    
    inp = ft.TextField(label="Enter the text here", multiline=True)
    
    def baak(e):
        if inp.value.strip():
            # Initialize the offline engine instance
            engine = pyttsx3.init()
            
            # Queue the text to speak
            engine.say(inp.value.strip())
            
            # Run the engine to speak immediately through the phone speakers
            engine.runAndWait()

    bt = ft.FilledButton("Speak", width=200, on_click=baak, height=50)
    
    page.add(inp, bt)

if __name__ == "__main__":
    ft.run(main)
    
