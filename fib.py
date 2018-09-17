def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def M(n):
    if n == 0: return 1
    else: return M(n-1)*n

for i in range(5):
    print F(i)

print "____________"
    
for i in range(10):
    print M(i)
