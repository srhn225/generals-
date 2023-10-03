from generals import General,Grid,Plain, Swamp, Mountain, Farmer, Lieutenant, Commander,Player
def bomb(board,location,round):
    part=location.split(",")
    x=(int)(part[0])
    y=(int)(part[1])
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),  (0, 0),  (0, 1),
               (1, -1),  (1, 0),  (1, 1)]
    for offset in offsets:
        offset_row, offset_col = offset
        adjacent_row = x + offset_row
        adjacent_col =y + offset_col
        # 检查相邻点是否在数组范围内
        if 0 <= adjacent_row < len(board) and 0 <= adjacent_col < len(board[0]):
            if type(board[adjacent_row][adjacent_col]).__name__ == "Farmer" or type(board[adjacent_row][adjacent_col]).__name__ == "Lieutenant" or type(board[adjacent_row][adjacent_col]).__name__ == "Plain":
                board[adjacent_row][adjacent_col]=Plain()
                board[adjacent_row][adjacent_col].isradiation=True
                board[adjacent_row][adjacent_col].radiatedround=round
            elif type(board[adjacent_row][adjacent_col]).__name__ == "Swamp":
                board[adjacent_row][adjacent_col]=Swamp()
                board[adjacent_row][adjacent_col].isradiation=True
                board[adjacent_row][adjacent_col].radiatedround=round
            elif type(board[adjacent_row][adjacent_col]).__name__ == "Mountain":
                board[adjacent_row][adjacent_col]=Mountain()
                board[adjacent_row][adjacent_col].isradiation=True
                board[adjacent_row][adjacent_col].radiatedround=round
            elif type(board[adjacent_row][adjacent_col]).__name__ == "Commander":
                board[adjacent_row][adjacent_col].army=board[adjacent_row][adjacent_col].army//2
                board[adjacent_row][adjacent_col].isradiation=True
                board[adjacent_row][adjacent_col].radiatedround=round
            else:
                print("Error:类型错误")

def strengthen(board,location,round):
    part=location.split(",")
    x=(int)(part[0])
    y=(int)(part[1])
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),  (0, 0),  (0, 1),
               (1, -1),  (1, 0),  (1, 1)]
    for offset in offsets:
        offset_row, offset_col = offset
        adjacent_row = x + offset_row
        adjacent_col =y + offset_col
        # 检查相邻点是否在数组范围内
        if 0 <= adjacent_row < len(board) and 0 <= adjacent_col < len(board[0]):
            board[adjacent_row][adjacent_col].isstrengthen=True
            board[adjacent_row][adjacent_col].defence*=3
            board[adjacent_row][adjacent_col].attack*=3
            board[adjacent_row][adjacent_col].strengthenround=round
def tp(board,location,dest,player,round):
    part=location.split(",")
    x=(int)(part[0])
    y=(int)(part[1])
    destpart=dest.split(",")
    destx=(int)(destpart[0])
    desty=(int)(destpart[1])
    if type(board[destx][desty]).__name__ == "Farmer" or type(board[destx][desty]).__name__ == "Lieutenant" or type(board[destx][desty]).__name__ == "Commander":
        print("Error:传送失败")
        return
    elif type(board[destx][desty]).__name__ == "Mountain":
        if not player.ismountain:
            print("Error:传送失败")
            return
    if player.belong!=board[x][y].belong:
        print("Error:只能传送自己的军队")
    tparmy=board[x][y].army
    board[destx][desty].army=tparmy
    board[destx][desty].belong=board[x][y].belong
    board[x][y].army=0
    stop(board[destx][desty],round)
def timestop(board,location,round):
    part=location.split(",")
    x=(int)(part[0])
    y=(int)(part[1])
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),  (0, 0),  (0, 1),
               (1, -1),  (1, 0),  (1, 1)]
    for offset in offsets:
        offset_row, offset_col = offset
        adjacent_row = x + offset_row
        adjacent_col =y + offset_col
        # 检查相邻点是否在数组范围内
        if 0 <= adjacent_row < len(board) and 0 <= adjacent_col < len(board[0]):
            stop(board[adjacent_row][adjacent_col],round)
def stop(grid,round):
    grid.isstopped=True
    grid.stopround=round
