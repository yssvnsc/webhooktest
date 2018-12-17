##############

print("HI")

##############################################################################
s = "Venky"
print('my name is : %s'%(s))

##############################################################################
x = float(1.2345678)
y = float(100.1)
print('Float number with 2 decimals: %1.2f'%(x))
print('Float number with 3 decimals:%1.3f'%(x))
#Removesd the decimals after 3 digits
print('Float number with 4 decimals:%1.4f'%(y))
#Added with 0 'sr
print('Float number with 4 decimals:%10.4f'%(x))
# prints 10 digits in that 6 are number spaces and 4 are decimals.
print('Float number with 4 decimals:%15.1f'%(y))
print('Float number with 4 decimals:%s'%(x))
# We have passed %s method
print('Float number with 4 decimals:%r'%(y))
# We have passed %r method

##############################################################################
print('First no: %s, Second no %s, third no :%s' %('1', '2', '3.0'))
print('Firsr no: %s, Second no %s' %(2,2))
#To print the valued between the statements
print('First no:{a} Second no:{a} Number3{b}'.format(a = 1,b = 3))
print('insert first value{a} insert second value {y}'.format(a = 'one', y = 'two'))
print('first value:{a}, second value:{y}, 3rd value as:{a}'.format(a = 'one', y = 'two'))
print('{a}'.format(a = 'xyz'))
print()
#To print the same value mltiple times we use this method {}

###############################################################################
