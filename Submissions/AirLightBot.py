# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from gameSettings import HP
from random import random


# primary skill can be defensive or offensive
# secondary skills involve summoning a projectile

# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Lasso, Boomerang, Ice Wall, Bear Trap

# currently unsure how to enforce this...
#TODO FOR USER: Set primary and secondary skill here
PRIMARY_SKILL = OnePunchSkill
SECONDARY_SKILL = SuperArmorSkill

#constants, for easier move return
# movements
JUMP = ("move", (0,1))
FORWARD = ("move", (1,0))
BACK = ("move", (-1,0))
JUMP_FORWARD = ("move", (1,1))
JUMP_BACKWARD = ("move", (-1, 1))

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)

# no move, aka no input
NOMOVE = "NoMove"
# for testing
moves = SECONDARY,
moves_iter = iter(moves)

NLIGHTS = 2

class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL
        self.light_counter = NLIGHTS
        self.enemy_health = HP

        
    def init_player_skills(self):
        return self.primary, self.secondary
    
    #MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        if self.light_counter > 0:
            self.light_counter -= 1
            return LIGHT

        if len(enemy_projectiles) > 0:
            enemy_projectile = enemy_projectiles[0]
            dist_from_projectile = abs(get_pos(player)[0] - get_proj_pos(enemy_projectile)[0])
            if dist_from_projectile < 3:
                self.light_counter = NLIGHTS
                return JUMP_FORWARD
            
        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])
        
        if distance == 1:
            return LIGHT
        
        return FORWARD