
#importing the necessary modules
import player as create, os, signal , pygame ,numpy as np, msvcrt, cv2, keyboard, time, sys , winsound

#init scores
score1,score2=0,0

#init fps and ms
clock=pygame.time.Clock()
pygame.init()
ms=200
fps = 12
current_frame=0

def help_guide():
    os.system('cls')
    print('Dans ce jeu vous pouvez sauter, attquer, bloquer et vous deplacer... attention ce pendant il est un peu intuif que vous pouvez ne pas traverser un obstacle ou votre adversaire ;) \nPour ganger un point vous devez atteindre votre adveraise avec une attaque non bloquee ni paree\nVous ne pouvez pas traverser les objets, ( votre adversaire est concidere comme objet ) neamoins les bugs ("Feature") existent')
    print('\n')
    print(' '*25,'Guide:')
    print('*'*70)
    print('Joueur 1',' '*17,'|',' '*17,'Joueur 2')
    print('d : avancer a droite',' '*5,'|',' '*5,'fleche droite : avancer a droite')
    print('q : avancer a gauche',' '*5,'|',' '*5,'fleche gauche : avancer a gauche')
    print('e : sauter a droite',' '*6,'|',' '*5,'m : sauter a droite')
    print('a : sauter a gauche',' '*6,'|',' '*5,'l : sauter a gauche')
    print('z : attaquer',' '*13,'|',' '*5,'o : attaquer')
    print('s : bloquer',' '*14,'|',' '*5,'p : attaquer')
    print('\n')

ms1,ms2,as1,as2,ar1,ar2,br1,br2,bt1,bt2=0,0,0,0,0,0,0,0,0,0
def setting_stats():
    global ms1,ms2,as1,as2,ar1,ar2,br1,br2,bt1,bt2
    os.system('cls')
    print('***Il est temps de donner au 1er joeur ses carecteristiques !***')
    ms1 = int(input('Donnez la vitesse de deplacement ( retardement -_- ) : '))
    as1 = int(input('Donnez la vitesse d"attaque (exacty...) : '))
    ar1 = int(input('Donnez la portee d"attaque : '))
    br1 = int(input('Donnez la portee de la defense : '))
    bt1 = int(input('Donnez la duree de la defense : '))
    os.system('cls')
    print("K, cool wait a bit '-'")
    time.sleep(1)
    os.system('cls')
    print('***Il est temps de donner au 2eme joeur ses carecteristiques !***')
    ms2 = int(input('Donnez la vitesse de deplacement ( retardement -_- ) : '))
    as2 = int(input('Donnez la vitesse d"attaque (exacty...) : '))
    ar2 = int(input('Donnez la portee d"attaque : '))
    br2 = int(input('Donnez la portee de la defense : '))
    bt2 = int(input('Donnez la duree de la defense : '))
    os.system('cls')
    print('Nicu jobu ! fufufufufu')
    time.sleep(1)
    os.system('cls')
