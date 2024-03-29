# Level data updated on: 2022-09-24 11:46:53.360014
import engine.object_renderer as objr

class level:
    def __init__(self, start_pos=0, title=0, blocks1=0, blocks2=0, hidden=0, stick_blocks=0, splat_blocks=0, splat_interact_open=0, splat_interact_close=0, harm_blocks=0, awards=0, objects=0, hearts=0, health=0, ending_platform=0, back1=(255,255,255), back2=(255,255,255)):
        self.start_pos = start_pos
        self.title = title
        self.blocks1 = blocks1
        self.blocks2 = blocks2
        self.hidden = hidden
        self.stick_blocks = stick_blocks
        self.splat_blocks = splat_blocks
        self.splat_interact_open = splat_interact_open
        self.splat_interact_close = splat_interact_close
        self.harm_blocks = harm_blocks
        self.awards = awards
        self.objects = objects
        self.hearts = hearts
        self.health = health
        self.ending_platform = ending_platform
        self.background1 = back1
        self.background2 = back2


level_data = [
# All the following data was made using a level creator and level images.
    level((2, 3), 'Tutorial 1',
        [(1,0),(3,0),(5,0),(7,0),(0,1),(8,1),(0,3),(8,3),(0,5),(8,5),(1,6),(3,6),(5,6),(7,6),],
        [(0,0),(2,0),(4,0),(6,0),(8,0),(0,2),(8,2),(0,4),(8,4),(0,6),(2,6),(4,6),(6,6),(8,6),],
        [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(1,3),(7,3),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),],
        [],
        [],
        [],
        [],
        [],
        [],
        [objr.tutorial_arrow((3,3),(5,3),(50,50,50),(70,70,70),270)],
        [], 3, (6,3), (255,250,250)),
    level((1, 1), 'Tutorial 2',
        [(1,0),(3,0),(5,0),(7,0),(9,0),(0,1),(10,1),(12,1),(0,3),(2,3),(4,3),(6,3),(10,3),(12,3),(7,4),(10,5),(12,5),(1,6),(3,6),(5,6),(7,6),(0,7),(12,7),(1,8),(3,8),(5,8),(7,8),(9,8),(11,8),],
        [(0,0),(2,0),(4,0),(6,0),(8,0),(10,0),(11,1),(0,2),(12,2),(1,3),(3,3),(5,3),(7,3),(10,4),(12,4),(7,5),(0,6),(2,6),(4,6),(6,6),(10,6),(12,6),(0,8),(2,8),(4,8),(6,8),(8,8),(10,8),(12,8),],
        [],
        [],
        [(6,2, 0, True),],
        [(7,7, 0, True),],
        [(4,1, 0, False),(4,2, 0, True),(10,2, 0, True),(10,7, 0, False),],
        [],
        [(11,4),],
        [objr.open_arrow((2,1),(8,1),(50,50,50),(70,70,70),270, 0, 'tut_arrow'),
         objr.tutorial_arrow((9,2),(9,6),(50,50,50),(70,70,70), 180, 'tut_arrow'),
         objr.close_arrow((9,2),(9,6),(50,50,50),(70,70,70), 180, 0),
         objr.tutorial_arrow((11,6),(11,5),(50,50,50),(70,70,70), 0, 'tut_arrow'),
         objr.close_arrow((8,7),(2,7),(50,50,50),(70,70,70),90, 0),
         objr.close_arrow((6,1),(8,1),(50,50,50),(70,70,70),270, 0),
         objr.award_arrow((10,2),(7,2),(50,50,50),(70,70,70),90, (11, 4), 'award_arrow'),
         objr.award_eraser((11, 4), 'tut_arrow', True),
         objr.splat_eraser(0, 'award_arrow')],
        [], 3, (1,7), (255,250,250)),
    level((7, 2), 'Tutorial 3',
        [(6,0),(8,0),(5,1),(9,1),(5,3),(9,3),(1,5),(3,5),(5,5),(9,5),(11,5),(13,5),(0,6),(14,6),(0,8),(14,8),(1,9),(3,9),(5,9),(9,9),(11,9),(13,9),(5,11),(9,11),(5,13),(9,13),(6,14),(8,14),],
        [(5,0),(7,0),(9,0),(5,2),(9,2),(5,4),(9,4),(0,5),(2,5),(4,5),(10,5),(12,5),(14,5),(0,7),(14,7),(0,9),(2,9),(4,9),(10,9),(12,9),(14,9),(5,10),(9,10),(5,12),(9,12),(5,14),(7,14),(9,14),],
        [(7,1),(6,2),(8,2),(2,6),(12,6),(1,7),(13,7),(2,8),(12,8),(6,12),(8,12),(7,13),],
        [(7,7),],
        [],
        [],
        [],
        [],
        [(2,7),(12,7),],
        [objr.tutorial_arrow((7,3),(7,6),(200,200,200),(220,240,220), 180, 'tut_arrow'),
         objr.stick_arrow((6,7),(3,7),(255,255,0),(255,255,200), 90, (7,7), 'award_left'),
         objr.award_arrow((3,7),(6,7),(0,255,255),(200,255,255), 270, (2,7), 'award_left_'),
         objr.stick_arrow((8,7),(11,7),(255,255,0),(255,255,200), 270, (7,7), 'award_right'),
         objr.award_arrow((11,7),(8,7),(0,255,255),(200,255,255), 90, (12,7), 'award_right_'),
         objr.stick_arrow((7,8),(7,11),(0,0,255),(200,200,255), 180, (7,7)),
         objr.stick_eraser((7,7), 'tut_arrow'),
         objr.award_eraser((2,7), 'award_left'),
         objr.award_eraser((12,7), 'award_right'),],
        [], 3, (7,12), (20,20,20),(30,30,30)),
    level((6, 13), 'Level 1',
        [(1,0),(3,0),(5,0),(7,0),(9,0),(11,0),(13,0),(0,1),(14,1),(0,3),(2,3),(4,3),(6,3),(8,3),(10,3),(12,3),(14,3),(3,4),(11,4),(0,5),(14,5),(5,6),(9,6),(0,7),(14,7),(6,8),(8,8),(0,9),(14,9),(6,10),(8,10),(0,11),(14,11),(0,13),(14,13),(1,14),(3,14),(5,14),(7,14),(9,14),(11,14),(13,14),],
        [(0,0),(2,0),(4,0),(6,0),(8,0),(10,0),(12,0),(14,0),(7,1),(0,2),(14,2),(3,3),(5,3),(7,3),(9,3),(11,3),(0,4),(14,4),(4,5),(10,5),(0,6),(14,6),(6,7),(8,7),(0,8),(14,8),(6,9),(8,9),(0,10),(14,10),(0,12),(14,12),(0,14),(2,14),(4,14),(6,14),(8,14),(10,14),(12,14),(14,14),],
        [],
        [],
        [(8,1, 0, True),(11,7, 1, True),],
        [(13,3, 0, True),],
        [(1,7, 1, True),(8,13, 0, False),],
        [],
        [(3,8),(12,8),],
        [],
        [], 3, (7,5), (255,250,250)),
    level((7, 7), 'Level 2',
        [(1,0),(3,0),(5,0),(9,0),(11,0),(13,0),(0,1),(6,1),(8,1),(14,1),(0,3),(14,3),(0,5),(14,5),(1,6),(7,6),(13,6),(1,8),(13,8),(1,10),(13,10),(8,11),(1,12),(13,12),(2,13),(4,13),(6,13),(8,13),(10,13),(12,13),],
        [(0,0),(2,0),(4,0),(6,0),(8,0),(10,0),(12,0),(14,0),(0,2),(14,2),(11,3),(0,4),(6,4),(8,4),(14,4),(0,6),(6,6),(8,6),(14,6),(1,7),(13,7),(1,9),(13,9),(1,11),(13,11),(1,13),(3,13),(5,13),(7,13),(9,13),(11,13),(13,13),],
        [],
        [],
        [(3,1, 0, True),(3,5, 1, True),(9,11, 2, True),],
        [(2,1, 2, False),(6,2, 0, True),(8,2, 0, True),(3,3, 2, False),(6,5, 0, False),(8,5, 0, False),(9,6, 1, False),(10,6, 1, True),(11,6, 1, False),(12,6, 1, True),],
        [(11,2, 2, True),(5,3, 2, True),(2,4, 2, True),(10,4, 2, True),(11,5, 2, True),],
        [],
        [(4,2),(12,2),(7,3),(9,9),],
        [],
        [], 3, (10,9), (255,250,250)),

]
level_count = len(level_data)