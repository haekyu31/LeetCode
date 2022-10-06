class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(sum, index, path):
            # dfs의 종료조건 설정
            # target보다 숫자가 커질경우 종료
            if sum<0:
                return
            # target이 된다면 result 에 결과를 저장
            if sum ==0:
                result.append(path)
                return
            # 재귀함수 호출 자기 자신부터 모든 원소들을 포함하도록 
            for i in range(index,len(candidates)):
                # index 위치 값을 제외하고 path에는 값을 저장한상태로 재귀함수
                dfs(sum-candidates[i], i,  path + [candidates[i]])
        dfs(target, 0, [])
        return result