from collections import deque

def is_palidrome(input_letters) -> bool:
    cleaned_letters = ''.join(input_letters.lower().split()) # робимо не чутливий рядок до пробілів та регістру
    deq = deque(cleaned_letters) # створюємо чергу
    while len(deq) > 1: # створюємо цикл
        if deq.pop() != deq.popleft(): # задаємо умову для чи запис є паліндром
            return  " Не поліндром "
    return  " Поліндром "
print(is_palidrome("L ool")) # перевіряємо вводячи текст
