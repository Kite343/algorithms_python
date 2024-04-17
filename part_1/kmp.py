#1. Алгоритм Кнута-Морриса-Пратта (КМП-алгоритм)
#  алгоритм, осуществляющий поиск подстроки в строке, 
# используя то, что при возникновении несоответствия 
# само слово содержит достаточно информации, 
# чтобы определить, где может начаться следующее совпадение,
#  минуя лишние проверки. 
# Время работы алгоритма линейно зависит от объёма входных данных,
#  то есть разработать асимптотически более эффективный алгоритм
#  невозможно.


def kmp(sample: str, line_data: str):
    m = len(sample)

    p = [0] * len(sample)
    i = 1
    j = 0
    while i < (len(sample)):
        if sample[j] == sample[i]:
            p[i] = j+1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j-1]

    n = len(line_data)
    i = 0
    j = 0
    while i < n:
        if line_data[i] == sample[j]:
            i += 1
            j += 1
            if j == m:
                print("образец найден")
                return (i - j, i - 1)
                # break
        else:
            if j > 0:
                j = p[j-1]
            else:
                i += 1
    else:
        print("образец не найден")
        return -1

    # if i == n and j != m:
    #     print("образец не найден")

if __name__ == "__main__":
    print(kmp('abcbabca','abcbabcabcbabcbabcbabcabcbabcbabca'))
    print(kmp('cbabca','abcbabcabcbabcbabcbabcabcbabcbabca'))
    print(kmp('abab','ababcabababc'))
    print(kmp('baba','ababcabababc'))