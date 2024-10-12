import queue
import time
import random

def generate_request(request_queue, generate_id):
    request_empty = generate_id # створюємо нову заявку
    request_queue.put(request_empty) # додаємо заявку до черги
    print(f"Сформовану нову заявку: {request_empty}")

def process_reguest(request_queue):
    if not request_queue.empty(): # задаємо умови, якщо черга не пуста то робити 
        request_empty = request_queue.get() # видалити заявку
        print(f"Беремо реєструвати заявку: {request_empty}") # беремо реєструвати заявку
    else:
        print("Черга пуста")

def main(): # головний цикл програми, поки з нього не вийдемо.
    request_queue = queue.Queue()
    request_id = 0

    try: # щоб  зупинити цикл використати комбінацію клавіш Ctrl+C
        while True:
            time.sleep(1)
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)
            if  random.choice([True, False]):
                process_reguest(request_queue)
    except KeyboardInterrupt:
        print("Програма завершена")

if __name__=="__main__":
    main()

