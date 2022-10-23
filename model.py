import view
lst_contact = []


def add_contact(all_data): #добавление записи по сотруднику
    lst_contact.append(all_data)
    return lst_contact


def del_contact(del_str):#удаление записи по сотруднику
    del lst_contact[del_str]
    return lst_contact


def editing_data(edit):#внесение изменений по сотруднику
    print('Выбран сотрудник:')
    print(lst_contact[edit])
    lst_contact[edit] = view.menu1()
    return lst_contact
