from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty

class Link(ToggleButton):
    vis_filter = StringProperty(None)

    def on_vis_filter(self, instance, value):
        options = {'SHOW_ALL': 'Todos', 'SHOW_ACTIVE': 'Activos',
                   'SHOW_COMPLETED': 'Completados'}
        self.text = options[value]

    def on_touch_down(self, touch):
        if self.state == 'down':
            return False
        else:
            super(Link, self).on_touch_down(touch)
