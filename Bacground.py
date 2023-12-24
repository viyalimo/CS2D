import pygame

Background_anim = [
    pygame.image.load('Background/frame_00_delay-0.1s.gif'),
    pygame.image.load('Background/frame_01_delay-0.1s.gif'),
    pygame.image.load('Background/frame_02_delay-0.1s.gif'),
    pygame.image.load('Background/frame_03_delay-0.1s.gif'),
    pygame.image.load('Background/frame_04_delay-0.1s.gif'),
    pygame.image.load('Background/frame_05_delay-0.1s.gif'),
    pygame.image.load('Background/frame_06_delay-0.1s.gif'),
    pygame.image.load('Background/frame_07_delay-0.1s.gif'),
    pygame.image.load('Background/frame_08_delay-0.1s.gif'),
    pygame.image.load('Background/frame_09_delay-0.1s.gif'),
    pygame.image.load('Background/frame_10_delay-0.1s.gif'),
    pygame.image.load('Background/frame_11_delay-0.1s.gif'),
    pygame.image.load('Background/frame_12_delay-0.1s.gif'),
    pygame.image.load('Background/frame_13_delay-0.1s.gif'),
    pygame.image.load('Background/frame_14_delay-0.1s.gif'),
    pygame.image.load('Background/frame_15_delay-0.1s.gif'),
    pygame.image.load('Background/frame_16_delay-0.1s.gif'),
    pygame.image.load('Background/frame_17_delay-0.1s.gif'),

]


def background_anim(i, weight, height):
    frame = Background_anim[i]
    frame = pygame.transform.scale(frame, [weight, height])
    return frame, len(Background_anim)
