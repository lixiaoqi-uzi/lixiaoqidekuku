# 1：讲摄氏度转换为华氏度 F=(9/5)*C+12
C = float (input('请输入摄氏度'))
F = (9/5) *C +32
print('华氏度为',F)

# 2：计算圆柱体底面积和体积  area=radius*radius*pai    volume=area*length
import math
R = float (input('请输入圆柱体的半径'))
H = float (input('再输入圆柱体的高'))
A = R * R * math.pi
V = R * R * math.pi * H
print('圆柱体底面积为>%.2f'%A)
print('圆柱体体积为>%.2f'%V)

# 3:英尺转换为米  m=0.35*y
y = float (input('请输入英尺'))
m = y * 0.35
print('英尺转换为米数后为%.4f'%m)

# 4：计算把水从初始温度加热到最终温度所需能量 Q=M*(F1-F2)*4184
M = float (input('请输入以千克为单位的水量'))
F1 = float (input('请输入水的最终温度'))
F2 = float (input('请输入水的初始温度'))
Q = M * ( F1 - F2) * 4184
print('所需要的能量为%.4f'%Q)

# 5: 计算利息  利息=差额*（年利率/1200）
CE = float(input('请输入差额'))
NNL = float(input('请输入年利率'))
LX = CE * ( NNL / 1200)
print('利息为%.4f'%LX)

# 6:计算平均加速度 a=(V-V)/t
V1 = float(input('请输入末速度'))
V2 = float(input('请输入初速度'))
t = float(input('再输入所占用时间'))
a = ( V1 - V2) / t
print('平均加速度为%.2f'%a)

# 7:
 money = float(input('请输入每个月存款数'))
 a = money * ( 1 + 0.00417)
 b = ( a + money) * ( 1 + 0.00417)
 c = ( b + money) * ( 1 + 0.00417)
 d = ( c + money) * ( 1 + 0.00417)
 e = ( d + money) * ( 1 + 0.00417)
 f = ( e + money) * ( 1 + 0.00417)
 print('六个月后账户余额为',f)


# 8：求一个整数的各位数字相加的和
N = int(input('请输入一个整数'))
Q = N % 10 + (N //10)%10 + N // 100
print('和为:',Q)

# 9：
import math
r = float (input('请输入五边形中心到顶点距离'))
s = 2 * r * math.sin(math.pi/5)
area = 5 * s * s / ( 4 * math.tan(math.pi/5))
print('五边形面积为%.4f'%area)

# 10:将邮箱进行加密
import hashlib
email = 'choudd@126.com'
m = hashlib.md5()
b = email.encode(encoding = 'utf-8')
.update(b)
email_md5 = m.hexdigest()
print('md5加密前为：'+email)
print('md5加密后为：'+email_md5)

