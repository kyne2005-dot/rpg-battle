import random
from Hero import Hero
#story,text,decision,low,high
story=[("You are traveliving down the road and BAM out of no where you are attacked by the enemy","damage",50,80),("After you defeat the enemy you wander and find a chest that has heals.","heal",20,40),("Once again you head into another fight this time a boss fight.","damage",100,120),("After the battle you are badly injured so you run and find a super healer.","heal",50,70)]

def get_story(player,text,decision,low,high):
        print(f"\n{text}")
        amount=random.randint(low,high)
        if decision=="damage":
            player.damage(amount)
            print(f"During the battle you take -{amount} damage you needs to get heals before the next battle.")
        else:
            player.heals(amount)
            print(f"You finally get heals which gives you +{amount} heals, now you are ready for battle.")
        print(player)

def main():
    player=Hero("Hero")
    print(player)
    for text,decision,low,high in story:
        get_story(player,text,decision,low,high)
        if not player.is_alive():
            print("\nYou are dead")
            return
        print("\nYou are alive")




if __name__=="__main__":
    main()