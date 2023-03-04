import random #para poder usar el metodo random

who = ['The dog','My grandma','His turtle','My bird']; #arreglos []
action = ['ate','peed','crushed','broke'];
what = ['my homework', 'the keys', 'the car'];
when = ['before the class','right on time','when I finished','during my lunch','while I was praying'];

#recordando que en python las variales se pueden declarar solo con el nombre como lo es who, action, what, when
#para agregar elementos en el arreglo se puede hacer who.appen("my sister").

r1 = random.randint (0,len(who)-1) #para buscar cualquier posición aleatearoia dentro del arreglo
print(r1)
r2 = random.choice(action) #recorre aleatoreamente el arreglo action
print(r2)
r3 = round(random.random()*(len(what)-1)) #random.random arroja un valor decimal entre 0 y 1 sin incluir estos numeros.. si no se usa round se genera un error (probar)
print(round(r3)) #round para redondear los decimales
r4 = random.choice(when)
print(r4)

excuse = who[r1] + " " + r2 + " " + what[r3] + " " + r4 #forma de concatenar #1
print(excuse)

excuse = f'{who[r1]} {r2} {what[r3]} {r4}' #imprimir de forma concatenada #2 usando format f'{var}'
print(excuse)
