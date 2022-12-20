def opn_f(n: str):
    '''
    :param n: Строка с именем файла.
    :return: -
    '''
    f = open(n)
    count: int = int(f.readline())
    num_list: list[str] = f.read().splitlines()
    if count < len(num_list):
        raise ZeroDivisionError()
    for i in range(count):
        print(num_list[i])
    f.close()


try:
    name: str = input('Введите имя файла: ')
    opn_f(name)
except FileNotFoundError:
    print("Такого файла нет!")
    rez: bool = False
except NameError:
    print("Такого имени нет!")
    rez: bool = False
except ValueError:
    print("Превая сторока имеет недопустимое значение!")
    rez: bool = False
except TypeError:
    print("Несовместимые аргументы!")
    rez: bool = False
except ZeroDivisionError:
    print('Неверные данные для итерации!!')
    rez: bool = False
except MemoryError:
    print("Недостаточно оперативной памяти!")
    rez: bool = False
except StopIteration:
    print("Неверные данные для итерации!*")
    rez: bool = False
except IndexError:
    print("Неверные данные для итерации!/")
    rez: bool = False
except:
    print("Fatality error!")
    rez: bool = False
else:
    rez: bool = True
finally:
    try:
        print(f"Try: {'Успешно' if rez else 'Провал'}")
    except NameError:
        print("Переменная не найдена")
    except:
        print("Fatality error!")
