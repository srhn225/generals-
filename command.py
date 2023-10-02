from generals import General,Grid,Plain, Swamp, Mountain, Farmer, Lieutenant, Commander,Player
from colorama import init, Back,Fore,Style
import skills
import constant
def print_board(board):
    for num in range(constant.col):
        print("{:3}".format(num), end=' ')
    print()
    init()
    init_fore_color = Fore.RESET
    init_back_color = Back.RESET
    rownum=0
    for row in board:
        rownum_f = "{:2}".format(rownum)
        print(rownum_f, end='')
        rownum+=1
        for cell in row:
            num, belong, name = cell.to_string()
            bg_color = Fore.WHITE
            # 根据 belong 设置背景色
            if belong == 0:
                bg_color = Back.RED
            elif belong == 1:
                bg_color = Back.BLUE
            else:
                bg_color = Back.WHITE
            # 根据 name 设置字体颜色
            font_color = Fore.WHITE
            if name == 'Swamp':
                font_color = Fore.LIGHTMAGENTA_EX
            elif name == 'Mountain':
                font_color = Fore.YELLOW
            elif name == 'Farmer':
                font_color = Fore.GREEN
            elif name == 'Lieutenant':
                font_color = Fore.CYAN
            elif name == 'Commander':
                font_color = Fore.BLACK
            # 打印 num，带有对应的背景色和字体颜色
            cell_output = "{:3}".format(num)
            print(f"{bg_color}{font_color}{cell_output}", end=" ")
            
        # 换行
        print(init_back_color + init_fore_color)
def read_command():
    location=input("请输入要选择的格子：")
    command=input("请输入要执行的操作：")
    return location,command

