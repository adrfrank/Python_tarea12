from copy import deepcopy

def todo(state, action):
    if action.action_type == 'ADD_TODO':
        return {'t_id': action.t_id, 'text': action.text, 'completed': False}
    elif action.action_type == 'TOGGLE_TODO':
        if state['t_id'] != action.t_id:
            return state
        else:
            new_state = deepcopy(state)
            new_state.update({'completed': not state['completed']})
            return new_state
    else:
        return state


def todos(action, state=[]):
    if action.action_type == 'ADD_TODO':
        return state + [todo(state, action)]
    elif action.action_type == 'TOGGLE_TODO':
        return [todo(t, action) for t in state]
    else:
        return state
