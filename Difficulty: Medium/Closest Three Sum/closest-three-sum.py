#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest (self, arr, target):
        minDiff = 1e8
        arr.sort()
        for i in range(0, len(arr)):
            l = i + 1
            r = len(arr) - 1
            while l < r:
                sum1 = arr[i] + arr[l] + arr[r]
                diff = abs(sum1 - target)
                if diff < minDiff:
                    minDiff = diff
                    ans = sum1
                elif diff == minDiff:
                    ans = max(ans,sum1)
                if sum1 > target:
                    r -= 1
                else:
                    l += 1
        return ans
    # Your Code Here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))

# } Driver Code Ends