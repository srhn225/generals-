class Grid:
    def __init__(self):
        self.army=0
        self.belong=2  #0和1代表占领方,2表示未被占领
        self.defence=1
        self.attack=1
        self.isradiation=False
        self.isstrengthen=False
        self.strengthenround=0
        self.radiatedround=0
        self.isstopped=False
        self.stopround=0
    def variation(self,round,player1,player2):
        pass
    def to_string(self):
        return self.army,self.belong,"Grid"
    def print_info(self):
        print("army:",self.army,"belong:",self.belong,"type:",self.type,"attack:",self.attack,"defence:",self.defence)
    def get_radiated(self):
        if self.army > 3:
            self.army -= 3
        else:
            self.army = 0


class Plain(Grid):
    def __init__(self):
        super().__init__()
    def variation(self,round,player1,player2):
        if self.belong!=2 and round % 25 == 0:
            self.army += 1
    def to_string(self):
        return self.army,self.belong,"Plain"

class Swamp(Grid):
    def __init__(self):
        super().__init__()
    def variation(self,round,player1,player2):
        if self.army!=0:
            if self.belong==0:
                if not player1.isswampde:
                    self.army -= 1   
                else:
                    pass
        if self.belong==1:
                if not player2.isswampde:
                    self.army -= 1   
                else:
                    pass
    def to_string(self):
        return self.army,self.belong,"Swamp"

class Mountain(Grid):
    def __init__(self):
        super().__init__()
    def variation(self,round,player1,player2):
        if self.belong!=2 and round % 25 == 0:
            self.army += 1
    def to_string(self):
        return self.army,self.belong,"Mountain"
class General(Grid):
    def __init__(self):
        super().__init__()
    def variation():
        pass
    def to_string(self):
        return self.army,self.belong,"General"
    
class Farmer(General):
    def __init__(self,army):
        super().__init__()
        self.army=army
        self.productlevel=1
        self.nowon=Grid()
    def variation(self,round,player1,player2):
        if self.belong!=2 and round % 25 == 0:
            self.army += 1
    def to_string(self):
        return self.army,self.belong,"Farmer"
    def print_info(self):
        print("army:",self.army,"belong:",self.belong,"type:",self.type,"attack:",self.attack,"defence:",self.defence,"productlevel:",self.productlevel)
class Lieutenant(General):
    def __init__(self,army):
        super().__init__()
        self.army=army
        self.productlevel=1
        self.actpoint=1
        self.nowon=Grid()
    def variation(self,round,player1,player2):
        if self.belong!=2:
            self.army += self.productlevel
    def to_string(self):
        return self.army,self.belong,"Lieutenant"
    def print_info(self):
        print("army:",self.army,"belong:",self.belong,"type:",self.type,"attack:",self.attack,"defence:",self.defence,"productlevel:",self.productlevel)
class Commander(General):
    def __init__(self,belong):
        super().__init__()
        self.belong=belong
        self.productlevel=1
        self.actpoint=1
        self.nowon=Grid()
    def variation(self,round,player1,player2):
        if self.belong!=2:
            self.army += self.productlevel
    def to_string(self):
        return self.army,self.belong,"Commander"
    def print_info(self):
        print("army:",self.army,"belong:",self.belong,"type:",self.type,"attack:",self.attack,"defence:",self.defence,"productlevel:",self.productlevel)
class Player:
    def __init__(self,belong):
        self.belong=belong#区分两个玩家
        self.money=0#初始金额为0
        self.generalactpoint=1#每回合移动一步将军
        self.generalactpointnow=1
        self.armyactpoint=2#move 2 armies per round
        self.armyactpointnow=2#move 2 armies per round 
        self.ismountain=False#can or cannot climb
        self.isswampde=True#swamp decrease
        self.ishitech=False#permission of super weapon
        self.hitechround=0
    def upgrade_mountain_climbing(self):
        # 解锁攀岩能力
        self.ismountain = True

    def disable_swamp_decrease(self):
        # 免疫沼泽减少效果
        self.isswampde = False

    def unlock_super_weapon(self,round):
        # 解锁超级武器
        self.ishitech = True
        self.hitechround = round
