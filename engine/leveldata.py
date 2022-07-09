import engine.object_renderer as objr

class level:
    def __init__(self, start_pos, title, blocks, splat_blocks, harm_blocks, awards, objects, hearts, health, ending_platform, back1=(255,255,255), back2=(255,255,255)):
        self.start_pos = start_pos
        self.title = title
        self.blocks = blocks
        self.splat_blocks = splat_blocks
        self.harm_blocks = harm_blocks
        self.awards = awards
        self.objects = objects
        self.hearts = hearts
        self.health = health
        self.ending_platform = ending_platform
        self.background1 = back1
        self.background2 = back2

level_data = [
    level((1, 2),'Tutorial 1', [
        (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(4,4),(3,4),(2,4),(1,4),(0,4),(0,3),(0,2),(0,1)],
          [], [], [],
          [objr.tutorial_arrow((2,2),(3,2),(50,50,50),(70,70,70),270)],
          [], 3, (4,2), (255,250,250)),
    level((1, 2),'Tutorial 2', [
        (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(4,4),(3,4),(2,4),(1,4),(0,4),(0,3),(0,2),(0,1)],
          [], [], [],
          [objr.tutorial_arrow((2,2),(3,2),(50,50,50),(70,70,70),270)],
          [], 3, (4,2), (255,250,250))
]
level_count = len(level_data)