def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return (fib(num-1) + fib(num-2))

def fib2(num):
    if num == 0:
        return [0]
    else:
        seq = [0,1]
        while(len(seq)<num):
            seq.append(seq[len(seq)-1]+seq[len(seq)-2])
        return seq


a = int(input())

print( f"Hallo ich bin {a}" )

if (a % 2 == 0):
    print( "gerade" )
else:
    print( "ungerade" )

print( )

for icount, i in enumerate(range(a+1)):
    for jcount, j in enumerate(range(a+1)):
        print( f"{(icount * jcount):4d}" , end=" " )
    print()

print( )

#fib(a)
print(fib2( a ))

