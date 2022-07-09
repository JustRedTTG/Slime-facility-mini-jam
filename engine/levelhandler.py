import engine.main_renderer as mr
import engine.game as g
import engine.eventhandler as eventhandler
import engine.action as action
import engine.data as data

def splat_filter(splats, splatted=False):
    final = []
    for splat in splats:
        if (splat[2] in data.splat_blocks) == splatted: final.append((splat[0], splat[1]))
    return final
def get_splat_location(position):
    for splat in mr.current_level.splat_blocks:
        if not splat[2] in data.splat_blocks:
            if (splat[0], splat[1]) == position: return splat
def check_for_block(position): return position in mr.current_level.blocks1 or \
                                      position in mr.current_level.blocks2 or \
                                      position in mr.current_level.hidden or \
                                      position in splat_filter(mr.current_level.splat_interact_open) or \
                                      position in splat_filter(mr.current_level.splat_interact_close, True)
def check_for_splat(position): return position in splat_filter(mr.current_level.splat_blocks)
def check_for_award(position): return position in mr.current_level.awards
def player_grid(): return (int(mr.player_pos[0]+.5), int(mr.player_pos[1]+.5))
def add_grid(g, a): return (g[0]+a[0], g[1]+a[1])
def remove_grid(g, a): return (g[0]-a[0], g[1]-a[1])
def reset_movement():
    data.force = [0, 0]
    mr.player_pos = player_grid()
    eventhandler.allow_force = True

def move_right():
    if not check_for_block(add_grid(player_grid(), (1, 0))): mr.player_pos = add_grid(mr.player_pos, (data.movement_speed, 0))
    else: reset_movement()
def move_left():
    if not check_for_block(remove_grid(player_grid(), (1, 0))): mr.player_pos = remove_grid(mr.player_pos, (data.movement_speed, 0))
    else: reset_movement()
def move_up():
    if not check_for_block(remove_grid(player_grid(), (0, 1))): mr.player_pos = remove_grid(mr.player_pos, (0, data.movement_speed))
    else: reset_movement()
def move_down():
    if not check_for_block(add_grid(player_grid(), (0, 1))): mr.player_pos = add_grid(mr.player_pos, (0, data.movement_speed))
    else: reset_movement()

def debug_cube(pos, color): mr.trans_rect(mr.window.dis, color, mr.block_rect(pos))
def debug_draw(cube):
    if check_for_block(cube): debug_cube(cube, (0,255,0,50))
    else: debug_cube(cube, (255,0,0,20))
def handle_level():
    if mr.current_screen < 1: return
    if mr.halt: return

    # Movement
    if data.force[0] > 0: move_right()
    elif data.force[0] < 0: move_left()
    elif data.force[1] > 0: move_down()
    elif data.force[1] < 0: move_up()

    # Interactions
    if check_for_splat(player_grid()): data.splat_blocks.add(get_splat_location(player_grid())[2])
    if check_for_award(player_grid()): data.awards_collected.add(player_grid())

    if mr.current_screen > 1: return
    # Events
    if player_grid() == mr.current_level.ending_platform:
        g.slot.complete_levels.append(g.slot.unlocked_level)
        g.slot.unlocked_level += 1
        eventhandler.add_action(action.save)
        mr.current_screen = 2
        mr.level_size = mr.window.size[0]
        mr.level_size_original = mr.window.size[0] * .1
        mr.object_renderer.remove('level obj', True)

    # DEBUG
    if not data.debug: return
    debug_draw(add_grid(player_grid(), (1, 0)))
    debug_draw(remove_grid(player_grid(), (1, 0)))
    debug_draw(add_grid(player_grid(), (0, 1)))
    debug_draw(remove_grid(player_grid(), (0, 1)))