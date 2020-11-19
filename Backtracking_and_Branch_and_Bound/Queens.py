'''
在n*n格的棋盘撒上放置彼此不受攻击的n个皇后。按照国际象棋的规矩，
皇后可以攻击与之处在同一行或者同一列或者同一斜线上的棋子。
N皇后问题等价于在n * n格的棋盘上放置n个皇后，任何2个皇后
不放在同一行同一列同一斜线上。
'''

#name:queens
#全排列函数
per_result = []
def per(lst,s,e):
    if s == e:
        per_result.append(list(lst))
    else:
        for i in range(s,e):
            lst[i],lst[s] = lst[s],lst[i]#试探
            per(lst,s+1,e)#递归
            lst[i],lst[s] = lst[s],lst[i]#回溯
#剪枝函数
#args:[1,2,3,4]
#return true or false
def shear(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if(abs(lst[j] - lst[i]) == abs(j-i)):
                result += 1
    if(result > 0):
        return True
    else:
        return False
#格式打印函数
def stamp(st):
    for i in st:
        for j in range(len(i)):
            a = ("."*(i[j]-1)+"#"+"."*(len(i)-i[j]))
            print(a,"\t","第{}个皇后放在棋盘的第{}列".format(j+1,i[j]))
        print(" ")#负责空行
num = eval(input("请输入皇后的个数："))
lst = [i+1 for i in range(num)]
per(lst,0,num)
queen_lst = []
for i in per_result:
    if(shear(i) == False):
        queen_lst.append(i)
stamp(queen_lst)
print("共{:d}种可能".format(len(queen_lst)))
