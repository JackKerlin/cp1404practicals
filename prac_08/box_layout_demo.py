from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build kivy app from file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def clear(self):
        """Clear output and input."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""

    def handle_greet(self):
        """Set output as greeting."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()
