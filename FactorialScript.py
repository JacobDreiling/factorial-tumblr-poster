#Huge thanks to Peter Luschny for this incredible factorial algorithm:
#http://www.luschny.de/math/factorial/SwingFactorialSagePython.html

def fac(n):
	smallOddSwing = [
		1,1,1,3,3,15,5,35,35, 315, 63, 693, 231, 3003, 429, 6435, 6435,
		109395,12155,230945,46189,969969,88179,2028117,676039,16900975,
		1300075,35102025,5014575,145422675,9694845,300540195,300540195 ]
	smallOddFactorial = [
		1,1,1,3,3,15,45,315, 315, 2835, 14175, 155925, 467775, 6081075,
		42567525, 638512875, 638512875 ]
	def product(m, len):
		if len == 1: return m
		if len == 2: return m * (m - 2)
		hlen = len >> 1
		return product(m - hlen * 2, len - hlen) * product(m, hlen)
	def oddFactorial(n):
		sqrOddFact = 1
		if n < 17:
			oddFact = smallOddFactorial[n]
			sqrOddFact = smallOddFactorial[n//2]
		else:
			(sqrOddFact, oldOddFact) = oddFactorial(n//2)
			if n < 33: 
				oddSwing = smallOddSwing[n] 
			else:
				len = (n - 1) // 4
				if (n % 4) != 2: len += 1
				high = n - ((n + 1) & 1)
				oddSwing = product(high, len) // oldOddFact
			oddFact = (sqrOddFact*sqrOddFact) * oddSwing
		return (oddFact, sqrOddFact)
	if n == 0: return 1
	if n <  0: return 0
	N, bits = n, n
	while N != 0:
		bits -= N & 1
		N >>= 1
	F = oddFactorial(n)
	twos= 1
	for i in range(bits): twos*=2
	return F[0]*twos


def nameScript2(num):
	unIllions= ['','mi','bi','tri','quadri','quinti','sexti','septi','octi','noni']
	monIllions= ['','un','duo','tre','quattuor','quinqua','se','septe','octo','nove']
	decIllions= ['','deci','viginti','triginta','quadraginta','quinquaginta','sexaginta','septuaginta','octoginta','nonaginta']
	centIllions= ['','centi','ducenti','trecenti','quadrigenti','quingenti','sescenti','septingenti','octingenti','nongenti']
	tens= ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	teens= ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	ones= ['','one','two','three','four','five','six','seven','eight','nine']
	L= len(num)
	name= ''
	for cluster in range((L-1)//3-1,-1,-1):
#First part of the name: blah hundred blobitty-blah
		notFlat= True
		if cluster==(L-1)//3-1 and L%3: #first-clusters w/ 2 digits and 1 digit, respectively
			d1,d2= int(num[0]),int(num[1])
			if L%3==2:
				if d1==1: name+=' '+teens[d2]
				else: name+=' '+tens[d1]+(d2>0)*('-'+ones[d2])
			else: name+=' '+ones[d1]
		else: #all other clusters (including three-digit first-clusters)
			hun,ten,one= int(num[L-3*cluster-6]),int(num[L-3*cluster-5]),int(num[L-3*cluster-4])
			notFlat= hun+ten+one>0
			if hun>0: name+=' %s hundred'%ones[hun]
			if ten==1: name+=' '+teens[one]
			elif ten>1: name+=' '+tens[ten]+(one>0)*('-'+ones[one])
			elif one>0: name+=' '+ones[one]
#Second part of the name: the gross Roman nomenclature
		if notFlat:
			if cluster==0: name+=' thousand,'
			else:
				def exceptions(a,b,c):
					if a in [3,6] and (b in [2,3,4,5] or (b==0 and c in [3,4,5])): return 's'
					if a==6 and (b==8 or (b==0 and c in [1,8])): return 'x'
					if a in [7,9] and (b in [1,3,4,5,6,7] or (b==0 and c in range(1,8))): return 'n'
					if a in [7,9] and (b in [2,8] or (b==0 and c==8)): return 'm'
					return ''
				temp= cluster
				illion= ''
				a,b,c= temp%10,(temp//10)%10,(temp//100)%10 #MONillion digits of the cluster number
				if temp<10: illion+=unIllions[a]
				else: illion+=monIllions[a]
				illion+=exceptions(a,b,c)+decIllions[b]+centIllions[c]
				temp//=1000
				d,e,f= temp%10,(temp//10)%10,(temp//100)%10 #MILLillion digits of the cluster number
				if temp<10: illion+=unIllions[d]
				else: illion+=monIllions[d]
				illion+=exceptions(d,e,f)+decIllions[e]+centIllions[f]
				name+=' %s%sillion,'%(illion[:-1],(temp>0)*'illin')
#Final part of the name: the last three digits
	hun,ten,one= int(num[-3]),int(num[-2]),int(num[-1])
	if hun>0: name+=' %s hundred'%ones[hun]
	if ten==1: name+=' '+teens[one]
	elif ten>1: name+=' '+tens[ten]+(one>0)*('-'+ones[one])
	elif one>0: name+=' '+ones[one]
	if hun+ten+one>0: name+=' '
#And it's that EZ boys and girls common now get it together
	return name[1:-1].capitalize()


interestings= [0,6,10,24,25,38,42,69,70,92,100,120,171,200,720,1000,1144,2080,2081,5040,6969,10000,40320,100000,362880,564212]
coolFax= ['','','','','','','','','','','','','','','','','The smallest value of <i>n</i> such that <i>n</i>! > 10^3003, which is called a \"Millinillion\".','The largest value of <i>n</i> such that <i>n</i>! can be named using the conventional SI short-scale large number naming system (which gives names up to but not including 10^6003).','The smallest value of <i>n</i> such that <i>n</i>! > 10^6003 and hence must be named using an extended SI short-scale system (I will denote the proceeding thousandth terms as "billinillion, trillinillion, quadrillinillion," etc.)','The fifth non-trivial value of <i>n</i> such that <i>n</i>! is itself a factorial (namely, 7!).','Insert double innuendo here','The first five-digit value of <i>n</i>.','The sixth non-trivial value of <i>n</i> such that <i>n</i>! is itself a factorial (namely, 8!).','The first six-digit value of <i>n</i>.','The seventh non-trivial value of <i>n</i> such that <i>n</i>! is itself a factorial (namely, 9!).','SPECIAL']


def facScript(x):
	numStr= str(fac(x))
	digits= len(numStr)
	for i in range(digits-3,0,-3): numStr= numStr[:i]+' '+numStr[i:]
	body= '{}! = {}<br>\n<b>Name: </b>{}<br>\n<b>Digits: </b>{}'.format(x,numStr,nameScript2(numStr.replace(' ','')),digits)
	if interestings.count(x)>0: body+='<br>\n— '+coolFax[interestings.index(x)]
	return body[:1001]+'[[MORE]]'+body[1001:]
print(facScript(100))

#naïve factorial:
#100,000! takes about   94 seconds or  1.57 minutes
#200,000! takes about  424 seconds or  7.07 minutes
#300,000! takes about 1040 seconds or 17.77 minutes
#400,000! takes about 1905 seconds or 31.75 minutes

#factorial swing:
#100,000! takes about  53 seconds or  0.9 minutes
#200,000! takes about 142 seconds or 2.36 minutes      ~3 times faster than naïve
#300,000! takes about 328 seconds or 5.47 minutes
#400,000! takes about 599 seconds or 9.97 minutes

#factorial swing on Mac:
#100,000! takes about  16 seconds or 0.09 minutes
#200,000! takes about  65 seconds or 1.08 minutes      ~6 times faster than naïve
#300,000! takes about 154 seconds or 2.57 minutes
#400,000! takes about 287 seconds or 4.79 minutes
