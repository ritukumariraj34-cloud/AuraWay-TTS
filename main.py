import flet as ft
import urllib.parse

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
    
    # 1. Create Flet's Native Audio player control
    audio_player = ft.Audio(autoplay=False)
    page.overlay.append(audio_player) # Overlay handles background elements

    def baak(e):
        if inp.value.strip():
            # Encode text to be URL safe
            encoded_text = urllib.parse.quote(inp.value.strip())
            # Use Google's free TTS stream URL
            tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q={encoded_text}"
            
            # Point the player to the generated audio stream and play it
            audio_player.src = tts_url
            audio_player.update()
            audio_player.play()

    bt = ft.FilledButton("Speak", width=200, on_click=baak, height=50)
    
    page.add(inp, bt)

if __name__ == "__main__":
    ft.run(main)
    
