from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import subprocess

class DekoBoosterApp(App):
    def build(self):
        self.title = "Ultimate Game Booster"
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.title_label = Label(
            text="[b]ULTIMATE GAME BOOSTER 🚀[/b]",
            markup=True,
            font_size='22sp',
            halign='center'
        )
        layout.add_widget(self.title_label)
        
        self.status_label = Label(
            text="Status: Ready to optimize",
            font_size='16sp',
            halign='center'
        )
        layout.add_widget(self.status_label)
        
        self.boost_btn = Button(
            text="APPLY OPTIMIZATION",
            font_size='18sp',
            background_color=(0.1, 0.6, 0.2, 1)
        )
        self.boost_btn.bind(on_press=self.run_boost)
        layout.add_widget(self.boost_btn)
        
        return layout

    def run_boost(self, instance):
        try:
            subprocess.run(["sync"], shell=True)
            self.status_label.text = "[✔] OPTIMIZATION APPLIED SUCCESSFULLY!"
        except Exception as e:
            self.status_label.text = "[-] Optimization failed."

if __name__ == "__main__":
    DekoBoosterApp().run()
