# 복잡도는 O(2^6 * n)
question_statement = input()


def solution(statement):
    MIN = -(2**31)
    ans = MIN
    arr = []
    idx_mapper = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5
    }

    def calc(arr):
        acc = 0  # 초기값
        op = '+'  # 초기값

        for elem in statement:
            if elem in ['+', '-', '*']:
                op = elem
            else:
                number = arr[idx_mapper[elem]] # 파싱
                if op == '+':
                    acc += number
                if op == '-':
                    acc -= number
                if op == '*':
                    acc *= number
        return acc


    def choose(curr_idx):
        nonlocal ans

        if curr_idx == 6:
            # 2. 중복순열 순서대로 a부터 f까지 매핑
            # 3. 매핑대로 식 계산한 값으로 max값 겨루기
            ans = max(ans, calc(arr))
            return

        for i in range(1, 4 + 1):
            arr.append(i)
            choose(curr_idx + 1)
            arr.pop()

    # 1. 6자리 중복순열만들기(원소는 1~4)
    choose(0)

    return ans


print(solution(question_statement))