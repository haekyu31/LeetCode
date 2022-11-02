class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))    # 이동결로가 존재한다면 어휘순으로 첫번째 이동경로를 가져온다
            route.append(a)             # 더이상 이동할 곳이 없을 경우 역순으로 담기기 시작한다. 
        dfs('JFK')
        return route[::-1]
    # 많이 어려운 문제