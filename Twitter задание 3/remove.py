#!/usr/bin/python3
from tempfile import mkstemp
from os import close
from shutil import move

def remove_dubl(file):
     ft, temp = mkstemp() # создать temp-файл
     lines = [] # уникальные строки из file
     with open(temp, 'w') as t, open(file) as f:
         for line in f: # читать file построчно
             if line not in lines: # для line, отсутствующих в lines
                 lines.append(line) # сохранить line в lines
                 t.write(line) # записать line в temp-файл
     close(ft) # закрыть temp-файл
     move(temp, file) # переместить/переименовать temp-файл в file

if __name__ == '__main__':
     remove_dubl('log.txt')