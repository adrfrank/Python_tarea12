from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.scrollview import ScrollView
from todo import Todo

class TodoList(ScrollView):
    todos = ListProperty([])
    item_callback = ObjectProperty(None)

    def on_todos(self, instance, value):
        container = self.ids.todos
        container.clear_widgets()
        for todo in value:
            container.add_widget(Todo(text=todo['text'], t_id=todo['t_id'],
                                      completed=todo['completed'],
                                      release_callback=self.item_callback,
                                      size_hint=(1.0, None), height=50))
