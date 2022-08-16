from collections import defaultdict
from typing import (
    List,
)

class Solution:
    """
    @param tickets: the list of the airline tickets
    @return: the reconstructed itinerary
    """

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import heapq
        from collections import defaultdict

        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]

    def find_itinerary_slow(self, tickets: List[List[str]]) -> List[str]:
        # Write your code here

        from collections import defaultdict

        tckt = defaultdict(list)

        for t in tickets:
            tckt[t[0]].append(t[1])

        for t in tckt.keys():
            #print(t)
            if len(tckt[t]) > 1:
                #print(tckt[t])
                tckt[t].sort()

        #print(tckt)
        itinerary = []

        def dfs(start, temp_itinerary, temp_ticket):
            nonlocal itinerary

            temp_itinerary.append(start)

            if start not in temp_ticket or not len(temp_ticket[start]):
                if len(temp_itinerary) > len(itinerary):
                    itinerary = list(temp_itinerary)
                    temp_itinerary.pop()
                    return

            for i in range(len(temp_ticket[start])):

                temp_dest = temp_ticket[start].pop(i)
                dfs(temp_dest, temp_itinerary, temp_ticket)
                temp_ticket[start].insert(i, temp_dest)


            temp_itinerary.pop()

        dfs("JFK", [], tckt)

        return itinerary


    def find_itinerary_non_dfs(self, tickets: List[List[str]]) -> List[str]:
        # Write your code here

        from collections import defaultdict

        tckt = defaultdict(list)

        for t in tickets:
            tckt[t[0]].append(t[1])

        for t in tckt.keys():
            #print(t)
            if len(tckt[t]) > 1:
                #print(tckt[t])
                tckt[t].sort()

        print(tckt)
        itinerary = []
        curr = "JFK"

        while curr != "":

            itinerary.append(curr)

            #print(tckt)

            if len(tckt[curr]) > 1:
                found = False
                prev = curr
                for i in range(len(tckt[curr])):
                    print(tckt[curr],tckt[curr][i])
                    if tckt[curr][i] in tckt and len(tckt[tckt[curr][i]]):
                        curr = tckt[curr].pop(i)
                        found = True
                        break

                #tckt[prev].sort()
                if not found:
                    curr = ""
            elif len(tckt[curr]) == 1:
                curr = tckt[curr].pop()
            else:
                curr = ""

        return itinerary

