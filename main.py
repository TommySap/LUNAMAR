import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import pandas as pd
import requests

# URL de Google Sheets publicado (actualiza con tu propio enlace)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfTvml_JigGWIZhSsqEL-juvOJN5FeZGkmnv-vLKrVdq6TTh9ysp3u4zaoHCZRjFYlsLzswQkFqP67/pub?output=csv"

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Cargando datos...')
        self.layout.add_widget(self.label)
        Clock.schedule_interval(self.update_data, 10)  # Actualiza cada 10 segundos
        return self.layout

    def update_data(self, dt):
        try:
            # Verifica la conexión antes de intentar descargar los datos
            response = requests.get(sheet_url)
            if response.status_code == 200:
                # Obtener los datos de Google Sheets
                data = pd.read_csv(sheet_url)
                if not data.empty:
                    info = "\n".join([f"Nombre: {row['Nombre']}\nUbicación: {row['Ubicación']}\nRuta: {row['Ruta']}" for _, row in data.iterrows()])
                    self.label.text = info
                else:
                    self.label.text = "No hay datos disponibles."
            else:
                self.label.text = "No se pudo acceder a los datos. Verifica la URL."
        except Exception as e:
            self.label.text = f"Error al obtener datos: {str(e)}"

if __name__ == '__main__':
    MyApp().run()