L = [1, 42, 36, 78, 95, 6.0, "abc", 'abd291']
print(L)
#to check the length
print(len(L))

#To print in  perticular elemint
print(L[5])

#To list elements between index 3 to 6 means it will prints 3 (to n-1 = 6-1=5)  to 5 th element
print(L[3:6])

#To print first to 4 th means 4-1 th index
print(L[:4])

#To print from index 2
print(L[2:])

#To Concadinate
J = L + ['A']
print(L + ['Keerthi']) # Add to the list
print(L) # Keerthi Added to the list but not assigned yet
print(J)

#Multiplication it prints twice
print(J * 2)

#Append the list
A = [1,2,3,4]
print(A)
A.append('Love!')
print(A)