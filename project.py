from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class CanteenApp(MDApp):

    # Friendly mesazze from none other than the owner itself 😲
    _owner_mesazze = "Jaldi Jaldi Khana Banao Tumhari Maka Chodon 😙"

    def build(self):
        # Theming
        self.theme_cls.theme_style = "Dark"  # Dark theme for app
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "300"

        # Initialise and add widget to screen
        screen = MDScreen()
        screen.add_widget(
            MDLabel(
                text=self._owner_mesazze,
                halign="center")
        )

if __name__ == '__main__':
    CanteenApp().run()
