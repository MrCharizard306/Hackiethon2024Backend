# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from Game.gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = DashAttackSkill     
SECONDARY_SKILL = Hadoken      

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
CANCEL = ("skill_cancel", )

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
        
        # if not secondary_on_cooldown(player):
        #     return SECONDARY
        # elif not secondary_on_cooldown(player):
        #     return PRIMARY
        
        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])
    #     if distance < 3:
    #         return LIGHT
        
    #     return FORWARD

                
    # distance = abs(get_pos(player)[0] - get_pos(enemy)[0])
        # if not primary_on_cooldown(player) and distance < 5:
        #     return PRIMARY
        # elif distance == 1:
        #     return BLOCK
        # if get_stun_duration(enemy) == 0 and distance == 1:
        #     return BLOCK
        # elif get_stun_duration(enemy) > 0 and distance == 1:
        #     for i in range(3):
        #         LIGHT 
        if not bool(enemy_projectiles):
            # if get_stun_duration(enemy) == 0 and distance == 1:
            #     return HEAVY
            # elif get_stun_duration(enemy) > 0 and distance == 1:
            #     for i in range(3):
            #         LIGHT 
            # if distance < 3:
            #     return BACK
            # elif not primary_on_cooldown(player) and distance < 5:
            #     return PRIMARY
            # # elif not secondary_on_cooldown(player) and 2 <= distance <= 7:
            # #     return SECONDARY and BACK
            # elif not secondary_on_cooldown and distance >= 2:
            #     return SECONDARY
            # else: 
            #     for i in range(3):
            #         BACK
            #
            # if not secondary_on_cooldown(player):
            #     return SECONDARY
            # elif not primary_on_cooldown(player):
            #     return PRIMARY
            # else:
            #     return LIGHT
            # if distance == 1:
            #     return HEAVY
           

            # if get_stun_duration(enemy) == 0 and distance <= 1 and primary_on_cooldown(enemy):
            #     return BLOCK and BACK
            # elif distance  <= 1 and not heavy_on_cooldown and get_stun_duration(enemy) != 0 :
            #     return HEAVY
            # elif distance  <= 1 and  heavy_on_cooldown and get_stun_duration(enemy) != 0 :
            #     return LIGHT
            # elif not primary_on_cooldown(player) and distance < 5:
            #     return PRIMARY
            # elif not secondary_on_cooldown(player) and get_pos(player)[1] == 0:
            #     return SECONDARY
            if not secondary_on_cooldown(player):
                return SECONDARY
            elif not primary_on_cooldown(player):
                return PRIMARY
            elif distance  <= 1 and not heavy_on_cooldown and get_stun_duration(enemy) != 0 :
                return HEAVY
            elif distance  <= 1 and  heavy_on_cooldown and get_stun_duration(enemy) != 0 :
                return LIGHT
            
            else:
                return FORWARD and BLOCK

                
        else:
            
            distproj = abs(get_pos(player)[0] - get_proj_pos(enemy_projectiles[0])[0])
            print(distproj)
            if distance < 5 and distproj < 5 and not primary_on_cooldown(player):
                return PRIMARY
            
            elif distance == 1 and primary_on_cooldown:
                    JUMP_BACKWARD
            elif distproj <= 1:
                return BLOCK             
            # if distance == 1:
            #     return HEAVY    
            # elif not primary_on_cooldown(player) and distance < 5 and distproj < 5:
            #     return PRIMARY 
            # elif primary_on_cooldown(player) and distproj == 1:
            #     return JUMP_BACKWARD
            
            # else:
            #     if not secondary_on_cooldown(player):
            #         return SECONDARY
            #     elif not primary_on_cooldown(player):
            #         return PRIMARY


        
        
    