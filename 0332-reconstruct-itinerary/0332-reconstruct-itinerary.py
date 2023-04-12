class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route, stack = [], ['JFK']
        
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
            
        return route[::-1]
#         # 그래프를 뒤집어서 구성
#         for a, b in sorted(tickets, reverse = True):
#             graph[a].append(b)
#         route = []
        
#         def dfs(a):
#             while graph[a]:
#                 dfs(graph[a].pop())
#             route.append(a)
        
#         dfs('JFK')
#         return route[::-1]
#         # 그래프 순서대로 구성
#         for a, b in sorted(tickets):
#             graph[a].append(b)

#         route = []
        
#         def dfs(a):
#             # 첫 번째 값을 읽어 어휘 순 방문
#             while graph[a]:
#                 dfs(graph[a].pop(0))
#             route.append(a)
        
#         dfs('JFK')
#         # 다시 뒤집어 어휘 순 결과로 
#         return route[::-1]
            