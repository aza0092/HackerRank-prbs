def kangaroo(x1, v1, x2, v2):
    if((x1>x2 and v1>v2) or (x1<x2 and v1<v2) or (v1-v2)==0):
        return "NO"
    if((x1 - x2) % (v2 - v1)) == 0:
        return "YES"
    else:
        return "NO"

'''
EXPLANATION:
solving the equation mentioned above, x1+ y*v1=x2+ y*v2 , we get (x1-x2)/(v2-v1)= y.
Since y is number of jumps so it has to be an integer,
thus (x2-x1)%(v2-v1)==0


x1+y*v1 = x2+y*v2

=>(x1-x2)+y(v1-v2) = 0

=>(x1-x2) = -y(v1-v2) Removing the '-ve' sign from RHS =>(x2-x1) = y(v1-v2)

=>(x2-x1)/(v1-v2) = y ----(1)

If you multiply -1 to both the numerator and denominator, then

=>(x1-x2)/(v2-v1) = y ----(2)

Thus equation (1) and (2) are the same.

'''

		
'''
input:
0 3 4 2
ANSWER: YES
input: 
0 2 5 3
ANSWER: NO

		
		

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
