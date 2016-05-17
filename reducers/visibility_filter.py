def visibility_filter(action, state='SHOW_ALL'):
    if action.action_type == 'SET_VISIBILITY_FILTER':
        return action.vis_filter
    else:
        return state
