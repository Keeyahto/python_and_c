import subprocess
import timeit
import pickle

NUMBER_OF_ITERATIONS = 1000


def c_prog_call(i):
    subprocess.run('prog.exe', input=i)


def python_prog_call(i):
    subprocess.run('python python.py', input=i)


c_list = []
p_list = []
first_i = 0

for i in range(1, NUMBER_OF_ITERATIONS):
    c_list.append(timeit.timeit(f'c_prog_call(b"{i}")', number=5, globals=globals()) / 5)
    p_list.append(timeit.timeit(f'python_prog_call(b"{i}")', number=5, globals=globals()) / 5)
    if p_list[-1] < c_list[-1] and first_i == 0:
        first_i = i

print('i =', first_i)
print('Время исполнения python скрита:', p_list[-1])
print('Время исполнения с скрита:', c_list[-1])

with open('c_list', 'wb') as f:
    pickle.dump(c_list, f)

with open('p_list', 'wb') as f:
    pickle.dump(p_list, f)
