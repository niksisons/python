def opn_f():
    itr = []
    f = open(name)
    count = int(f.readline())
    for i in range(count):
        itr.append(f.readline().strip())
    f.close()
    return itr


try:
    name = input('Введите имя файла: ')
    opn_f()
except FileNotFoundError:
    print("Такого файла нет!")
    rez = False
except NameError:
    print("Такого имени нет!")
    rez = False
except ValueError:
    print("Превая сторока имеет недопустимое значение!")
    rez = False
except TypeError:
    print("Несовместимые аргументы!")
    rez = False
except ZeroDivisionError:
    print("Нельзя делить на ноль!")
    rez = False
except MemoryError:
    print("Недостаточно оперативной памяти!")
    rez = False
except StopIteration:
    print("Неверные данные для итерации!")
    rez = False
except:
    print("Fatality error!")
    rez = False
else:
    print(opn_f())
    rez = True
finally:
    print(f"Try: {'Успешно'if rez else 'Провал'}")
