# generals
## 命令行中的操作
- `location=x,y`
  - `command=x up/down/left/right`
    - 让位置 (x, y) 的若干兵向某个方向移动（x 可以是任意整数）。
  - `command=gen up/down/left/right`
    - 让位置 (x, y) 的将领向某个方向移动。
  - `command=gen sk Raid x,y/Breakthrough x,y/Leadership/Defense/Weaken`
    - 让位置 (x, y) 的将领执行特定的技能：Raid x,y、Breakthrough x,y、Leadership、Defense、Weaken。
  - `command=update 1/2`
    - 将位置 (x, y) 的将领升级，升级类型为 1 或 2（产量、防御）。
  - `command=tech 1/2/3/4/5`（行动力、将军行动力、攀岩、解锁超武、免疫沼泽）
    - 解锁指定科技：1、2、3、4、5。
  - `location=end/""`
    - 结束这一回合。
  - `location=x,y`
    - `command=print`
      - 打印位置 (x, y) 的信息。
  - `location=x,y`
    - `command=bomb/strengthen/tp x,y/timestop`
      - 使用超级武器：bomb、strengthen、tp x,y、timestop。
  - `location=x,y`
    - `command=newgen`
      - 招募新将领
