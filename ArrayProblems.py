
# Homework 3
def largest(array, count):
    # O(1)
    largest_values = []
    # O(k)
    for j in range(count):
        # O(1)
        i = 0
        # O(1)
        largestNum = 0
        # O(n)
        while i != len(array) - 1:
        # O(1), O(k)
            if largestNum < array[i] and array[i] not in largest_values:
                # O(1)
                largestNum = array[i]
        # O(1)
        i += 1
        # O(1)
        largest_values.append(largestNum)
    print(largest_values)

a=[5, 1, 3, 6, 8, 2, 4, 7] 
k=3
largest(a, k)
# O(k) * O(n * k) = O(k^2 * n)


# Homework 4
def distance_to_t(t, x):
    return abs(t - x)

def closestToT(arrayA, arrayB, T):
    # O(1)
    val_a = 0
    # O(1)
    val_b = 0
    # O(1)
    smallestNum = 10000
    # O(A)
    for i in range(len(arrayA)):
        # O(B)
        for j in range(len(arrayB)):
            # O(1)
            numApart = distance_to_t(T, (arrayA[i] + arrayB[j]))
            # O(2)
            if smallestNum > numApart or smallestNum == numApart:
                # O(1)
                smallestNum = numApart
                # O(1)
                val_a = arrayA[i]
                # O(1)
                val_b = arrayB[j]
    print([val_a, val_b])

a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=20
closestToT(a,b,t)
# O(A * B)
