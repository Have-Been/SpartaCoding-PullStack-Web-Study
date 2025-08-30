import random

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)

lotto_numbers = generate_lotto_numbers()
print("로또 추천 번호: ", lotto_numbers)