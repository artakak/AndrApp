'''
Demonstrates using kv language to create some simple buttons and a
label, with each button modifying the label text.
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_string('''
<MainWidget>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'some string '
            on_press: the_right_pane.text += self.text
        Button:
            text: 'one two three four '
            on_press: the_right_pane.text += self.text
        Button:
            text: 'follow the yellow brick road '
            on_press: the_right_pane.text += self.text
        Button:
            text: 'five six seven eight '
            on_press: the_right_pane.text += self.text
        Button:
            text: 'CLEAR LABEL'
            on_press: root.update_text()
        Label:
            id: txt_inpt
            text: app.text
    Label:
        id: the_right_pane
        text: ''
        text_size: self.size
        halign: 'center'
        valign: 'middle'
''')


class MainWidget(BoxLayout):
    txt_inpt = ObjectProperty(None)

    def update_text(self):
        print(self.ids["txt_inpt"].text)
        self.ids["txt_inpt"].text = "bla-bla"


class ExampleApp(App):
    text = "123"

    def build(self):
        return MainWidget()


ExampleApp().run()
