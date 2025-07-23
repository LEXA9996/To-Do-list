from . import read_task, delete_task, add_task, edit_task, export
def back_menu():
    while True:
        return_menu = input("Хотите вернуться в меню? Да [y] 😊, Нет [n] 👋: ")
        if return_menu.lower() == "y":
            menu()
            break
        elif return_menu.lower() == "n":
            print("Спасибо за использование программы! До свидания! 👋")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова. 🤔")
            continue


def menu():
    while True:
        try:
            choice = int(input(
                "\nЗдравствуйте! 👋\n"
                "Выберите действие:\n"
                "1. Посмотреть список текущих задач 📋\n"
                "2. Добавить новую задачу ➕\n"
                "3. Отметить задачу как выполненную ✅\n"
                "4. Изменить активную задачу ✏️\n"
                "5. Посмотреть список выполненных задач 🎉\n"
                "6. Скачать файл с активными и выполненными задачами 📁\n"
                "7. Удалить задачу 🗑️\n"
                "8. Выйти из программы 🚪\n"
                "Ваш выбор: "
            ))
        except ValueError:
            print("Пожалуйста, вводите только цифры от 1 до 6. ❌")
            continue

        if choice == 1:
            read_task.read_task()
            break
        elif choice == 2:
            add_task.append_task()
            break
        elif choice == 3:
            add_task.mark_completed()
            break
        elif choice == 5:
            read_task.show_completed()
            break
        elif choice == 7:
            delete_task.delete_task()
            break
        elif choice == 8:
            print("Выход из программы. До новых встреч! 👋")
            break
        elif choice == 4:
            edit_task.edit()
            break
        elif choice == 6:
            export.export_task()
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите число от 1 до 6. 🤨")