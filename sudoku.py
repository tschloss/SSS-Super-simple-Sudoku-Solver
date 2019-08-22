inp = '913500007007300915064197003091073056345926871706051309479685132538219764162734598'

 # '627984315013057490000013070900560040000400050001300620170830060300745180000106030' # '627984315013057490000013070900560040000400050001300620170832060300745180000106030'
# '000000060006873005007005900000008107000007006000600080503400670090052800800000049'
#96230040508542970007456002053198467264005003082000054049600015 0218045390753190204'
#'015023607-000000900-600000250-064102538-132800479-508300162-800209000-009000026-000730890'
# '300650700050010306086000000904865230260374095035100460540200070600581943190740002'
# '586070000004901600009600000007060000962010305005090006091046008003580060658120470'
#'586070000004901600009600000007065000962010305005090006091046008003580060658120470'
#900005070015006943030000050500003720004607000079004300040102000000070030091008000'
# '903560004000100036680300000038219607160734080000685301345926718726851493800473562'
# 128030745000024000000000000000000000000000000000000000000000000000000000000000000'
#'000068030190000000803100200400051060700020004000070800010005007004000000050030100'
#'031060400000002000000000003000400000062000009004900001000004500097080030080010764'
#'500000900042901607007008204080003470000000160200040500920010000400000091800300700'


def calc_possibilities (l,r,f):
	if f[l][r] != 0:
		return {f[l][r]}
	possibles={1,2,3,4,5,6,7,8,9}
	for v in field[l]:
		possibles.discard(v)
	for i in range(9):
		possibles.discard(field[i][r])
	for ll in range(3):
		for rr in range(3):
			possibles.discard(field[3*(l//3)+ll][3*(r//3)+rr])
	return possibles

def test_exclusive (c,l,r,f):
	# c is one possible value for l/r, is l/r the only position in one of the 3 peer groups? => c in none of the other possibilities
	
	# exclusive in horizontal group?
	exclusive = True
	for i in range(9):
		if (i != r) and (f[l][i] == 0):
			if c in calc_possibilities(l,i,f):
				exclusive = False
				break
	if exclusive: 
		#print ('h')
		return(True)
	
	# exclusive in vertical group?
	exclusive = True
	for i in range(9):
		if (i != l) and (f[i][r] == 0):
			if c in calc_possibilities(i,r,f):
				exclusive = False
				break
	if exclusive: 
		#print ('v')
		return(True)
				
	# exclusive in square group?
	exclusive = True
	x=r//3
	y=l//3
	for i in range(3):
		for j in range(3):
			if ((y*3+i != l) or (x*3+j != r)) and (f[y*3+i][x*3+j] == 0):
				#print ('  check q: ',c, y*3+i,x*3+j )
				if c in calc_possibilities(y*3+i,x*3+j,f):
					exclusive = False
					break  # should leave both loops!
	if exclusive: 
		#print ('q')
		return(True)
	
	return (False)
	
def print_field(field):
	j=0
	for l in field:
		s=''
		i=0
		for r in l:
			s = s + ('.' if (r==0) else str(r))
			i = i+1
			if i in {3,6}: s = s + '|'
		print (s)
		j=j+1
		if j in {3,6}: print('---+---+---')
		

field = []
i=0
line = []
for c in inp:
	if (c >= '0' and c <= '9'):
		line.append(ord(c) - 48)
		if (i % 9) == 8:
			field.append(line)
			line = []
		i = i+1

print_field(field)

changed=True
while changed:
	changed = False
	for l in range(9):
		for r in range(9):
			if field[l][r]==0:
				possibles = calc_possibilities(l,r,field)
				# print(l,r,possibles)
				if len(possibles) == 1:
					field[l][r] = possibles.pop()
					changed = True
					print (l,r,'1->',field[l][r])
				else:
					for c in possibles:
						if test_exclusive(c,l,r,field):
							field[l][r] = c
							changed = True
							print (l,r,'x->',field[l][r])
							break
	print ('------')		
			
print_field(field)
