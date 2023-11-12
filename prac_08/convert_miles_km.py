"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.609344


class MilesKmConverterApp(App):
    """Kivy app to convert miles to km"""
    output_text = StringProperty()

    def build(self):
        """Build kivy app from file"""
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, text, increment_value):
        """Increment input text by some value"""
        miles = self.convert_to_float(text)
        self.root.ids.input_miles.text = str(miles + increment_value)

    def handle_conversion(self, text):
        """Set output as calculated result"""
        miles = self.convert_to_float(text)
        result = miles * CONVERSION_FACTOR
        self.output_text = str(result)

    @staticmethod
    def convert_to_float(text):
        """Convert the text to a float"""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesKmConverterApp().run()
