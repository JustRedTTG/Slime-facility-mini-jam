import pygame as pg
import engine.window as window
import engine.data as data
import engine.leveldata as lvld
import engine.game as g
from engine.blend import blend
import engine.object_renderer as object_renderer
import engine.eventhandler as eventhandler

clock = pg.time.Clock()
current_screen = -1
background_i = 0
color_blending = 0
color_blending_switch = True
offset = (0, 0)
player_pos = (0, 0)
is_player_move = False

def trans_rect(display:pg.Surface, color, rect):
    if type(rect) == tuple: surface = pg.Surface((rect[2], rect[3]))
    elif type(rect) == pg.Rect: surface = pg.Surface((rect.w, rect.h))
    surface.fill(color)
    if len(color) > 3: surface.set_alpha(color[3])
    display.blit(surface, rect)

level_size = window.size[0] * .1
level_size_original = window.size[0] * .1
enter_level = False
buildSize = window.size
current_level = lvld.level()
def block_rect(pos):
    pos = (pos[0]*data.level_grid, pos[1]*data.level_grid)
    pos = (pos[0] + offset[0], pos[1] + offset[1])
    return (int(pos[0] - data.level_grid * .5), int(pos[1] - data.level_grid * .5), data.level_grid, data.level_grid)
def splat_rect(pos):
    pos = (pos[0]*data.level_grid, pos[1]*data.level_grid)
    pos = (pos[0] + offset[0], pos[1] + offset[1])
    return (int(pos[0] - data.level_grid * .6), int(pos[1] - data.level_grid * .6), data.level_grid * 1.2, data.level_grid * 1.2)
