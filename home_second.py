from collections import deque

def is_palidrome(letters) -> bool:
    deq = deque()
    for  letter in letters:
        if deq.pop() != deq.popleft():
            print(" Не поліндром ")
        else:
            deq.pop() 
            deq.popleft()
        print( " Поліндром ")
    return deq
 is_palidrome(lool)  
