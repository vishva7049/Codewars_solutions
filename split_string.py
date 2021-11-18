def solution(s):
  l1 = []
  s1 = ''

  if s== 0 :
      return s

  for i in s:
      s1 += i
      if len(s1) == 2:
          l1.append(s1)
          s1 = ''

  if len(s1)==1:
      l1.append(s1 + '_')

  return l1

print(solution('vishv'))
print(solution(''))