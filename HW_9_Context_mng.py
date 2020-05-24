class Myopen:
    def __init__(self, file_path):
        self.file = open(file_path, encoding="utf-8")
        from datetime import datetime as dt
        self.open_time = dt.now()

    def __enter__(self):
        print(f'Время старта программы: {self.open_time}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        from datetime import datetime as dt
        self.close_time = dt.now()
        print(f'Время завершения программы: {self.close_time}')
        print(f'Время исполнения: {dt.now() - self.open_time}')

with Myopen('newfile.txt') as file:
    to_sort = []
    for line in file:
        f = file.readline().lower().split()
        to_sort.append(f)
    all = []
    for lst in to_sort:
        all = all + lst
    res = {}
    for word in all:
        if word in res.keys():
            res[word] += 1
        else:
            res[word] = 1
    max_word = max(res.values())
    final_dict = {key: value for key, value in res.items() if value == max_word}
    print(f'Самое часто употребляемое слово {final_dict}')