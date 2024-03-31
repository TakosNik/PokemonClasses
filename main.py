import time
import numpy as np
import sys

#Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Class creation
class Pokemon:
    def __init__(self, name, types, moves, EVs, health = '====================')
        #variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defence = EVs['DEFENCE']
        self.bars = 20 # The amount of hp bars

    def fight(self, Pokemon2):
        print('----POKEMON BATTLE----')
        print(f'{self.name}')
        print('TYPE/', self.types)
        print('DEFENCE/', self.defence)
        print('LVL/', 3*(1+np.mean([self.attack, self.defence])))
        print('\nVS')
        print(f'{Pokemon2.name}')
        print('TYPE/', Pokemon2.types)
        print('DEFENCE/', Pokemon2.defence)
        print('LVL/', 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defence])))
        print('\nVS')

        time.sleep(2)

        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                #For same type
                if Pokemon2.types == k:
                    string_1_attack = 'Its not very effective...'
                    string_2_attack = 'Its not very effective...'

                # Pokemon2 is stronger
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defence *= 2
                    self.attack /= 2
                    self.defence /= 2
                    string_1_attack = 'Its not very effective...'
                    string_2_attack = 'Its super effective!'








if __name__ == '__main__':
    pass