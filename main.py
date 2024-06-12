import threading
import multiprocessing
import time
from Control_database import Database


def insert_ishchilar(thread_number):
    query = f"""
    INSERT INTO ishchilar (name, age, position) VALUES 
    ('Ali {thread_number}', 30, 'Manager'),
    ('Vali {thread_number}', 25, 'Developer'),
    ('Said {thread_number}', 28, 'Designer'),
    ('Nodir {thread_number}', 19, 'Coder'),
    ('Qodir {thread_number}', 28, 'SMM'),
    ('Oqil {thread_number}', 28, 'Flutter'),
    ('Sardor {thread_number}', 28, 'Android dev'),
    ('Dilshod {thread_number}', 21, 'Fronted dev')
    
    """
    db = Database()
    result = db.connection(query, 'insert')
    print(f"Thread {thread_number}: {result}")


def insert_telefonlar(thread_number):
    query = f"""
    INSERT INTO telefonlar (model, brand, price) VALUES 
    ('iPhone 12 {thread_number}', 'Apple', 999),
    ('Galaxy S21 {thread_number}', 'Samsung', 799),
    ('Pixel 5 {thread_number}', 'Google', 699),
    ('Iphone 15 {thread_number}', 'Apple', 1050),
    ('Galaxy a34 {thread_number}', 'Samsung', 280),
    ('Galaxy a35 {thread_number}', 'Samsung', 300),
    ('Redmi Note 13 {thread_number}', 'Xiomi Redmi', 450),
    ('Y90s  {thread_number}', 'Vivo', 400)
    """

    result = Database.connection(query, 'insert')
    print(f"Thread {thread_number}: {result}")


def thread_task(thread_number):
    insert_ishchilar(thread_number)
    insert_telefonlar(thread_number)


def process_task(process_number):
    insert_ishchilar(process_number)
    insert_telefonlar(process_number)


if __name__ == '__main__':
    threads = []
    for i in range(1, 9):
        thread = threading.Thread(target=thread_task, args=(i,))
        threads.append(thread)
        thread.start()
        time.sleep(1)

    for thread in threads:
        thread.join()

    processes = []
    for i in range(1, 9):
        process = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(process)
        process.start()
        time.sleep(1)

    for process in processes:
        process.join()
