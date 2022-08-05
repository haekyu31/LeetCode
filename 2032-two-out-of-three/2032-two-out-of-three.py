class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        # 중복제거
        # nums1 nums2 nums3 하나의 리스트로 만든다
        # 하나의 list 에서 2개 이상의 숫자만 list형태로 return한다.
        
        nums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        c = collections.Counter(nums)
        return [i[0] for i in c.items() if i[1] >= 2]
        
        # Step1: num1, num2, num3에서 중복을 제거한다.
        # python list delete duplicate
        # Step2: num1+num2+num3 를 합쳐서 하나의 list로 만든다.
        # python concatenate lists to one list
        # Step3: 하나의 list가 된 데이터에서 count를 하여,
        # 2개 이상인 숫자들만 list 형태로 return 한다.
        # python counter in list Collections.Counter
        