#a start menu that give many possibility to the players
def start_menu():
    global chosen_scene,score1,score2,ms1,ms2,as1,as2,ar1,ar2,br1,br2,bt1,bt2
    winsound.PlaySound("BackgroundMusic\MainMenu.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    started = False
    while not started:
        os.system('cls')
        print('*'*32,'welcome to the arena','*'*33)
        print('\n')
        print('*'*35,'MAIN MENU:','*'*40)
        print('?-Pour lire la description du jeu, veillez appuier sur la touche "H" suivit d"un entre')
        print('?-Pour lancer une nouvelle partie, veillez appuier sur la touche "N" suivit d"entre')
        print('?-Pour reprendre une ancienne partie, veillez appuier sur la touche "C" suivit d"entre')
        print('?-Pour quiter le jeu, veillez appuier sur la touche "Q" suivit d"entre')
        print('!!-(╯°□°）╯︵ ┻━..., toute autres touches inserees vous meneront au menu precedent')
        key=input()
        #help reading
        if key in ['h','H']:
            help_guide()
            print('Appuier sur nimporte quelle touche pour retourner a la page precedente')
            input()
        #commencer une nouvelle partie
        if key in ['n','N']:
            os.system('cls')
            print('*'*32,'Lancement d"une nouvelle partie','*'*32)
            print('\n')
            print('?-Veillez choisir une des parties suivante en inserant son numero correspendant \n(si la touche inseree "D" est inseree, la scene par defaut sera chargee =\'3):')
            print('\n')
            for i in range(5):
                try:
                    with open("Scenes\scene"+str(i)+".ffscene") as f:
                        print("Scene N", i+1,': ', f.read())
                except IOError:
                    print("Un fichier manquant N :", i+1," a ete detecte, veuillez restaurer toute la version originale du jeu SVP pour eviter des erreurs internes")
            key = input()
            os.system('cls')
            if ord(key) < 54 and ord(key) >= 49:
                started=True
                chosen_scene="Scenes\scene"+str(int(key)-1)+".ffscene"
                setting_stats()
                score1,score2=0,0
                print('Votre partie va commencer "scene : '+key+'" dans un instant!!')
                print('\n')
                print('. .. ... ... .LOADING . ... . . .. .')
                time.sleep(3)
            if key in ['d','D']:
                score1,score2=0,0
                chosen_scene="Scenes\default.ffscene"
                setting_stats()
                print('Votre partie va commencer "scene par default" dans un instant!!')
                print('\n')
                print('. .. ... ... .LOADING . ... . . .. .')
                time.sleep(1.2)
                started=True
        #charger une partie
        if key in ['c','C']:
            os.system('cls')
            print('*'*32,'Lancement d"une partie sauvgardee','*'*32)
            print('\n')
            print('?-Veillez choisir une des sauvegardes suivante en inserant son numero correspendant \n(si la touche inseree est "D" ou si la sauvegarde selectionnee est vide, la scene par defaut sera chargee -_-"):')
            print('\n')
            for i in range(3):
                try:
                    with open("Saves\saved"+str(i)+".ffsave") as f:
                        print("Scene sauvgardee N", i+1,': ', f.read())
                except IOError:
                    print("Un fichier manquant a ete detecte, veuillez restaurer toute la version originale SVP pour eviter des erreurs internes")
            key = input()
            os.system('cls')
            if ord(key) < 52 and ord(key) >= 49:
                started=True
                with open("Saves\saved"+str(int(key)-1)+".ffsave") as f:
                    lines = f.read().split(',')
                if len(lines) == 13:
                    print('Voter partie sauvgarde "scene : '+key+'" va commencer dans un instant!!')
                    print('\n')
                    print('. .. ... ... .LOADING . ... . . .. .')
                    time.sleep(4)
                    chosen_scene="Saves\saved"+str(int(key)-1)+".ffsave"
                    ms1,ms2,as1,as2,ar1,ar2,br1,br2,bt1,bt2=int(lines[3]),int(lines[4]),int(lines[5]),int(lines[6]),int(lines[7]),int(lines[8]),int(lines[9]),int(lines[10]),int(lines[11]),int(lines[12])
                    score1=int(lines[1])
                    score2=int(lines[2])
                else:
                    print("La scene par default va etre chargee dans un moment car le fichier de sauvegarde est endomage 'erreur de chargement' ou vide")
                    print('Voter partie va commencer "scene par default" dans un instant!!')
                    print('\n')
                    setting_stats()
                    print('. .. ... ... .LOADING . ... . . .. .')
                    time.sleep(4)
                    chosen_scene="Scenes\default.ffscene"
            if key in ['d','D']:
                print("La scene par default va etre chargee dans un moment car la touche 'd' a ete insere")
                time.sleep(2.2)                
                setting_stats()
                score1,score2=0,0
                print('Voter partie va commencer "scene par default" dans un instant!!')
                print('\n')
                print('. .. ... ... .LOADING . ... . . .. .')                
                time.sleep(1.2)
                chosen_scene="Scenes\default.ffscene"
                started=True
        #quit the game
        if key in ['q','Q']:
            os.system('cls')
            print('Thank you for spending time on this game !!!!!')
            print("we wont miss you :3")
            time.sleep(3)
            winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_ALIAS )
            if os.path.exists("main.py"):
                os.system("python main.py")
            else:
                os.system('cls')
                print("Un fichier manquant a ete detecte, nous ne pouvons pas vous rediriger vers le menu principal; veuillez restaurer toute la version originale du jeu SVP pour eviter des erreurs internes")
                time.sleep(10)
            os.kill(os.getppid(),signal.SIGTERM)
            os.system("exit")
            sys.exit()
            break

