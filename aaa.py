# python은 세미콜론 ;을 사용하지 않는다.
rubin = 1
print(rubin)
rubin = "바보"
print(rubin)

kdt = {
  "삼백오호" : "홀쭉",
  "공욱재" : "미남",
}
print(kdt["공욱재"])

kdt_order = ["우리는", "개발자", "입니다"]
print(kdt_order[0], kdt_order[1], kdt_order[2])

for index in kdt_order:
  print(index)
# def = defenition 정의하다
def percent_calc(real_value, total_value):
  result = (real_value / total_value) * 100
  return result

print(percent_calc(1, 3))