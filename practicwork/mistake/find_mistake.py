def opn_f(n):
    f = open(n)
    count = int(f.readline())
    num_list = f.read().splitlines()
    if count < len(num_list):
        raise ZeroDivisionError()
    for i in range(count):
        print(num_list[i])
    f.close()


try:
    name = input('Введите имя файла: ')
    print(opn_f(name))
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
    print('Неверные данные для итерации!!')
    rez = False
except MemoryError:
    print("Недостаточно оперативной памяти!")
    rez = False
except StopIteration:
    print("Неверные данные для итерации!*")
    rez = False
except IndexError:
    print("Неверные данные для итерации!/")
    rez = False
except:
    print("Fatality error!")
    rez = False
else:
    print(opn_f(name))
    rez = True
finally:
    try:
        print(f"Try: {'Успешно' if rez else 'Провал'}")
    except NameError:
        print("Переменная не найдена")
    except:
        print("Fatality error!")
