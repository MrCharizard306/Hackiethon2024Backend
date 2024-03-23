# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = DashAttackSkill
SECONDARY_SKILL = Grenade

#constants, for easier move return
#movements
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

# TODO FOR PARTICIPANT: WRITE YOUR WINNING BOT
class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL
        
    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary
    
    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])
        print(distance)
        
            
        
        if not bool(enemy_projectiles):
            
        
                if not primary_on_cooldown(player):
                    return PRIMARY
                if not secondary_on_cooldown:
                    return SECONDARY    
                elif distance > 3 and secondary_on_cooldown:
                    return BACK 
        else:
            
            distproj = abs(get_pos(player)[0] - get_proj_pos(enemy_projectiles[0])[0])
            #if distance == 1:
                
                #if primary_on_cooldown and distproj >= 1:
                  #  if not secondary_on_cooldown:
                    #    return BACK and SECONDARY
                   # else:
                     #   return BACK and BLOCK
                #elif not primary_on_cooldown:
                 #   return PRIMARY
                
           # elif distproj == 0:
            #    return BACK and BLOCK
             
            
            if not primary_on_cooldown(player) and distance <= 5:
                return PRIMARY and FORWARD
            elif primary_on_cooldown and distproj == 1:
                return JUMP_FORWARD
            elif distance == 7 and not secondary_on_cooldown:
                return SECONDARY
            else:
                return FORWARD
                    
            



            