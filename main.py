from generals import General,Grid,Plain, Swamp, Mountain, Farmer, Lieutenant, Commander,Player
import board
import command
round=0
board.generate_generals(board.grid)
board.generate_swamp(board.grid)
board.generate_mountain(board.grid)
board.generate_lieutenant(board.grid)
board.generate_farmer(board.grid)
board.generate_plain(board.grid)
player1=Player(0)
player2=Player(1)
while True:
    round+=1
    command.print_board(board.grid)
    print("玩家1行动,目前金钱："+str(player1.money))
    while True:
        location,nowcommand=command.read_command()
        if location=="end" or location=="":
            break
        command.execute_command(board.grid,location,nowcommand,player1)
        
    print("玩家2行动,目前金钱："+str(player2.money))
    while True:   
        
        location,nowcommand=command.read_command()
        if location=="end" or location=="":
            break
        command.execute_command(board.grid,location,nowcommand,player2) 
        
    command.update_round(board.grid,round,player1,player2)