class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프가 순환인지 판별하는 문제
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        traced = set()              # 순환구조인지 확인
        visited = set()             # 이미 방문했던 노드인지 
        
        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            
            traced.add(i)
            
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            
            return True
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
# Time Limit 에 걸린다. 
#         # [a,b] a끝난 다음 b를 끝낼 수 있다
#         graph = collections.defaultdict(list)
#         for x, y in prerequisites:
#             graph[x].append(y)          # 'x' :['y1', 'y2']  의 형태로 만들기
            
#         traced = set()                  # 이미 방문했던 노드를 traced에 저장하기 
        
#         def dfs(i):
#             # 순환구조이면 False
#             if i in traced:
#                 return False
            
#             traced.add(i)               # set 더할때는 add()
#             for y in graph[i]:          # i : "y1", "y2"..
#                 if not dfs(y):
#                     return False        # 순환구조 일경우 dfs(y) == False
#             # 탐색 종료후 순환 노드 삭제
#             traced.remove(i)
            
#             return True
        
#         for x in list(graph):
#             if not dfs(x):
#                 return False
            
#         return True
            
        