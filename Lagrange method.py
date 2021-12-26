a=2
b=-1
c=5
d=-4
f=-8
g=-6

k1=d/(2*a)
k2=f/(2*a)
k3=b-(pow(d,2)/(4*a))
k4=(2*a*g-d*f)/(4*a*b-pow(d,2))
k5=1/(4*a)*(4*a*c-pow(f,2)-(pow((2*a*g-d*f), 2)/(4*a*b-d*d)))

print("k1=", k1)
print("k2=", k2)
print("k3=", k3)
print("k4=", k4)
print("k5=", k5)

koef=[a, k3, k5]
p=0
for i in range(3):
    if koef[i]>0:
        p+=1
r=3-koef.count(0)

print("\nРанг r=", r)
print("Додатний індекс інерції p=", p)
print("Від'ємний індекс інерції q=", r-p)
print("Сигнатура s=", p-(r-p))
    