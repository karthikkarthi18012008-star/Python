import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,23])

print("\nArray a :",a)
print("\nArray b:",b)
print("="*30)

# Arithmetic operations
print("Addition:",a+b)
print("\nSubtraction:",b-a)
print("\nMultiplication:",a*b)
print("\nDivision",a/b)
print("="*30)

# Statistical operations
print("\nMinimum value:",np.min(a))
print("\nMaximum value:",np.max(a))
print("\nSum of a:",np.sum(a))
print("\nMean of a:",np.mean(a))
print("\nStandard Deviation of a:",np.std(a))
print("="*30)

#slicing
print("\nFirst three elements of a:",a[:3])
print("\nLast two elements of a:",a[-2:])
print("\nElements from greater then 2:",a[a>2])
print("="*30)

#Reshaping
c = np.arange(1,10)
print("Original array:",c)
print("Reshaped array (3x3):\n",c.reshape(3,3))
print("="*30)