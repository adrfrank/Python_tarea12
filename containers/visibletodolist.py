from components import TodoList
from store import store
from kivy.factory import Factory
from actions import toggle_todo

def get_visible_todos(todos, vis_filter):
    if vis_filter == 'SHOW_ALL':
        return todos
    elif vis_filter == 'SHOW_COMPLETED':
        return filter(lambda x: x['completed'], todos)
    elif vis_filter == 'SHOW_ACTIVE':
        return filter(lambda x: not x['completed'], todos)

def map_state_to_props(state, widget):
    return {'todos': get_visible_todos(state['todos'], 
                                       state['visibility_filter'])}

def map_dispatch_to_props(dispatch, widget):
    return {'assign': {
                'item_callback': lambda t_id: dispatch(toggle_todo(t_id))
                }
        }

VisibleTodoList = store.connect(map_state_to_props, map_dispatch_to_props,
                                TodoList)
Factory.register('VisibleTodoList', VisibleTodoList)
