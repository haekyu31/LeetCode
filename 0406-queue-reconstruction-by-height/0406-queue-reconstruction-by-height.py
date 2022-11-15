class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            # 역순으로 집어넣어 최대 힙 구현
            heapq.heappush(heap, (-person[0], person[1]))
        result = []
        # 키 역순 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result