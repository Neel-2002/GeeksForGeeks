

import heapq

class Solution:
    def getMedian(self, nums):
        max_heap = []  # To store the smaller half (using negative values for max-heap)
        min_heap = []  # To store the larger half
        medians = []

        for num in nums:
            # Add the number to the appropriate heap
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

            # Balance the heaps
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # Calculate the median
            if len(max_heap) == len(min_heap):
                median = (-max_heap[0] + min_heap[0]) / 2
            else:
                median = -max_heap[0]
            
            medians.append(median)
        
        return medians


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends