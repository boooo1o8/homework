'''
题⽬：猴⼦吃桃问题：猴⼦第⼀天摘下若⼲个桃⼦，当即吃了⼀半，还不瘾，⼜多吃了⼀个第⼆天早上⼜将剩下的桃⼦吃掉⼀半，⼜多吃了⼀个。以后每天早上都吃了前⼀天剩下的⼀半零⼀个。到第10天早上想再吃时，⻅只剩下⼀个桃⼦了。求第⼀天共摘了多少。
程序分析：采取逆向思维的⽅法，从后往前推断。
'''

day = 10
peach = 1

while day >= 1:
    print(f"{day}:{peach}")
    peach = (peach+1)*2
    day -= 1