n = int(input())


def solution(n):
    ans = []
    nums = [4, 5, 6]

    def possible(arr):
        # print(f'{arr}')
        len_arr = len(arr)
        for length in range(1, n + 1):
            start1, end1 = len_arr - length, len_arr - 1
            start2, end2 = start1 - length, start1 - 1
            
            if start1 < 0 or start2 < 0:
                break
            # print(f'{length}: {start1},{end1} / {start2},{end2}')

            if arr[start2 : end2 + 1] == arr[start1 : end1 + 1]:
                return False
        return True

    arr = []
    def choose(curr_idx):
        nonlocal ans

        # 사전순으로 가장 첫번째 수열을 리턴해야 하니까
        # ans가 한번이라도 채워진 적 있다면 스루
        # (import sys 안써보고 싶어서 이렇게 한거임)
        if len(ans) > 0:
            return

        if curr_idx == n:
            ans = arr[:]
            return
        for num in nums:
            arr.append(num)
            # 추가하자마자 수열의 가능성을 따져
            # 더이상 나아갈지말지 결정하는 것임
            if possible(arr[:]):
                choose(curr_idx + 1)
            # 가능성이 없다면 아묻따 바로 팽~!
            arr.pop()

    # 중복수열을 만들되
    # 추가하자마자, 수열의 가능성을 따져보고
    # 더이상 탐색할지말지 결정한다
    choose(0)

    return ans


ans = solution(n)
for el in ans:
    print(el, end="")