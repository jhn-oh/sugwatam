probability_list = [1/3, 1/3, 1/3]
next_probability_list = []

n_max = input("n의 최댓값을 입력하세요.")
n_max_int = int(n_max)
for n in range(3, n_max_int+1): #n_max_int-2번 시행
  next_probability_list.append(probability_list[0]/3)
  next_probability_list.append(probability_list[0]/3 + probability_list[1]/3)
  for k in range(2, len(probability_list)):
    next_probability_list.append(probability_list[k]/3 + probability_list[k-1]/3+probability_list[k-2]/3)
  next_probability_list.append(probability_list[-1]/3 + probability_list[-2]/3)
  next_probability_list.append(probability_list[-1]/3)
  print(next_probability_list)
  probability_list = next_probability_list
  next_probability_list = []

