from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class CanteenApp(MDApp):
    
    _owner_mesazze = "Jaldi Jaldi Khana Bamao Tumhari Maka Chodon 😙"

    def build(self):
        self.theme_cls.theme_style = "Dark"  # Dark theme for app
        
        screen = MDScreen()
        screen.add_widget(
            MDLabel(
                text=self._owner_mesazze,
                halign="center")
        )


CanteenApp().run()