level_blind = 255
level_color = (0,0,0)
helt = False
exit_level, exit_level_number = False, g.slot.unlocked_level
quit_level = False
def handle_render():
    global current_screen, background_i, color_blending, color_blending_switch, level_size, level_size_original, buildSize, enter_level, current_level, offset, player_pos, is_player_move, level_blind, level_color, exit_level, exit_level_number, halt, quit_level
    if buildSize != window.size:
        buildSize = window.size
        level_size = window.size[0] * .1
        level_size_original = window.size[0] * .1
    window.dis.fill((0,0,0))
    halt = exit_level

    if current_screen in [0]:
        i = int(background_i)
        for y in range(0, window.size[1], 5):
            pg.draw.line(window.dis, data.boxart_pallet[i],
                         (0, y),
                         (window.size[0], y), 5)
            i += 1
            if i >= len(data.boxart_pallet): i = 0
        background_i -= 0.5
        if background_i < 0: background_i = len(data.boxart_pallet)-1

    if current_screen == 0:
        size = window.size[0] * .1
        if enter_level: level_size2 = window.size[0]
        else: level_size2 = window.size[0] * .2
        center = (window.size[0] * .5, window.size[1] * .5)
        mouse_rect = pg.Rect(*eventhandler.mouse_position, 1, 1)  # Mouse rect
        level_rect = pg.Rect(center[0] - level_size * .5, center[1] - level_size * .5,
                      level_size, level_size)
        level_rect_original = pg.Rect(center[0] - level_size_original * .5, center[1] - level_size_original * .5,
                      level_size_original, level_size_original)
        diff = level_size2 - level_size
        if enter_level and not color_blending_switch:
            current_screen = 1
        if mouse_rect.colliderect(level_rect) or enter_level or data.enter:
            if (level_size < level_size2-1 or enter_level) and not exit_level:
                level_size += diff*data.level_size_blending_increment
                level_size = min(level_size2, level_size)
            if (eventhandler.mouse_left or data.enter) and g.slot.unlocked_level < lvld.level_count and not enter_level:
                current_level = lvld.level_data[g.slot.unlocked_level]
                enter_level = True
                color_blending = 0
                color_blending_switch = True
                player_pos = current_level.start_pos
                is_player_move = False
                for object in current_level.objects:
                    object.ID = 'level obj'
                    object_renderer.objects.append(object)
                level_blind = 200
                level_color = data.level_frame_unclaimed2
                data.movement_target = 'player'
                data.force = [0, 0]
                data.splat_blocks.clear()
                data.awards_collected.clear()
        elif not exit_level:
            level_size -= diff*data.level_size_blending_increment
            level_size = max(size, level_size)
        raw = (level_size_original - (level_size2-level_size)) / (level_size_original * .9)
        rawclap = max(0, min(.9, raw))
        level_rect2 = pg.Rect(center[0] - level_size * raw * .5, center[1] - level_size * raw * .5,
                      level_size * raw, level_size * raw)
        for i in range(1,len(g.slot.complete_levels)+1):
            if i == len(g.slot.complete_levels) and len(g.slot.complete_levels) == lvld.level_count: break
            if level_size > level_size_original:
                trans_rect(window.dis, (*blend(data.level_frame_claimed1, data.level_frame_claimed2, i % 2 == 0),255-255*rawclap),
                         (center[0] - size * .5 - (size+size * .5)*i, center[1] - size * .5,
                          size, size))
            else:
                pg.draw.rect(window.dis, blend(data.level_frame_claimed1, data.level_frame_claimed2, i % 2 == 0),
                         (center[0] - size * .5 - (size+size * .5)*i, center[1] - size * .5,
                          size, size))
        for i in range(1,lvld.level_count-len(g.slot.complete_levels)):
            if level_size > level_size_original:
                trans_rect(window.dis, (*blend(data.level_frame_locked1, data.level_frame_locked2, i % 2 == 0),255-255*rawclap),
                         (center[0] - size * .5 + (size+size * .5)*i, center[1] - size * .5,
                          size, size))
            else:
                pg.draw.rect(window.dis, blend(data.level_frame_locked1, data.level_frame_locked2, i % 2 == 0),
                         (center[0] - size * .5 + (size+size * .5)*i, center[1] - size * .5,
                          size, size))
        if level_size > level_size_original and not enter_level and not exit_level:
            trans_rect(window.dis, (0,0,0,50), level_rect2)
        if exit_level:
            pg.draw.rect(window.dis, blend(data.level_frame_unclaimed1, data.level_frame_unclaimed2), level_rect_original)
            claim_rect = (level_rect[0] - size - size * .5,level_rect[1],
                          level_rect[2],level_rect[3])
            if quit_level or len(g.slot.complete_levels) == lvld.level_count:
                pg.draw.rect(window.dis, blend(data.level_frame_claimed1, data.level_frame_claimed2), level_rect)
            else:
                pg.draw.rect(window.dis, blend(data.level_frame_claimed1, data.level_frame_claimed2), claim_rect)

            if level_size > level_size_original:
                level_size -= data.level_exit_speed
            else:
                exit_level = False
                halt = False
        elif len(g.slot.complete_levels) == lvld.level_count:
            pg.draw.rect(window.dis, blend(data.level_frame_claimed1, data.level_frame_claimed2), level_rect)
        else:
            pg.draw.rect(window.dis, blend(data.level_frame_unclaimed1, data.level_frame_unclaimed2), level_rect)

    elif 1 <= current_screen <= 3:
        offset = (window.size[0] * .5 - player_pos[0] * data.level_grid,
                  window.size[1] * .5 - player_pos[1] * data.level_grid)
        data.offset = offset
        window.dis.fill(blend(current_level.background1, current_level.background2))
        for block in current_level.blocks1: pg.draw.rect(window.dis, blend(data.level_block_color1, data.level_block_color2), block_rect(block), data.level_grid_frame)
        for block in current_level.blocks2: pg.draw.rect(window.dis, blend(data.level_block_color1, data.level_block_color2, True), block_rect(block), data.level_grid_frame)
        for block in current_level.stick_blocks: trans_rect(window.dis, (*blend(data.level_stick_block_color1, data.level_stick_block_color2, True), 150), block_rect(block))
        for block in current_level.splat_blocks:
            if not block[2] in data.splat_blocks: trans_rect(window.dis, (*blend(data.level_splat_block_color1, data.level_splat_block_color2, block[3]), 200), block_rect(block))
            else: trans_rect(window.dis, (*blend(data.level_splat_block_color1, data.level_splat_block_color2, block[3]), 155), splat_rect(block))
        for block in current_level.splat_interact_open:
            if not block[2] in data.splat_blocks: pg.draw.rect(window.dis, blend(data.level_interacted_block_color1, data.level_interacted_block_color2, block[3]), block_rect(block), data.level_grid_frame)
        for block in current_level.splat_interact_close:
            if block[2] in data.splat_blocks: pg.draw.rect(window.dis, blend(data.level_interacted_block_color1, data.level_interacted_block_color2, block[3]), block_rect(block), data.level_grid_frame)
        for award in current_level.awards:
            if not award in data.awards_collected: pg.draw.ellipse(window.dis, blend(data.level_award_color1, data.level_award_color2), block_rect(award), data.level_grid_frame)
        trans_rect(window.dis, (*blend(data.level_exit_color1, data.level_exit_color2), 200), block_rect(current_level.ending_platform))

        if 2 <= current_screen <= 3 and level_blind <= 255:
            trans_rect(window.dis, (*level_color, level_blind), (0, 0, *window.size))
            level_blind += 5
        elif level_blind > 0:
            trans_rect(window.dis, (*level_color, level_blind), (0,0,*window.size))
            level_blind -= 5
        if 2 <= current_screen <= 3 and level_blind >= 255:
            quit_level = current_screen == 3
            current_screen = 0
            level_blind = 255
            enter_level = False
            exit_level = True
            exit_level_number


    for object in object_renderer.objects:
        if object.ID == 'level obj' and current_screen != 1: continue
        object.render()
        halt = halt or object.halt
    halt = halt or current_screen == 2
    halt = halt or current_screen == 3

    if current_screen == 1 and not halt:
        player_rect = block_rect(player_pos)
        trans_rect(window.dis, (*blend(data.player_color1, data.player_color2), 200), (
            player_rect[0] + max(0, data.force[0]) * data.level_grid * .25 * data.movement_time,
            player_rect[1] + max(0, data.force[1]) * data.level_grid * .25 * data.movement_time,
            player_rect[2] + min(0, data.force[0]) * data.level_grid * .25 * data.movement_time - max(0, data.force[0]) * data.level_grid * .25 * data.movement_time,
            player_rect[3]  + min(0, data.force[1]) * data.level_grid * .25 * data.movement_time - max(0, data.force[1]) * data.level_grid * .25 * data.movement_time
        ))
        if data.debug: pg.draw.rect(window.dis, 'orange', player_rect, 2, 5)

    clock.tick(120)
    if data.debug and data.debug_level > 0:
        color_blending = 1
        color_blending_switch = False
    elif color_blending_switch:
        color_blending += data.color_blending_increment
        if color_blending >= 1:
            color_blending_switch = False
            color_blending = 1
    else:
        color_blending -= data.color_blending_increment
        if color_blending <= 0:
            color_blending_switch = True
            color_blending = 0
    data.color_blending = color_blending