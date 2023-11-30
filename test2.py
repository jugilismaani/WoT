import numpy as np

NoDrop = []

# Lists for tracking the spesific tank drops
PlayersGotA = []
PlayersGotB = []
PlayersGotC = []
PlayersGotD = []
PlayersGotE = []

# Lists for counting the amount of boxes in a sample
PlayersGot0 = []
PlayersGot1 = []
PlayersGot2 = []
PlayersGot3 = []
PlayersGot4 = []
PlayersGot5 = []

HowManySpesificTanksPlayerGot = []

HowManyBoxes = 25 # The amount of boxes players bought

rng = np.random.default_rng()
for players in range(10000): # Going through the loop 10 000 times, representing 10 000 users
    SpesificTankA = [] # Lists are emptied in the beginning
    SpesificTankB = []
    SpesificTankC = []
    SpesificTankD = []
    SpesificTankE = []
    HowManySpesifics = []
    for i in range(HowManyBoxes):
        if len(NoDrop) < 50: # If there has been a tank drop during the past 50 boxes 
            roll = rng.integers(low=1, high=10000, size=1) # random generator, 0.48% drop chance for individual tanks, so interval of 48 out of 10 000
            if roll >= 1 and roll <= 48: 
                SpesificTankA.append(0) # if roll hits for a spesific tank, the list gets longer
                NoDrop = [] # every time a drop happens, the length of the "nodrop" list drops to zero
            if roll > 48 and roll <= 96:
                SpesificTankB.append(0)
                NoDrop = []
            if roll > 96 and roll <= 144:
                SpesificTankC.append(0)
                NoDrop = []
            if roll > 144 and roll <= 192:
                SpesificTankD.append(0)
                NoDrop = []
            if roll > 192 and roll <= 240:
                SpesificTankE.append(0)
                NoDrop = []
        if len(NoDrop) == 50: # If there has not been a drop during the last 50 boxes, pity system kicks in
            roll = rng.integers(low=1, high=6, size=1) # this gives numbers from 1 to 5, for some reason when high was set to 5, only numbers from 1 to 4 appeared
            if roll == 1: # always rolls one of the tanks with 20% chance
                SpesificTankA.append(0) 
                NoDrop = []
            if roll == 2:
                SpesificTankB.append(0)
                NoDrop = []
            if roll == 3:
                SpesificTankC.append(0)
                NoDrop = []
            if roll == 4:
                SpesificTankD.append(0)
                NoDrop = []
            if roll == 5:
                SpesificTankE.append(0)
                NoDrop = []
        NoDrop.append(0) # Length of "NoDrop" increases by 1 after every loop, always resets if tank drops 
    if len(SpesificTankA) > 0: # if player n has acquired a "tank A", the number of players with "tank A" increases
        PlayersGotA.append(0)
        HowManySpesifics.append(0) # this list tracks how many different tanks each player n has acquired
    if len(SpesificTankB) > 0:
        PlayersGotB.append(0)
        HowManySpesifics.append(0)
    if len(SpesificTankC) > 0:
        PlayersGotC.append(0)
        HowManySpesifics.append(0)
    if len(SpesificTankD) > 0:
        PlayersGotD.append(0)
        HowManySpesifics.append(0)
    if len(SpesificTankE) > 0:
        PlayersGotE.append(0)
        HowManySpesifics.append(0)
    HowManySpesificTanksPlayerGot.append(len(HowManySpesifics)) # this counts how many of the available tanks player got at least once

print(len(PlayersGotA), len(PlayersGotB), len(PlayersGotC), len(PlayersGotD), len(PlayersGotE))
print(HowManySpesificTanksPlayerGot)
# Checks how many results are among the 10 000 players
NoTank = HowManySpesificTanksPlayerGot.count(0)
OneTank = HowManySpesificTanksPlayerGot.count(1)
TwoTank = HowManySpesificTanksPlayerGot.count(2)
ThreeTank = HowManySpesificTanksPlayerGot.count(3)
FourTank = HowManySpesificTanksPlayerGot.count(4)
FiveTank = HowManySpesificTanksPlayerGot.count(5)
print("Player with no tanks:", NoTank)
print("Players with a single tank:", OneTank)
print("Players with two tanks:", TwoTank)
print("Players with three tanks:", ThreeTank)
print("Players with four tanks:", FourTank)
print("Players with five tanks:", FiveTank)