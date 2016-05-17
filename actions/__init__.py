from action import Action

next_todo_id = 0

def add_todo(text):
    global next_todo_id
    action = Action('ADD_TODO', t_id=next_todo_id, text=text)
    next_todo_id += 1
    return action

def set_visibility_filter(vis_filter):
    return Action('SET_VISIBILITY_FILTER', vis_filter=vis_filter)

def toggle_todo(t_id):
    return Action('TOGGLE_TODO', t_id=t_id)
