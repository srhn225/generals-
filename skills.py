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
def traverse_5x5_region(arr, center_row, center_col):
    for i in range(center_row - 2, center_row + 3):
        for j in range(center_col - 2, center_col + 3):
            # 检查索引是否在数组范围内
            if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
                print(arr[i][j])