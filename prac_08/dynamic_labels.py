from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self):
        """Construct main app."""
        super().__init__()
        # model to create app
        self.names = ("John Smith", "Jane Doe", "John Smithson")

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        """Creates widgets from a list."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.font_size = 30
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
