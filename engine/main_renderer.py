import pygame as pg
import engine.window as window
import engine.data as data
import engine.game as g
import engine.object_renderer as object_renderer
import engine.eventhandler as eventhandler

clock = pg.time.Clock()
current_screen = -1
background_i = 0
color_blending = 0
color_blending_switch = True

def trans_rect(display:pg.Surface, color, rect):
    if type(rect) == tuple: surface = pg.Surface((rect[2], rect[3]))
    elif type(rect) == pg.Rect: surface = pg.Surface((rect.w, rect.h))
    surface.fill(color)
    if len(color) > 3: surface.set_alpha(color[3])
    display.blit(surface, rect)

def blend(c1, c2, reverse=False):
    global color_blending
    dif_R = c2[0] - c1[0]
    dif_G = c2[1] - c1[1]
    dif_B = c2[2] - c1[2]
    if reverse:
        return (
            c1[0] + dif_R * (1-color_blending),
            c1[1] + dif_G * (1-color_blending),
            c1[2] + dif_B * (1-color_blending)
        )
    return (
        c1[0] + dif_R * color_blending,
        c1[1] + dif_G * color_blending,
        c1[2] + dif_B * color_blending
    )

level_size = window.size[0] * .1
level_size_original = window.size[0] * .1
enter_level = False
buildSize = window.size
def handle_render():
    global current_screen, background_i, color_blending, color_blending_switch, level_size, level_size_original, buildSize, enter_level
    if buildSize != window.size:
        buildSize = window.size
        level_size = window.size[0] * .1
        level_size_original = window.size[0] * .1
    window.dis.fill((0,0,0))
    halt = False

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
        diff = level_size2 - level_size
        if enter_level and not color_blending_switch:
            current_screen = 1
        if mouse_rect.colliderect(level_rect) or enter_level:
            if level_size < level_size2-1 or enter_level:
                level_size += diff*data.level_size_blending_increment
                level_size = min(level_size2, level_size)
            if eventhandler.mouse_left:
                enter_level = True
                color_blending = 0
                color_blending_switch = True

        else:
            level_size -= diff*data.level_size_blending_increment
            level_size = max(size, level_size)
        raw = (level_size_original - (level_size2-level_size)) / (level_size_original * .9)
        rawclap = max(0, min(.9, raw))
        level_rect2 = pg.Rect(center[0] - level_size * raw * .5, center[1] - level_size * raw * .5,
                      level_size * raw, level_size * raw)
        for i in range(1,len(g.slot.complete_levels)+1):
            if level_size > level_size_original:
                trans_rect(window.dis, (*blend(data.level_frame_claimed1, data.level_frame_claimed2, i % 2 == 0),255-255*rawclap),
                         (center[0] - size * .5 - (size+size * .5)*i, center[1] - size * .5,
                          size, size))
            else:
                pg.draw.rect(window.dis, blend(data.level_frame_claimed1, data.level_frame_claimed2, i % 2 == 0),
                         (center[0] - size * .5 - (size+size * .5)*i, center[1] - size * .5,
                          size, size))
        for i in range(1,data.level_count-len(g.slot.complete_levels)):
            if level_size > level_size_original:
                trans_rect(window.dis, (*blend(data.level_frame_locked1, data.level_frame_locked2, i % 2 == 0),255-255*rawclap),
                         (center[0] - size * .5 + (size+size * .5)*i, center[1] - size * .5,
                          size, size))
            else:
                pg.draw.rect(window.dis, blend(data.level_frame_locked1, data.level_frame_locked2, i % 2 == 0),
                         (center[0] - size * .5 + (size+size * .5)*i, center[1] - size * .5,
                          size, size))
        if level_size > level_size_original and not enter_level:
            trans_rect(window.dis, (0,0,0,50), level_rect2)
        pg.draw.rect(window.dis, blend(data.level_frame_unclaimed1, data.level_frame_unclaimed2), level_rect)

    elif current_screen == 1: pass

    for object in object_renderer.objects:
        object.render()
        halt = halt and object.halt
    clock.tick(120)

    if color_blending_switch:
        color_blending += data.color_blending_increment
        if color_blending >= 1:
            color_blending_switch = False
            color_blending = 1
    else:
        color_blending -= data.color_blending_increment
        if color_blending <= 0:
            color_blending_switch = True
            color_blending = 0