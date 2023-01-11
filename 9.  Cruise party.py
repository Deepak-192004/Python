def max_guests(T,E,L):
    if not isinstance(T,int) or T <=0:
        return 0
    guests = 0
    max_guests = 1
    for i in range(T):
        guests += E[i]
        guests -= L[i]
        max_guests = max(max_guests, guests)
    return max_guests
print(max_guests(5, [7,0,5,1,3],[1,2,1,3,4]))
        
    
