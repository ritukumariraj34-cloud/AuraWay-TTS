import flet as ft
from jnius import autoclass

def main(page: ft.Page):
    page.title = "AuraWay TTS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1A1C1E"
    
    page.theme = ft.Theme(color_scheme_seed="#00e676")
    page.appbar = ft.AppBar(
        title=ft.Text("AuraWay TTS", weight="bold", color="white"),
        center_title=True,
        bgcolor="#00e676"
    )
    
    inp = ft.TextField(label="Enter the text here", multiline=True)

    # --- NATIVE OFFLINE JAVA TTS SETUP VIA PYJNIUS ---
    # 1. Import necessary Android Java classes
    Locale = autoclass('java.util.Locale')
    # Flet's underlying Android activity hook is org.smartek.serious_python.PythonActivity
    PythonActivity = autoclass('org.smartek.serious_python.PythonActivity')
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    
    # 2. Instantiate the on-device TTS Engine using the app's current context
    # Passing None for the listener parameter is perfectly fine for basic speech execution
    tts_engine = TextToSpeech(PythonActivity.mActivity, None)
    
    # 3. Force the engine language to English (or use Locale.CHINESE, etc.)
    tts_engine.setLanguage(Locale.US)
    # -------------------------------------------------

    def baak(e):
        if inp.value.strip():
            # Call Android's native speak method directly
            # TextToSpeech.QUEUE_FLUSH clears previous spoken phrases immediately
            tts_engine.speak(inp.value.strip(), TextToSpeech.QUEUE_FLUSH, None, None)

    bt = ft.FilledButton("Speak", width=200, on_click=baak, height=50)
    page.add(inp, bt)

if __name__ == "__main__":
    ft.run(main)
    
