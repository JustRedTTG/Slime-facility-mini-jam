# Level data updated on: 2022-07-09 21:54:42.237316
import engine.object_renderer as objr

class level:
    def __init__(self, start_pos=0, title=0, blocks1=0, blocks2=0, hidden=0, splat_blocks=0, splat_interact_open=0, splat_interact_close=0, harm_blocks=0, awards=0, objects=0, hearts=0, health=0, ending_platform=0, back1=(255,255,255), back2=(255,255,255)):
        self.start_pos = start_pos
        self.title = title
        self.blocks1 = blocks1
        self.blocks2 = blocks2
        self.hidden = hidden
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
        [objr.tutorial_arrow((3,3),(5,3),(50,50,50),(70,70,70),270)],
        [], 3, (6,3), (255,250,250)),
    level((1, 1), 'Tutorial 2',
        [(1,0),(3,0),(5,0),(7,0),(9,0),(0,1),(10,1),(12,1),(0,3),(2,3),(4,3),(6,3),(10,3),(12,3),(7,4),(0,5),(2,5),(10,5),(12,5),(3,6),(5,6),(7,6),(0,7),(12,7),(1,8),(3,8),(5,8),(7,8),(9,8),(11,8),],
        [(0,0),(2,0),(4,0),(6,0),(8,0),(10,0),(11,1),(0,2),(12,2),(1,3),(3,3),(5,3),(7,3),(10,4),(12,4),(1,5),(7,5),(0,6),(2,6),(4,6),(6,6),(10,6),(12,6),(0,8),(2,8),(4,8),(6,8),(8,8),(10,8),(12,8),],
        [],
        [(6,2, 0, True),],
        [(7,7, 0, True),],
        [(4,1, 0, False),(4,2, 0, True),(10,2, 0, True),(10,7, 0, False),],
        [],
        [(11,4)],
        [objr.open_arrow((2,1),(8,1),(50,50,50),(70,70,70),270, 0),
         objr.tutorial_arrow((9,2),(9,6),(50,50,50),(70,70,70),180),
         objr.close_arrow((8,7),(2,7),(50,50,50),(70,70,70),90, 0),
         objr.close_arrow((6,1),(8,1),(50,50,50),(70,70,70),270, 0),
         objr.award_arrow((10,2),(7,2),(50,50,50),(70,70,70),90, (11,4))],
        [], 3, (1,6), (255,250,250)),

]
level_count = len(level_data)