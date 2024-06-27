n = int(input())


def solution(n):
    ans = []
    arr = []

    def in_range(start_idx, length):
        nonlocal n
        if start_idx + length <= n and \
            start_idx + 2 * length <= n:
            return True
        return False


    def possible(arr):
        n = len(arr)
        if n == 1:
            return True
        # print(arr)
        for start_idx in range(n):
            for length in range(1, n + 1):
                if not in_range(start_idx, length):
                    break
                a = arr[start_idx : start_idx + length]
                b = arr[start_idx + length : start_idx + 2 * length]
                if a == b:
                    return False
        return True


    def choose(curr_idx):
        nonlocal n, ans

        if len(ans) > 0:
            return

        if curr_idx == n:
            ans = arr[:]
            return
        
        for i in range(4, 6 + 1):
            arr.append(i)
            if possible(arr[:]):
                choose(curr_idx + 1)
            arr.pop()


    # 1. n길이 중복순열 만들기
    choose(0)
    return ans


res = solution(n)
for el in res:
    print(el, end="")