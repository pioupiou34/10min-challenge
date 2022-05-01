debug = 0
a = 1
b = 1
c = 1

SS = []
SSS = []

print('Quel nombre voulez vous décomposé en somme de 3 chiffre ?')
T = int(input())

while a <= 6 :
	while b <= 6 :
		while c <= 6 :
			S = a+b+c
			if S == T:
				if debug == 1:
					print(a,b,c)
				
				SS.append([a,b,c])
				SSS.append(a*b*c)
				

			c +=1
		b += 1
		c = 1
	a += 1 
	b = 1

if debug == 1:
	print(SS)
	print(SSS)





def indlist(ll,p):
	indices = [i for i, x in enumerate(ll) if x == p]
	if debug == 1:
		print(indices)
	return indices 

def dett(ll,li):
	ll = [i for j, i in enumerate(ll) if j not in li]
	return ll

def index_in_list(a_list, index):
    return(index < len(a_list))

pe = 0
fin = []
while pe < len(SSS):

	cd = indlist(SSS,SSS[0])

	fin.append(SS[0])
	SSS = dett(SSS,cd)
	SS = dett(SS,cd)
	if debug == 1:
		print('*',SS)
		print("**",SSS)
	pe += 1

if index_in_list(SS,0) == True:
	fin.append(SS[0]) 



io = 0
print("\n")
print("Il y a",len(fin),"de possibliltés :")
print("\n")
while io < len(fin):
	ae = fin[io]
	print(ae[0],"+",ae[1],'+',ae[2], "=",T)
	io += 1
