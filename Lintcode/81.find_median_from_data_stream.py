from heapq import heappush, heappop

class Solution:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    """
    @param val: a num from the data stream.
    @return: nothing
    """
    def add(self, val: int):
        # write your code here

        if self.min_heap and val >= self.min_heap[0]:
            heappush(self.min_heap, val)
        else:
            heappush(self.max_heap, val*-1)

        # Re-balance min and max heap
        # make sure two heap length are the same or max heap is one element longer
        while not ((len(self.max_heap) == len(self.min_heap)) or (len(self.max_heap) == len(self.min_heap) + 1)):
            if len(self.max_heap) > len(self.min_heap) + 1:
                temp = heappop(self.max_heap)*-1
                heappush(self.min_heap, temp)
            elif len(self.min_heap) > len(self.max_heap):
                temp = heappop(self.min_heap)*-1
                heappush(self.max_heap, temp)
            else:
                break

        #print(self.min_heap)

    """
    @return: return the median of the all numbers
    """
    def getMedian(self) -> int:
        # write your code here
        #print(self.max_heap, self.min_heap)
        return self.max_heap[0]*-1