def pause_menu():
    global done,player1,player2,current_frame,ground,actif,scene,score1,score2,chosen_scene
    winsound.PlaySound("BackgroundMusic\MainMenu.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    while not done :
        os.system('cls')
        print('!'*18,'Le jeu est en pause','!'*18)
        help_guide()
        print('*'*75)
        print('?-Pour continuer la partie, veilliez appuier sur la touche "C" suivit d"entre')
        print('?-Pour reinitialiser la partie, veilliez appuier sur la touche "R" suivit d"entre')
        print('?-Pour sauvgarder votre partie courante, veilliez appuier sur la touche "S" suivit d"entre')
        print('?-Pour retrouner au menu principal, veilliez appuier sur la touche "M" suivit d"entre \n !!Attention vous risquez de perdre tout les donne de cette parie si elle nest pas sauvgardee!!')
        print('?-Pour quiter le jeu, veilliez appuier sur la touche "Q" suivit d"entre')
        key = input()
        if key in key:
            #continue
            if key in ['c','C']:
                actif=True
                done=True
            #restart
            if key in ['r','R']:                
                score1,score2=0,0
                player1.reset()
                player2.reset()
                player1,player2 = make_scene()
                actif=True
                done=True
            #save game
            if key in ['s','S']:
                os.system('cls')
                print('?-Veillez choisir une des sauvegardes suivante en inserant son numero correspendant \n(si la touche inseree ne correspont a aucun des fichiers presents la sauvegarde ne seffectuera pas XDD):')
                for i in range(3):
                    try:
                        with open("Saves\saved"+str(i)+".ffsave") as f:
                            line = f.read().split(',')
                            if len(line)==13:
                                print("fichier pour sauvgarde N", i+1,': ',"scene :",line[0],' scores :',line[1],'-',line[2])
                            else:
                                print("fichier pour sauvgarde N", i+1,': ',"scene :")
                    except IOError:
                        print("Un fichier manquant a ete detecte, veuillez restaurer toute la version originale SVP pour eviter des erreurs internes")
                key = input()
                if ord(key) < 52 and ord(key) >= 49:
                    started=True
                    with open("Saves\saved"+str(int(key)-1)+".ffsave") as f:
                        lines=f.read().split(',')
                    if(len(lines))!=13:
                        s=list(ground)
                        for i in range(len(s)-2):
                            if s[i]=='1':
                                s[i]='_'
                            if s[i]=='2':
                                s[i]='_'
                        s[player1.get_Pos()[0]]='1'
                        s[player2.get_Pos()[0]]='2'
                        s=''.join(s)
                        with open("Saves\saved"+str(int(key)-1)+".ffsave",'w') as f:
                            f.write(f'{s},{score1},{score2},{ms1},{ms2},{as1},{as2},{ar1},{ar2},{br1},{br2},{bt1},{bt2}')
                        os.system('cls')
                        print('la partie a ete sauvgardee avec succes !!')
                        time.sleep(3)
                    else:
                        print('Vous vous appretez a ecraser une ancienne sauvgarde, etes vous sur de vouloir coninuer ? inserez "Y" pour confirmer votre decision precedente sinon inserez sur nimporte quelle autre touche')
                        decision = input()
                        if decision in ['y','Y']:
                            s=list(ground)
                            for i in range(len(s)-2):
                                if s[i]=='1':
                                    s[i]='_'
                                if s[i]=='2':
                                    s[i]='_'
                            s[player1.get_Pos()[0]]='1'
                            s[player2.get_Pos()[0]]='2'
                            s=''.join(s)
                            with open("Saves\saved"+str(int(key)-1)+".ffsave",'w') as f:
                                f.write(f'{s},{score1},{score2},{ms1},{ms2},{as1},{as2},{ar1},{ar2},{br1},{br2},{bt1},{bt2}')
                            os.system('cls')
                            print('la partie a ete sauvgardee avec succes !!')
                            time.sleep(3)
                else:
                    os.system('cls')
                    print('La sauvgarde a echouee XD, veillez reessayer si vous y tenez vraiment ( ´･ω･`)_且~ !!')
                    time.sleep(3)
            #main menu
            if key in ['m','M']:
                os.system('cls')
                print('En revenant au menu principal, votre partie sera abondonnee (non sauvgardee), etes vous sur de vouloir coninuer ? inserez "Y" pour confirmer votre decision precedente sinon inserez sur nimporte quelle autre touche')
                decision = input()
                if decision in ['y','Y']:
                    #restart everything
                    player1.reset()
                    player2.reset()
                    current_frame=0
                    start_menu()                
                    ground = loading(chosen_scene)
                    scene = np.zeros((10,len(ground)+4),object)
                    player1,player2 = make_scene()
                    actif=True
                    done=True
            #quit the game
            if key in ['q','Q']:
                os.system('cls')
                print('Thank you for spending time on this game !!!!!')
                print("we wont miss you :3")
                time.sleep(3)
                winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_ALIAS )
                if os.path.exists("main.py"):
                    os.system("python main.py")
                else :
                    os.system('cls')
                    print("Un fichier manquant a ete detecte, nous ne pouvons pas vous rediriger vers le menu principal; veuillez restaurer toute la version originale du jeu SVP pour eviter des erreurs internes")
                    time.sleep(10)
                os.kill(os.getppid(),signal.SIGTERM)
                os.system("exit")   
                sys.exit()
                break
            


