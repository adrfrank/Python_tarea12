from components import Link
from actions import set_visibility_filter as set_vis_fil
from store import store
from kivy.factory import Factory

def map_state_to_props(state, widget):
    if widget.vis_filter == state['visibility_filter']:
        return {'state': 'down'}
    else:
        return {'state': 'normal'}

def map_dispatch_to_props(dispatch, widget):
    return {'bind': {
                'on_release': lambda i: dispatch(
                                        set_vis_fil(widget.vis_filter)),
                }
            }


FilterLink = store.connect(map_state_to_props, map_dispatch_to_props, Link)
Factory.register('FilterLink', FilterLink)
