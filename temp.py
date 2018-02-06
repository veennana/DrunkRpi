import temp2 as temp2





def class_game():#start game
    import Mouse_Trap_New_backup as MouseTrap
    MouseTrap.game_intro(0)
    MouseTrap.pygame.quit()
    MouseTrap.quit()





def class_game_result():
    f = open("test.txt","r")
    score1 = int(f.read())
    f.close()
    if score1 == 0:
        print("Loser %d yung score"%score1)
    elif score1 >=1 and score1 <=5:
        print("Pwede na %d yung score"%score1)
    else:
        print("Wow! Taas! %d yung score"%score1)

def funcintemp2():
    y = temp2.writeto()


class_game()