#importing the scene which by defaul is the default one
def loading(scenes):
    with open(scenes) as f:
        return f.read().split(',')[0]

start_menu()


#get the final chosen scene
ground = loading(chosen_scene)

#loading the scene informations into a matrix
scene = np.zeros((10,len(ground)+4),object)

def make_scene(s1=0,s2=0):
    global ms1,ms2,as1,as2,ar1,ar2,br1,br2,bt1,bt2
    scene[:9,:]=' '
    scene[9:10,:] = '#'
    scene[0:1,(len(ground)+2)//2-2:(len(ground)+2)//2+3]=[['|',s1,'|',s2,'|']]
    for i in enumerate(ground):
        if i[1] == '1':
            player1=create.player(i[0], 0, ms1, as1, ar1, br1, bt1,i[1])
            scene[3:9,i[0]:i[0]+3]=player1.get_idle()
            scene[5:7,i[0]+3:i[0]+4]=player1.rest()
        if i[1] == '2':
            player2=create.player(i[0], 0, ms2, as2, ar2, br2, bt2,i[1])
            scene[3:9,i[0]:i[0]+3]=player2.get_idle()
            scene[5:7,i[0]-2:i[0]-1]=player2.rest()
        if i[1] == '#':
            scene[8,i[0]]='#'
    return player1,player2

#create the players
player1,player2 = make_scene(score1,score2)

#updating the scene
def update_scene(s1,s2,stat1=player1.rest(),stat2=player2.rest()):
    scene[:9,:]=' '
    for i in enumerate(ground):
        if i[1] == '#':
            scene[8,i[0]]='#'
    scene[0:1,(len(ground)+2)//2-2:(len(ground)+2)//2+3]=[['|',s1,'|',s2,'|']]
    scene[3-player1.get_Pos()[1]:9-player1.get_Pos()[1],player1.get_Pos()[0]:player1.get_Pos()[0]+3]=player1.get_idle()
    if player1.get_weap()=='g':
        scene[5-player1.get_Pos()[1]:7-player1.get_Pos()[1],player1.get_Pos()[0]+3:player1.get_Pos()[0]+4]=stat1
    else:
        scene[5-player1.get_Pos()[1]:7-player1.get_Pos()[1],player1.get_Pos()[0]-1:player1.get_Pos()[0]]=stat1
    scene[3-player2.get_Pos()[1]:9-player2.get_Pos()[1],player2.get_Pos()[0]:player2.get_Pos()[0]+3]=player2.get_idle()
    if player2.get_weap()=='d':
        scene[5-player2.get_Pos()[1]:7-player2.get_Pos()[1],player2.get_Pos()[0]-2:player2.get_Pos()[0]-1]=stat2
    else:
        scene[5-player2.get_Pos()[1]:7-player2.get_Pos()[1],player2.get_Pos()[0]+3:player2.get_Pos()[0]+4]=stat2

#displaying the scene on terminal
def display():
    for line in scene:
        output = ''
        for colomn in line:
            output+=str(colomn)
        print(output)


p1_move_left=[]
p2_move_left=[]
p1_move_right=[]
p2_move_right=[]
p1_jump_left=[]
p2_jump_left=[]
p1_jump_right=[]
p2_jump_right=[]
p1_attack=[]
p2_attack=[]
p1_block=[]
p2_block=[]
p1_move,p2_move,p1_action,p1scoring,p2scoring,p2_action=False,False,False,False,False,False
p1_jump_count,p2_jump_count=0,0
stat1,stat2=player1.rest(),player2.rest()


p1_move,p1_action,p2_move,p2_action=True,True,True,True
#function that hears the keyboard and allows one type of action for each player per frame
def listener(curframe,p1_move,p1_action,p2_move,p2_action):
    global p1_jump_count,p2_jump_count,actif,player1,player2,score1,score2,done
    distance = abs((player1.get_Pos()[0]+2)-(player2.get_Pos()[0]-1))

    #pause_menu
    if keyboard.is_pressed('space'):
        actif=False      
        done=False

    #player 1
    #if allowing one move only
    if p1_move:    
        #check which side the player is in the scene
        if player1.get_weap() == 'g':
            #moveleft
            if keyboard.is_pressed('q'):
                #check is the move is possible
                if player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-1] != '#':
                        if len(p1_move_right) > 1:
                            del p1_move_right[1:]
                        p1_move_left.append(curframe)
                p1_move = False
            #moveright
            if keyboard.is_pressed('d'):
                #check is the move is possible
                if distance > 1 and player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+3] != '#':
                    if len(p1_move_left) > 1:
                        del p1_move_left[1:]
                    p1_move_right.append(curframe)
                p1_move = False
            #jumpleft
            if keyboard.is_pressed('a'):
                #check is the move is possible
                if player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-3] != '#':
                    if len(p1_jump_left) == 0 and len(p1_jump_right) == 0:
                        p1_jump_left.append(curframe)
                        p1_jump_count=0
                p1_move = False
            #jumpright
            if keyboard.is_pressed('e'):
                #check is the move is possible
                if  distance > 1 and player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+4] != '#':
                    if len(p1_jump_right) == 0 and len(p1_jump_left) == 0:
                        p1_jump_right.append(curframe)
                        p1_jump_count=0
                p1_move = False
        else:            
            #moveleft
            if keyboard.is_pressed('q'):
                #check is the move is possible
                if distance > 1 and player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-1] != '#':
                        if len(p1_move_right) > 1:
                            del p1_move_right[1:]
                        p1_move_left.append(curframe)
                p1_move = False
            #moveright
            if keyboard.is_pressed('d'):
                #check is the move is possible
                if player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+2] != '#':
                    if len(p1_move_left) > 1:
                        del p1_move_left[1:]
                    p1_move_right.append(curframe)
                p1_move = False
            #jump left        
            if keyboard.is_pressed('a'):
                #check is the move is possible
                if distance > 1 and player1.get_Pos()[0] > 3 and scene[8,player1.get_Pos()[0]-3] != '#':
                    if len(p1_jump_left) == 0 and len(p1_jump_right) == 0:
                        p1_jump_left.append(curframe)
                        p1_jump_count=0
                p1_move = False
            #jumpright
            if keyboard.is_pressed('e'):
                #check is the move is possible
                if player1.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player1.get_Pos()[0]+4] != '#':
                    if len(p1_jump_right) == 0 and len(p1_jump_left) == 0:
                        p1_jump_right.append(curframe)
                        p1_jump_count=0
            p1_move = False
    if p1_action:
        #attack
        if keyboard.is_pressed('z'):
            if len(p1_attack) == 0 and len(p1_block) == 0:
                p1_attack.append(curframe)
            p1_action =False 
        #block
        if keyboard.is_pressed('s'):
            if len(p1_block) == 0 and len(p1_attack) == 0:
                p1_block.append(curframe)
            p1_action =False 
        
    #player 2
    if p2_move:    
        #check which side the player is in the scene
        if player2.get_weap()=='d':
            #moveleft
            if keyboard.is_pressed('left'):
                #check is the move is possible
                if distance > 1 and player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-1] != '#':
                    if len(p2_move_right) > 1:
                        del p2_move_right[1:]
                    p2_move_left.append(curframe)
                p2_move = False
            #moveright
            if keyboard.is_pressed('right'):
                #check is the move is possible
                if player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+3] != '#':
                    if len(p2_move_left) > 1:
                        del p2_move_left[1:]
                    p2_move_right.append(curframe)
                p2_move = False

        #jumpleft
            if keyboard.is_pressed('l'):
                #check is the move is possible
                if distance > 2 and player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-3] != '#':
                    if len(p2_jump_left) == 0 and len(p2_jump_right) == 0:
                        p2_jump_left.append(curframe)
                        p2_jump_count=0
                p2_move = False
            #jumpright
            if keyboard.is_pressed('m'):
                #check is the move is possible
                if player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+5] != '#':
                    if len(p2_jump_right) == 0 and len(p2_jump_left) == 0:
                        p2_jump_right.append(curframe)
                        p2_jump_count=0
                p2_move = False
        else :
            #moveleft
            if keyboard.is_pressed('left'):
                #check is the move is possible
                if  player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-1] != '#':
                    if len(p2_move_right) > 1:
                        del p2_move_right[1:]
                    p2_move_left.append(curframe)
                p2_move = False
            #moveright
            if keyboard.is_pressed('right'):
                #check is the move is possible
                if distance > 1 and player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+3] != '#':
                    if len(p2_move_left) > 1:
                        del p2_move_left[1:]
                    p2_move_right.append(curframe)
                p2_move = False
            if keyboard.is_pressed('l'):
                #check is the move is possible
                if player2.get_Pos()[0] > 3 and scene[8,player2.get_Pos()[0]-3] != '#':
                    if len(p2_jump_left) == 0 and len(p2_jump_right) == 0:
                        p2_jump_left.append(curframe)
                        p2_jump_count=0
                p2_move = False
            #jumpright
            if keyboard.is_pressed('m'):
                #check is the move is possible
                if distance > 3 and player2.get_Pos()[0] < np.shape(scene)[1] - 3 and scene[8,player2.get_Pos()[0]+5] != '#':
                    if len(p2_jump_right) == 0 and len(p2_jump_left) == 0:
                        p2_jump_right.append(curframe)
                        p2_jump_count=0
                p2_move = False
    if p2_action:
        #attack
        if keyboard.is_pressed('o'):
            if len(p2_attack) == 0 and len(p2_block) == 0:
                p2_attack.append(curframe)
            p2_action =False
        #block
        if keyboard.is_pressed('p'):
            if len(p2_block) == 0 and len(p2_attack) == 0:
                p2_block.append(curframe)
            p2_action =False