def execute_command(board,location,command,player):
    if(location=='none'):
        indexnow=(int)(command[5])#科技升级
        if indexnow == 1:
            if player.armyactpoint==2:
                if player.money>=constant.army_movement_T1:
                    player.armyactpoint+=1
                    player.armyactpointnow+=1
                    player.money-=constant.army_movement_T1
                else:
                    print("你没钱升级了")

            elif player.armyactpoint==3:
                if player.money>=constant.army_movement_T2:
                    player.armyactpoint+=2
                    player.armyactpointnow+=2
                    player.money-=constant.army_movement_T2
                else:
                    print("你没钱升级了")
            elif player.armyactpoint==5:
                print("Error:不能再升级")
            
        elif indexnow == 2:
            if player.generalactpoint==1:
                if player.money>=constant.general_movement_T1:
                    player.generalactpoint+=1
                    player.generalactpointnow+=1
                    player.money-=constant.general_movement_T1
                else:
                    print("你没钱升级了")

            elif player.generalactpoint==2:
                if player.money>=constant.general_movement_T2:
                    player.generalactpoint+=2
                    player.generalactpointnow+=2
                    player.money-=constant.general_movement_T2
                else:
                    print("你没钱升级了")
            elif player.armyactpoint==4:
                print("Error:不能再升级")
            
        elif indexnow == 3:
            if player.ismountain==False:
                if player.money>=constant.mountaineering:
                    player.upgrade_mountain_climbing()
                    player.money-=constant.mountaineering
                else:
                    print("Error:钱不够升级")
            else:
                print("Error:已经升级")
            
        elif indexnow ==  4:
            if player.ishitech==False:
                if player.money>=constant.unlock_super_weapon:
                    player.unlock_super_weapon(round)
                    player.money-=constant.unlock_super_weapon
                else:
                    print("Error:钱不够升级")
            else:
                print("Error:已经升级")
        elif indexnow == 5:
            if player.isswampde==True:
                if player.money>=constant.swamp_immunity:
                    player.disable_swamp_decrease()
                    player.money-=constant.swamp_immunity
                else:
                    print("Error:钱不够升级")
            else:
                print("Error:已经升级")
        else:
            print("Error:错误的升级方案")

    else:
        if command.find("update") != -1:
            indexnow=(int)(command[7])#指定将军升级
            part=location.split(",")
            x=(int)(part[0])
            y=(int)(part[1])
            if board[x][y].belong!=player.belong:
                print("Error:只能升级自己的将军")
            if indexnow==1:
                if type(board[x][y]).__name__=="Farmer":
                    if board[x][y].productlevel==1:
                        if player.money>=constant.farmer_production_T1:
                            board[x][y].productlevel=2
                            player.money-=constant.farmer_production_T1
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==2:
                        if player.money>=constant.farmer_production_T2:
                            board[x][y].productlevel=4
                            player.money-=constant.farmer_production_T2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==4:
                        if player.money>=constant.farmer_production_T3:
                            board[x][y].productlevel=6
                            player.money-=constant.farmer_production_T3
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==6:
                        print("Error:不能再升级")
                elif type(board[x][y]).__name__=="Lieutenant":
                    if board[x][y].productlevel==1:
                        if player.money>=constant.lieutenant_production_T1:
                            board[x][y].productlevel=2
                            player.money-=constant.lieutenant_production_T1
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==2:
                        if player.money>=constant.lieutenant_production_T2:
                            board[x][y].productlevel=4
                            player.money-=constant.lieutenant_production_T2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==4:
                        print("Error:不能再升级")
                elif type(board[x][y]).__name__=="Commander":
                    if board[x][y].productlevel==1:
                        if player.money>=constant.lieutenant_production_T1/2:
                            board[x][y].productlevel=2
                            player.money-=constant.lieutenant_production_T1/2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==2:
                        if player.money>=constant.lieutenant_production_T2/2:
                            board[x][y].productlevel=4
                            player.money-=constant.lieutenant_production_T2/2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==4:
                        print("Error:不能再升级")
                else:
                    print("Error:错误的位置")
            elif indexnow==2:
                if type(board[x][y]).__name__=="Farmer":
                    if board[x][y].defence==1:
                        if player.money>=constant.farmer_defense_T1:
                            board[x][y].defence=1.5
                            player.money-=constant.farmer_defense_T1
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].defence==1.5:
                        if player.money>=constant.farmer_defense_T2:
                            board[x][y].defence=2
                            player.money-=constant.farmer_defense_T2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].defence==2:
                        if player.money>=constant.farmer_defense_T3:
                            board[x][y].defence=3
                            player.money-=constant.farmer_defense_T3
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==3:
                        print("Error:不能再升级")
                elif type(board[x][y]).__name__=="Lieutenant":
                    if board[x][y].defence==1:
                        if player.money>=constant.lieutenant_defense_T1:
                            board[x][y].defence=2
                            player.money-=constant.lieutenant_defense_T1
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].defence==2:
                        if player.money>=constant.lieutenant_defense_T2:
                            board[x][y].defence=3
                            player.money-=constant.lieutenant_defense_T2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==3:
                        print("Error:不能再升级")
                elif type(board[x][y]).__name__=="Commander":
                    if board[x][y].defence==1:
                        if player.money>=constant.lieutenant_defense_T1/2:
                            board[x][y].defence=2
                            player.money-=constant.lieutenant_defense_T1/2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].defence==2:
                        if player.money>=constant.lieutenant_defense_T2/2:
                            board[x][y].defence=3
                            player.money-=constant.lieutenant_defense_T2/2
                        else:
                            print("Error:钱不够升级")
                    elif board[x][y].productlevel==3:
                        print("Error:不能再升级")
                else:
                    print("Error:错误的位置")
            else:
                print("Error:错误的升级方案")
        elif command=="print":
            part=location.split(",")
            x=(int)(part[0])
            y=(int)(part[1])
            board[x][y].print_info()
        elif command=="bomb":
            if player.ishitech and round-player.hitechround>=100:
                skills.bomb(board,location,round)
            else:
                print("Error:不可用")
        elif command=="strengthen":
            if player.ishitech and round-player.hitechround>=100:
                skills.strengthen(board,location,round)
            else:
                print("Error:不可用")
        elif command=="timestop":
            if player.ishitech and round-player.hitechround>=100:
                skills.timestop(board,location,round)
            else:
                print("Error:不可用")
        elif command[0]=="t" and command[1]=="p":
            if player.ishitech and round-player.hitechround>=100:
                _, xy = command.split(' ')
                skills.tp(board,location,xy,player,round)
            else:
                print("Error:不可用")
        else:
            part=location.split(",")
            x=(int)(part[0])
            y=(int)(part[1])
            if board[x][y].isstopped:
                print("Error:时间停止，不能操作")
                return
            if command.find("gen") != -1:#将军移动
                if player.generalactpointnow>0:
                    player.generalactpointnow-=1
                    commandnow=command[4:]
                    general_move(board,location,commandnow,player)
                else:
                    print("没有将军行动点")
            else:
                if player.armyactpointnow>0:
                    player.armyactpointnow-=1
                    command_parts = command.split()
                    direction = command_parts[1]
                    num=(int)(command_parts[0])
                    army_move(board,location,num,direction,player)#军队移动
                else:
                    print("没有军队行动点")

        
