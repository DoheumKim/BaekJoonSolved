import sys

sys.setrecursionlimit(5000)

line = sys.stdin.readline().strip()
if not line:
    exit()

# 식 분리
a_raw, rest = line.split('+')
b_raw, c_raw = rest.split('=')

la, lb, lc = len(a_raw), len(b_raw), len(c_raw)
max_len = max(la, lb, lc)

# 자릿수를 맞추기 위해 zfill 사용 (오른쪽 정렬)
a_str = a_raw.zfill(max_len)
b_str = b_raw.zfill(max_len)
c_str = c_raw.zfill(max_len)

memo = {}

def is_valid(val, idx, origin_str, original_len, max_len):
    char = origin_str[idx]
    # 실제 숫자가 시작되기 전 패딩 영역은 무조건 0이어야 함
    if idx < max_len - original_len:
        return val == 0
    # ?가 아닌 숫자가 이미 있으면 일치해야 함
    if char != '?' and int(char) != val:
        return False
    # 첫 자리가 0이면 안 됨 (원래 길이가 1이면 허용)
    real_idx = idx - (max_len - original_len)
    if real_idx == 0 and original_len > 1 and val == 0:
        return False
    return True

def solve(idx, carry):
    if idx == -1:
        return ("", "", "") if carry == 0 else None
    
    state = (idx, carry)
    if state in memo:
        return memo[state]
    
    best = None
    
    for a in range(10):
        if not is_valid(a, idx, a_str, la, max_len): continue
        for b in range(10):
            if not is_valid(b, idx, b_str, lb, max_len): continue
            
            total = a + b + carry
            c = total % 10
            next_carry = total // 10
            
            if not is_valid(c, idx, c_str, lc, max_len): continue
            
            res = solve(idx - 1, next_carry)
            if res is not None:
                # 결과 조립: (C_str, A_str, B_str)
                # 앞자리(res) 뒤에 현재 숫자(str(c))를 붙임
                cur_a = res[1] + str(a)
                cur_b = res[2] + str(b)
                cur_c = res[0] + str(c)
                
                # C 최대 -> A 최대 순으로 비교
                if best is None or (cur_c, cur_a) > (best[0], best[1]):
                    best = (cur_c, cur_a, cur_b)
    
    memo[state] = best
    return best

# 올바른 시작 인덱스와 carry로 호출
final_result = solve(max_len - 1, 0)


if final_result is None:
    print("-1")
else:
    # 패딩 제거 후 출력
    res_c, res_a, res_b = final_result
    print(f"{res_a[-la:]}+{res_b[-lb:]}={res_c[-lc:]}")