list_of_arrays=[
[277,349,127,236,411,0],
[123,117,206,21,14,244,244,225,40,130,214,226,210,222,185,0],
[106,84,449,478,402,476,72,166,0],
[803,421,358,867,911,824,666,992,879,617,940,0],
[3483,4629,5231,1987,3517,2958,4703,5557,4648,6040,4542,4096,4266,0],
[3459,372,112,2573,2055,1541,1943,1600,740,510,0],
[186,71,198,124,180,86,32,242,0],
[1062,908,104,523,2043,1128,1590,983,392,1271,1169,447,509,0],
[2961,1895,3174,3470,3364,0],
[401,2390,233,3275,3765,735,3046,2802,2714,1072,521,2922,2118,0],
[150,310,234,468,90,345,0],
[138,453,364,22,375,272,0]
]

results=[]

def array_avg(x):
	tmp=float(0)
	for i in x:
		tmp+=i	
	avg=tmp / (len(x)-1)
	return round(avg)

def main():
	x=0
	while x <= (len(list_of_arrays)-1):
		results.append(array_avg(list_of_arrays[x]))
		x+=1
	print results


main()
	
'''
#Author's Note:
a = [int(x) for x in input().split()]
avg = sum(a) / (len(a) - 1)
'''