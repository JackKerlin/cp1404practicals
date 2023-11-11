"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


CONVERSION_FACTOR = 1.609344

class MilesKmConversionApp(App):
    """Kivy app to convert miles to km"""

    def build(self):
        """ build the Kivy app """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value, increment_value):
        try:
            self.root.ids.input_miles.text = str(float(value) + increment_value)
        except ValueError:
            self.root.ids.input_miles.text = str(increment_value)
    def handle_conversion(self, value):
        try:
            result = float(value) * CONVERSION_FACTOR
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"


MilesKmConversionApp().run()
