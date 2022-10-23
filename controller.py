import model
import view


def button_click():
    pos = 1
    while pos:
        pos = view.menu()
        match pos:
            case 1:  # добавление сведений по сотруднику
               result = model.add_contact(view.input_contact())

            case 2:  # просмотр справочника
                view.output_directory(result)

            case 3:  # удаление всех сведений по сотруднику
                result = model.del_contact(view.all_del_contact())
                view.output_directory(result)

            case 4:  # экспорт справочника
                with open('bd.csv', 'a', encoding='utf-8') as file:
                    for value in model.lst_contact:
                        file.write(str(f'{value}\n'))
                file.close()
                print('Данные добавлены в файл bd.csv')

            case 5:  # импорт справочника и вывод на экран
                with open('bd.csv', 'r', encoding='utf-8') as lst_contact:
                    result = lst_contact.readlines()
                    print('Данные загруженые из файла bd.py')
                    view.output_directory(result)

            case 6: #редактирование данных сотрудника
                result = model.editing_data(view.editing_contact())
                                    
