import sys
import pygame
import os

__author__ = 'jezinka'

os.environ['SDL_VIDEO_CENTERED'] = '1'

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


def calculate_next_step(turn_table, true_bin_rules):

    turn_table_tmp = turn_table[:]

    for i in range(1, len(turn_table) - 2):

        cells = ''.join([str(turn_table[i - 1]), str(turn_table[i]), str(turn_table[i + 1])])

        if cells in true_bin_rules:
            turn_table_tmp[i] = 1
        else:
            turn_table_tmp[i] = 0

    return turn_table_tmp


def start_automata(rule_No):
    pygame.init()
    pygame.display.set_caption("One-dimension cellular automata")

    size = 1200, 600
    screen = pygame.display.set_mode(size)

    done = False

    clock = pygame.time.Clock()
    step_counter = 0

    screen.fill(WHITE)
    pygame.display.flip()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    font = pygame.font.Font(None, 24)

    turn_table = [0] * size[0]
    turn_table[size[0]/2] = 1

    bin_rule = bin(int(rule_No))[2:].rjust(8, '0')[::-1]
    true_indexes = [i for i in range(len(bin_rule)) if bin_rule[i] == '1']
    true_bin_rules = [bin(x)[2:].rjust(3, '0') for x in true_indexes]

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                done = True

        for i in range(len(turn_table)):
            background.set_at((i, step_counter), WHITE if turn_table[i] == 0 else BLACK)

        step_counter += 1

        if step_counter <= size[1]:
            turn_table = calculate_next_step(turn_table, true_bin_rules)

            text = font.render("Rule:" + rule_No + " Step:" + str(step_counter), True, BLACK)
            screen.blit(text, (0, 0))

            text1 = font.render("Press any key to quit", True, BLACK)
            screen.blit(text1, (0, 26))
            pygame.display.update()

            background = background.convert()
            screen.blit(background, (0, 0))

            clock.tick(12000)


rule_No = raw_input('Choose the rule (0-255):')
start_automata(rule_No)