# lunch actions regarding the stats
def actioner(curframe):
    global p1_jump_count,p2_jump_count,stat1,stat2,p1scoring,p2scoring,p1_move,p1_action,p2_move,p2_action
    #player1
    #moves
    if  len(p1_move_left) != 0:
        if curframe == (p1_move_left[0] + player1.get_MS()):
            p1_move_left.pop(0)
            player1.move_left()
            p1_move=True
    if  len(p1_move_right) != 0:
        if curframe == (p1_move_right[0] + player1.get_MS()):
            p1_move_right.pop(0)
            player1.move_right()
            p1_move=True
    if  len(p1_jump_left) != 0:
        if curframe == (p1_jump_left[0] + player1.get_MS()):
            p1_jump_left[0] = curframe + player1.get_MS() -1
            player1.jump_left(p1_jump_count)
            p1_jump_count+=1
            if p1_jump_count == 3:
                p1_jump_left.pop(0)
                p1_jump_count=0
                p1_move=True
    if  len(p1_jump_right) != 0:
        if curframe == (p1_jump_right[0] + player1.get_MS()):
            p1_jump_right[0] = curframe + player1.get_MS() -1
            player1.jump_right(p1_jump_count)
            p1_jump_count+=1
            if p1_jump_count == 3:
                p1_jump_right.pop(0)
                p1_jump_count=0
                p1_move=True
    #actions
    if len(p1_attack) != 0:
        if curframe == (p1_attack[0] + player1.get_Atk_Stats()[0]):
            p1_attack.pop(0)
            stat1=player1.attack()
            p1scoring = hitbox(player1.get_Pos()[0]+2, player2.get_Pos()[0], player1.get_Atk_Stats()[1], player2.get_Def_Stats()[0], p2_block)
            p1_action=True
    if len(p1_block) != 0:
        stat1=player1.block()
        if curframe == (p1_block[0] + player1.get_Def_Stats()[1]):
            p1_block.pop(0)
            p1_action=True

    #player2
    #moves
    if  len(p2_move_left) != 0:
        if curframe == (p2_move_left[0] + player2.get_MS()):
            p2_move_left.pop(0)
            player2.move_left()
            p2_move=True
    if  len(p2_move_right) != 0:
        if curframe == (p2_move_right[0] + player2.get_MS()):
            p2_move_right.pop(0)
            player2.move_right()
            p2_move=True
    if  len(p2_jump_left) != 0:
        if curframe == (p2_jump_left[0] + player2.get_MS()):
            p2_jump_left[0] = curframe + player2.get_MS() -1
            player2.jump_left(p2_jump_count)
            p2_jump_count+=1
            if p2_jump_count == 3:
                p2_jump_left.pop(0)
                p2_jump_count=0
                p2_move=True
    if  len(p2_jump_right) != 0:
        if curframe == (p2_jump_right[0] + player2.get_MS()):
            p2_jump_right[0] = curframe + player2.get_MS() -1
            player2.jump_right(p2_jump_count)
            p2_jump_count+=1
            if p2_jump_count == 3:
                p2_jump_right.pop(0)
                p2_jump_count=0
                p2_move=True
    #actions
    if len(p2_attack) != 0:
        if curframe == (p2_attack[0] + player2.get_Atk_Stats()[0]):
            p2_attack.pop(0)
            stat2=player2.attack()
            p2scoring = hitbox(player1.get_Pos()[0]+2, player2.get_Pos()[0], player2.get_Atk_Stats()[1], player2.get_Def_Stats()[0], p1_block)
            p2_action = True
    if len(p2_block) != 0:
        stat2=player2.block()
        if curframe == (p2_block[0] + player2.get_Def_Stats()[1]):
            p2_block.pop(0)
            p2_action = True


