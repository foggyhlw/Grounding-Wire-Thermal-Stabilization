#短路前导体温度为+70℃时导体热稳定系数参数表
dictC=dict([('alumium',87),('copper',171),('iron',60)])
print(dictC)
#常数K
dictK=dict([('alumium',222e6),('copper',522e6)])
print(dictK)
#常数τ
dictT=dict([('alumium',245),('copper',235)])
#极限校验温度
dictTemp=dict([('alumium',200),('copper',300),('iron',300)])
#若导体短路前温度不是+70℃，按下式计算C （仅限铜和铝）
def calculate_C(material,t1,t2):
	from math import log
	return (dictK[material]*log((dictT[material]+t2)/(dictT[material]+t1))/10000)**0.5


wiretype='JLB20A-120'
import sqlite3
conn = sqlite3.connect('wires.db')
cursor = conn.cursor()
<<<<<<< HEAD
cursor.execute("select * from wires where N= 'LGJ-240/30'")
=======
cursor.execute("select n,alS,ironS from wire where n = '{0}'".format(wiretype) )
>>>>>>> 37a370f9cc126e3a55b30928998863e0dccae3ef
values = cursor.fetchall()
cursor.close()
conn.close()
	
if values[0][1]=='':
	material='iron'
	S=float(values[0][2])
else:
	material='alumium'
	S=float(values[0][1])
	Si = float(values[0][2])
print(material,S,Si)

#校验热稳定，返回能承受的最大短路电流值,t为热校验时间，t1为初始温度
def check_stabilization(material,S,t,t1=70):
	#当是钢材时，没有相应计算C的公式，按照初始70度，最高300度计算
	if material == 'iron':
		print(dictC[material])
		return (S*dictC[material])**2/t/1000000
	#当时铜或铝时，如果给定了校验初始温度，则重新计算C值
	if material == 'alumium':
		C=calculate_C(material,t1,dictTemp[material])	
		return (S*C)**2/t/1000000
	if material == 'copper':
		C=calculate_C(material,t1,dictTemp[material])	
		return (S*C)**2/t/1000000

print(check_stabilization(material,S,0.5,70))