def Leadership(arr, center_row, center_col,player,round):
    for i in range(center_row - 2, center_row + 3):
        for j in range(center_col - 2, center_col + 3):
            # 检查索引是否在数组范围内
            if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
                if arr[i][j].belong==player.belong:
                    arr[i][j].attack*=1.5
                    arr[i][j].leadershipround=round
                    arr[i][j].isleadership=True
def Defense(arr, center_row, center_col,player,round):
    for i in range(center_row - 2, center_row + 3):
        for j in range(center_col - 2, center_col + 3):
            # 检查索引是否在数组范围内
            if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
                if arr[i][j].belong==player.belong:
                    arr[i][j].defence*=1.5
                    arr[i][j].defenceround=round
                    arr[i][j].isdefense=True
def Weaken(arr, center_row, center_col,player,round):
    for i in range(center_row - 2, center_row + 3):
        for j in range(center_col - 2, center_col + 3):
            # 检查索引是否在数组范围内
            if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
                if arr[i][j].belong!=player.belong:
                    arr[i][j].attack*=0.75
                    arr[i][j].defence*=0.75
                    arr[i][j].weakenround=round
                    arr[i][j].isweaken=True
def Raid(board,location,round,player,x,y):
    part=location.split(",")
    stx=(int)(part[0])
    sty=(int)(part[1])
    if type(board[x][y]).__name__=="Lieutenant" or type(board[x][y]).__name__=="Commander" or type(board[x][y]).__name__=="Farmer":
        print("Error:不可到达此位置")
        return
    if type(board[x][y]).__name__=="Mountain":
        if not player.ismountain:
            print("Error:不可到达此位置")
            return
    if board[x][y].belong!=board[stx][sty].belong:
        if board[stx][sty].army*board[stx][sty].attack<=board[x][y].army*board[x][y].defence:
            print("Error:不可到达此位置")
            return
        else:
            newarmynum=(board[stx][sty].army*board[stx][sty].attack-board[x][y].army*board[x][y].defence)//board[stx][sty].attack
            if type(board[x][y]).__name__=="Mountain":
                nowon=board[stx][sty].nowon
                if type(nowon).__name__=='Grid':
                    nowon=Plain()
                board[x][y]=board[stx][sty]
                board[x][y].nowon=Mountain()
                board[x][y].army=newarmynum
                board[stx][sty]=nowon
                board[stx][sty].army=0
                board[stx][sty].belong=player.belong
                
            elif type(board[x][y]).__name__=="Plain":
                nowon=board[stx][sty].nowon
                if type(nowon).__name__=='Grid':
                    nowon=Plain()
                board[x][y]=board[stx][sty]
                board[x][y].nowon=Plain()
                board[x][y].army=newarmynum
                board[stx][sty]=nowon
                board[stx][sty].army=0
                board[stx][sty].belong=player.belong
            elif type(board[x][y]).__name__=="Swamp":
                nowon=board[stx][sty].nowon
                if type(nowon).__name__=='Grid':
                    nowon=Plain()
                board[x][y]=board[stx][sty]
                board[x][y].nowon=Swamp()
                board[x][y].army=newarmynum
                board[stx][sty]=nowon
                board[stx][sty].army=0
                board[stx][sty].belong=player.belong
    elif board[x][y].belong==board[stx][sty].belong:
            newarmynum=board[stx][sty].army+board[x][y].army
            if type(board[x][y]).__name__=="Mountain":
                nowon=board[stx][sty].nowon
                if type(nowon).__name__=='Grid':
                    nowon=Plain()
                board[x][y]=board[stx][sty]
                board[x][y].nowon=Mountain()
                board[x][y].army=newarmynum
                board[stx][sty]=nowon
                board[stx][sty].army=0
                board[stx][sty].belong=player.belong
                
            elif type(board[x][y]).__name__=="Plain":
                nowon=board[stx][sty].nowon
                if type(nowon).__name__=='Grid':
                    nowon=Plain()
                board[x][y]=board[stx][sty]
                board[x][y].nowon=Plain()
                board[x][y].army=newarmynum
                board[stx][sty]=nowon
                board[stx][sty].army=0
                board[stx][sty].belong=player.belong
            elif type(board[x][y]).__name__=="Swamp":
                nowon=board[stx][sty].nowon
                if type(nowon).__name__=='Grid':
                    nowon=Plain()
                board[x][y]=board[stx][sty]
                board[x][y].nowon=Swamp()
                board[x][y].army=newarmynum
                board[stx][sty]=nowon
                board[stx][sty].army=0
                board[stx][sty].belong=player.belong