def hitbox(p1x,p2x,atk,blck,blocked):
    dist=abs(p1x-p2x)
    if len(blocked) == 0:
        if dist<=atk:
            return True
    elif dist<=(atk-blck+1):
        return True

def referee():
    global p1scoring,p2scoring, score1,score2, player1,player2
    if p1scoring and p2scoring:
        pass
    elif p1scoring :
        score1 +=1
        player1.reset()
        player2.reset()
        player1,player2 = make_scene()
        p1scoring=False
        os.system('cls')
        print('Le joueur 1 a reussit a marquer un point !')
        time.sleep(4)
    elif p2scoring:
        score2 +=1
        player1.reset()
        player2.reset()
        player1,player2 = make_scene()
        p2scoring=False
        os.system('cls')
        print('Le joueur 2 a reussit a marquer un point !')
        time.sleep(4)

def terminal():
    global ms,fps,current_frame,score1,score2,stat1,stat2,p1_move,p1_action,p2_move,p2_action
    #clear the terminal        
    os.system('cls')
    #fps
    print('FPS',clock.tick(fps)*1000/ms**2-1)
    print('frame courante',current_frame%fps)
    #actionners
    listener(current_frame,p1_move,p1_action,p2_move,p2_action)
    actioner(current_frame)    
    #frame counter
    current_frame+=1
    #refresh
    referee()
    update_scene(score1, score2, stat1,stat2)
    display()    
    print(' '*(len(ground)//2 -5) + 'Distance :' , abs((player1.get_Pos()[0]+2)-(player2.get_Pos()[0]-1)))
    if p1_action:
        stat1,stat2=player1.rest(),player2.rest()
    
    #ms
    time.sleep(ms/1000)


winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_ALIAS )
winsound.PlaySound("BackgroundMusic\InGame.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
actif = True 
done = True
while actif:
    terminal()
    if not done:
        winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_ALIAS )
        winsound.PlaySound("BackgroundMusic\MainMenu.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        pause_menu()
        winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_ALIAS )
        winsound.PlaySound("BackgroundMusic\InGame.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )