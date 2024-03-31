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
    def __init__(self, name, types, moves, EVs, health = '===================='):
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

                # First pokemon is stronger
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defence *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defence /= 2
                    string_1_attack = 'Its super effective!'
                    string_2_attack = 'Its not very effective...'

        # The fight
        # Proceeds while both pokemon have hp
        while (self.bars > 0) and (Pokemon2.bars > 0):
            print(f'{self.name}\t\tHLTH\t{self.health}\n')
            print(f'{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n')

            print(f'Go {self.name}')
            for i, x in enumerate(self.moves):
                print(f'{i+i}.', x)
            index = int(input('Pick a move: '))
            delay_print(f'{self.name} used {moves[index-1]}!')
            time.sleep(1)
            delay_print(string_1_attack)

            #Damage determination
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""


            #Add remaining hp bars back
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defence)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f'{self.name}\t\tHLTH\t{self.health}\n')
            print(f'{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n')
            time.sleep(.5)

            #Check if faded
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon.name + " fainted.")
                break

            #Pokemon2 turn
            print(f'Go {Pokemon2.name}')
            for i, x in enumerate(Pokemon2.moves):
                print(f'{i + i}.', x)
            index = int(input('Pick a move: '))
            delay_print(f'{Pokemon2.name} used {moves[index - 1]}!')
            time.sleep(1)
            delay_print(string_2_attack)

            # Damage determination
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add remaining hp bars back
            for j in range(int(self.bars + .1 * self.defence)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f'{self.name}\t\tHLTH\t{self.health}\n')
            print(f'{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n')
            time.sleep(.5)

            # Check if faded
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon.name + " fainted.")
                break

        money = np.random.choice(5000)
        delay_print(f"Opponent paid you ${money}")



if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


    Charizard.fight(Blastoise) # Get them to fight