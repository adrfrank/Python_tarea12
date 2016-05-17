from kivy.uix.label import Label
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior

class Todo(ButtonBehavior, Label):
    release_callback = ObjectProperty(None)
    completed = BooleanProperty(False)
    t_id = NumericProperty(None)
