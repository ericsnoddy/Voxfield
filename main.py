# local
from config import *  # imports pygame as pg
from star import *   


class App:
    def __init__(self):
        self.win = pg.display.set_mode(RES)
        # by overlaying an alpha surface instead of the bg fill, creates "tracers" that suggest volume
        self.alpha_surf = pg.Surface(RES)
        self.alpha_surf.set_alpha(ALPHA)

        self.clock = pg.time.Clock()
        self.starfield = Starfield(self)


    def run(self):
        while True:
            # since we don't fill the screen black before every draw, traces of our rects are left over from last draw
            # but they get increasingly duller as more alpha surfs are blitted over top, creating the tracer effect
            self.win.blit(self.alpha_surf, (0,0))
            self.starfield.run()

            pg.display.flip()
            pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
            [exit() for e in pg.event.get() if e.type == pg.QUIT]
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()
