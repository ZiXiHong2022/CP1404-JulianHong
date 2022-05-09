
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_display = {"Hong ZiXi", "Julian", "Jun xiang wen"}

    def build(self):
        self.title = "Dynamic Label"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_display:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.main.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "{}".format(name, self.name_display)


DynamicWidgetsApp().run()
