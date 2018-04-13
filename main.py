# -*- coding: utf-8 -*-
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
    TabbedPanel:
        do_default_tab: False
        
        TabbedPanelItem:
            text: 'Параметры'
            BoxLayout:
                orientation: 'vertical'
                GridLayout:
                    cols: 3
                    Button:
                        text: "Прихожая"
                    Button:
                        text: "Корридор"
                    Spinner:
                        text: "Мощность"
                        values: "60", "80", "100"
                        size_hint: (None, None)
                        size: (100, 44)
                GridLayout:
                    cols: 2
                    Button:
                        text: "Комната1"
                    Spinner:
                        text: "Мощность"
                        values: "60", "80", "100"
                        size_hint: (None, None)
                        size: (100, 44)
                    Button:
                        text: "Комната2"
                    Spinner:
                        text: "Мощность"
                        values: "60", "80", "100"
                        size_hint: (None, None)
                        size: (100, 44)
                
        
        TabbedPanelItem:
            text: 'Мониторинг'
            BoxLayout:
        
        TabbedPanelItem:
            text: 'Расписание'
            BoxLayout:
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