def army_move(board,location,num,way,player):#核心：军队移动和攻击逻辑
    part=location.split(",")
    x=(int)(part[0])
    y=(int)(part[1])
    if board[x][y].belong!=player.belong:
        print("非法操作")
        return
    if num>=board[x][y].army-1:
        num=board[x][y].army-1#最多移动这么多军队
    dx,dy=0,0
    if way=='up':
        dx,dy=-1,0
    elif way=='down':
        dx,dy=1,0
    elif way=='left':
        dx,dy=0,-1
    elif way=='right':
        dx,dy=0,1
    if num<=0:
        print("Error:非法的军队数量")
        return
    if x>=constant.row or x<0 or y>=constant.col or y<0:
        print("Error:非法的位置")
        return
    if x+dx>=constant.row or x+dx<0 or y+dy>=constant.col or y+dy<0:
        print("Error:越界的移动")
        return
    if type(board[x+dx][y+dy]).__name__=='Mountain' and player.ismountain==False:
        print("Error:不能跨越山脉")
        return
    if board[x+dx][y+dy].belong==board[x][y].belong :
            board[x+dx][y+dy].army+=num
            board[x][y].army-=num
    elif board[x+dx][y+dy].belong==2:
            if type(board[x+dx][y+dy]).__name__=='Plain' or type(board[x+dx][y+dy]).__name__=='Swamp' or type(board[x+dx][y+dy]).__name__=='Mountain':
                board[x+dx][y+dy].army+=num 
                board[x+dx][y+dy].belong=board[x][y].belong
                board[x][y].army-=num
            elif type(board[x+dx][y+dy]).__name__=='Lieutenant' or type(board[x+dx][y+dy]).__name__=='Farmer':
                if num*board[x][y].attack<=board[x+dx][y+dy].army:
                    board[x+dx][y+dy].army-=num*board[x][y].attack
                    board[x][y].army-=num
                else:
                    board[x][y].army-=num
                    newnum=(num*board[x][y].attack-board[x+dx][y+dy].army)//board[x][y].attack
                    board[x+dx][y+dy].army=newnum
                    board[x+dx][y+dy].belong=board[x][y].belong
            else:
                print("Error:未知错误"+type(board[x+dx][y+dy]).__name__)
    elif board[x+dx][y+dy].belong==1-board[x][y].belong:#enemy
            if type(board[x+dx][y+dy]).__name__=='Plain' or type(board[x+dx][y+dy]).__name__=='Swamp' or type(board[x+dx][y+dy]).__name__=='Mountain':
                if num*board[x][y].attack<=board[x+dx][y+dy].army*board[x+dx][y+dy].defence:
                    board[x+dx][y+dy].army=(board[x+dx][y+dy].army*board[x+dx][y+dy].defence-num*board[x][y].attack)//board[x+dx][y+dy].defence
                    board[x][y].army-=num
                else:
                    board[x][y].army-=num
                    newnum=(num*board[x][y].attack-board[x+dx][y+dy].army*board[x+dx][y+dy].defence)//board[x][y].attack
                    board[x+dx][y+dy].army=newnum
                    board[x+dx][y+dy].belong=board[x][y].belong
            elif type(board[x+dx][y+dy]).__name__=='Lieutenant' or type(board[x+dx][y+dy]).__name__=='Farmer':
                if num*board[x][y].attack<=board[x+dx][y+dy].army*board[x+dx][y+dy].defence:
                    board[x+dx][y+dy].army=(board[x+dx][y+dy].army*board[x+dx][y+dy].defence-num*board[x][y].attack)//board[x+dx][y+dy].defence
                    board[x][y].army-=num
                else:
                    board[x][y].army-=num
                    newnum=(num*board[x][y].attack-board[x+dx][y+dy].army*board[x+dx][y+dy].defence)//board[x][y].attack
                    board[x+dx][y+dy].army=newnum
                    board[x+dx][y+dy].belong=board[x][y].belong
