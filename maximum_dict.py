# Consider a dictionary my_points with single letter keys, each followed by a 2-element tuple representing
# the coordinates of a point in an x-y coordinate plane.
#       my_points={'a':(4,3),'b':(1,2),'c':(5,1)}
# Write a program to print the maximum value from within all the values tuples at same index.

my_points={'a':(4,3),'b':(1,2),'c':(5,1)}
highest=[0,0]
init=0
for a in range(3):
    init=0
    for b in my_points.keys():
        val=my_points[b][a]
        
        if init==0:
            highest[a]=val
        init+=1
        
        if val > highest[a]:
            highest[a]=val
print("Maximum Value at index(my_points,", a, ")=", highest[a])
