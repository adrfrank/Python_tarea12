from kivy.uix.boxlayout import BoxLayout
from store import store
from actions import add_todo

class AddTodo(BoxLayout):
    
    def add_todo_callback(self):
        text_input = self.ids.text_input
        store.dispatch(add_todo(text_input.text))
        text_input.text = ''
