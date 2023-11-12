from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NEW_COLOUR = (0, 1, 1, 0.5)


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self):
        """Construct main app."""
        super().__init__()
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ("John Smith", "Jane Doe", "John Smith", "Jane Doe", "John Smith", "Jane Doe", "Yes")

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.background_color = NEW_COLOUR
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
