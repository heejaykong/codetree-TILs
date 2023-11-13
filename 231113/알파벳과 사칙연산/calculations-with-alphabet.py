# 20:45
string = input()


def solution(string):
    string = list(string)
    ans = -(2 ** 31)

    def calc(arr):
        mapper = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
        }
        for (idx, key) in enumerate(mapper):
            mapper[key] = arr[idx]
        
        curr_num = mapper[string[0]]
        curr_op = ''
        i = 1
        while i < len(string):
            if string[i] == '+':
                curr_op = '+'
                i += 1
                continue
            if string[i] == '-':
                curr_op = '-'
                i += 1
                continue
            if string[i] == '*':
                curr_op = '*'
                i += 1
                continue
            if curr_op == '+':
                curr_num = curr_num + mapper[string[i]]
            if curr_op == '-':
                curr_num = curr_num - mapper[string[i]]
            if curr_op == '*':
                curr_num = curr_num * mapper[string[i]]
            i += 1

        return curr_num

    LEN = 6
    arr = []
    nums = [i for i in range(1, 4+1)]
    len_nums = len(nums)
    def choose(curr_idx):
        nonlocal ans

        if curr_idx == LEN:
            ans = max(ans, calc(arr[:]))
            return
        for num in nums:
            arr.append(num)
            choose(curr_idx + 1)
            arr.pop()

    # a ~ f까지 1~4 사이 숫자를 부여하는 중복순열 만들기(=1~4로 구성하는 6자리 중복순열 만들기)
    # 다 만든 결과로 수식 계산하고, 최대값과 겨루기
    choose(0)

    return ans


print(solution(string))