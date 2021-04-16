#Implement the function isStringPermutation() that takes two Strings as parameters and returns a Boolean 
# denoting whether the first string is a permutation of the second string.
#Examples:
#isStringPermutation(s1: “asdf”, s2: “fsda”) == true
#isStringPermutation(s1: “asdf”, s2: “fsa”) == false
#isStringPermutation(s1: “asdf”, s2: “fsax”) == false

#Implement the function pairsThatEqualSum() that takes an array of integers and a target integer and
#  returns an array of pairs (i.e., an array of tuples) where each pair contains two numbers from the input array
#  and the sum of each pair equals the target integer. (Order of the output does not matter).
#Examples:
#pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 5) == [(1, 4), (2, 3)]
#pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 1) == []
#pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 7) == [(2, 5), (3, 4)]



def main():
    #Tests for isStringPermutation
    s1 = "asdf"
    s2 = "asdf"
    print("String Permutation: ",isStringPermutation(s1, s2))

    s1 = "asdf"
    s2 = "fsa"
    print("String Permutation: ",isStringPermutation(s1, s2))

    s1 = "asdf"
    s2 = "fsax"
    print("String Permutation: ",isStringPermutation(s1, s2))

    print("\n")

    #Tests for pairsThatEqualSum
    arr = [1,2,3,4,5]
    target = 5
    print("Pairs that equal sum: ", pairsThatEqualSum(arr, target))

    arr = [1,2,3,4,5]
    target = 1
    print("Pairs that equal sum: ", pairsThatEqualSum(arr, target))

    arr = [1,2,3,4,5]
    target = 7
    print("Pairs that equal sum: ", pairsThatEqualSum(arr, target))



#Time Complexity: O(n)
def isStringPermutation(s1,s2):
    if len(s1) != len(s2): 
        return False
    s1Map = {}
    for i in s1:
        if i in s1Map:
            s1Map[i] += 1
        else:
            s1Map[i] = 1

    for i in s2:
        if i in s1Map and s1Map[i] > 0:
            s1Map[i] -= 1
        elif i in s1Map and s1Map[i] == 0:
            return False
        else:
            return False
    return True

def pairsThatEqualSum(arr, targetSum):
    #Create a list to store the pairs that equal sum and return at the end
    pairList = []
    #Create a map that will store the pairs
    compMap = {}
    #Iterate through the array
    for i in range(len(arr)):
        if targetSum - arr[i] > 0:
            comp = targetSum - arr[i]
        elif arr[i] - targetSum > 0:
            comp = arr[i] - targetSum
        else:
            return pairList
            
        if comp in compMap:
            pairList.append([arr[i],comp])
        else:
            compMap[arr[i]]=comp
    
    return pairList

main()
