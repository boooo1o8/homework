'''
题⽬：按逗号分隔列表[1,2,3,4,5]中的元素。
预期输出：1，2，3，4，5
程序分析：字符串的join⽅法
'''

a = [1, 2, 3, 4, 5]
print(','.join(str(x) for x in a))
