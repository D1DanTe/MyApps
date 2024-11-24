from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.theme = 'light'  # Текущая тема

        # История вычислений
        self.history_layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1, 0.3))
        self.scroll_view.add_widget(self.history_layout)
        self.add_widget(self.scroll_view)

        # Поле ввода
        self.result = TextInput(font_size=32, readonly=True, halign='right', size_hint_y=0.2)
        self.add_widget(self.result)

        # Кнопки
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],
            ['History', 'Theme']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=24, on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)

    def on_button_press(self, instance):
        text = instance.text

        if text == 'C':
            self.result.text = ''
        elif text == '=':
            try:
                calculation = str(eval(self.result.text))
                self.add_to_history(f"{self.result.text} = {calculation}")
                self.result.text = calculation
            except Exception:
                self.result.text = 'Error'
        elif text == 'History':
            self.scroll_view.visible = not self.scroll_view.visible
        elif text == 'Theme':
            self.switch_theme()
        else:
            self.result.text += text

    def add_to_history(self, calculation):
        label = Label(text=calculation, size_hint_y=None, height=30, halign='left', valign='middle')
        label.bind(size=label.setter('text_size'))
        self.history_layout.add_widget(label)

    def switch_theme(self):
        self.theme = 'dark' if self.theme == 'light' else 'light'
        bg_color = [0.1, 0.1, 0.1, 1] if self.theme == 'dark' else [1, 1, 1, 1]
        self.result.background_color = bg_color


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()