def general_move(board,location,way,player):
    part=location.split(",")
    x=(int)(part[0])
    y=(int)(part[1])
    dx,dy=0,0
    if type(board[x][y]).__name__=='Plain' or type(board[x][y]).__name__=='Swamp' or type(board[x][y]).__name__=='Mountain' or board[x][y].belong!=player.belong:
        print("Error:非法操作")
        return
    if way=='up':
        dx,dy=-1,0
    elif way=='down':
        dx,dy=1,0
    elif way=='left':
        dx,dy=0,-1
    elif way=='right':
        dx,dy=0,1
    if x>=constant.row or x<0 or y>=constant.col or y<0:
        print("Error:非法的位置")
        return
    if x+dx>=constant.row or x+dx<0 or y+dy>=constant.col or y+dy<0:
        print("Error:越界的移动")
        return
    if type(board[x+dx][y+dy]).__name__=='Mountain' and player.ismountain==False:
        print("Error:不能跨越山脉")
        return
    if board[x+dx][y+dy].belong!=board[x][y].belong:
        print("Error:不能移动到不属于自己的的领地")
        return
    if type(board[x+dx][y+dy]).__name__=='Commander' or type(board[x+dx][y+dy]).__name__=='Lieutenant' or type(board[x+dx][y+dy]).__name__=='Farmer':
        print("Error:不能移动到其他将军")
        return
    if type(board[x+dx][y+dy]).__name__=='Plain':
        newGen=board[x][y]
        armynow=board[x][y].army
        newGen.army=board[x+dx][y+dy].army
        if type(board[x][y].nowon).__name__=='Grid':
            newgrid=Plain()
        else:
            newgrid=board[x][y].nowon
        newgrid.army=armynow
        newgrid.belong=board[x][y].belong
        newGen.nowon=Plain()
        board[x+dx][y+dy]=newGen
        board[x][y]=newgrid
    elif type(board[x+dx][y+dy]).__name__=='Swamp':
        newGen=board[x][y]
        armynow=board[x][y].army
        newGen.army=board[x+dx][y+dy].army
        newgrid=board[x][y].nowon
        newgrid.army=armynow
        newgrid.belong=board[x][y].belong
        newGen.nowon=Swamp()
        board[x+dx][y+dy]=newGen
        board[x][y]=newgrid
    elif type(board[x+dx][y+dy]).__name__=='Mountain':
        newGen=board[x][y]
        armynow=board[x][y].army
        newGen.army=board[x+dx][y+dy].army
        newgrid=board[x][y].nowon
        newgrid.army=armynow
        newgrid.belong=board[x][y].belong
        newGen.nowon=Mountain()
        board[x+dx][y+dy]=newGen
        board[x][y]=newgrid    
def update_round(board,round,player1,player2):
    money_for_player1=0
    money_for_player2=0
    for row in board:
        for cell in row:
            if not cell.isstopped:
                cell.variation(round,player1,player2)
            if cell.isradiation:
                cell.get_radiated()
                if(round-cell.radiatedround>=10):
                    cell.isradiation=False
            if cell.isstrengthen:
                if(round-cell.strengthenround>=5):
                    cell.isstrengthen=False
                    cell.attack=cell.attack//3
                    cell.defense=cell.defense//3
            if cell.isstopped:
                if(round-cell.stopround>=5):
                    cell.isstopped=False
            if type(cell).__name__=='Farmer':
                if cell.belong==0:
                    money_for_player1+=cell.productlevel
                elif cell.belong==1:
                    money_for_player2+=cell.productlevel
    player1.armyactpointnow=player1.armyactpoint
    player1.generalactpointnow=player1.generalactpoint
    player2.armyactpointnow=player2.armyactpoint
    player2.generalactpointnow=player2.generalactpoint
    player1.money+=money_for_player1
    player2.money+=money_for_player2
