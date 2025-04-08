"""import flet"""

import flet as ft

from utils import parse_questions
from topmenu import menubar
from components.menu import getcontrol


def main(page: ft.Page):

    page.appbar = ft.AppBar(
        title=ft.Text("Проект"),
        center_title=True,
        bgcolor=ft.Colors.BLUE,
    )

    # Добавим главное меню
    page.add(ft.Row([menubar], rotate=0))

    # def ok_clicked(e):
    #     print("OK clicked")

    # page.add(getcontrol())#  MyButton(text="OK?",onclick=ok_clicked))

    # функции обработки выхода
    def handle_window_event(e):
        if e.data == "close":
            page.open(confirm_dialog)

    page.window.prevent_close = True
    page.window.on_event = handle_window_event

    def yes_click(e):
        page.window.destroy()

    def no_click(e):
        print(type(e))
        page.close(confirm_dialog)

    confirm_dialog:AlertDialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Подтверждение"),
        content=ft.Text("Вы действительно хотите выйти?"),
        actions=[
            ft.ElevatedButton("Да", on_click=yes_click),
            ft.OutlinedButton("Нет", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Определим функцию для обработки результата выбора файла
    # def on_dialog_result(e: ft.FilePickerResultEvent):
    #     if e.files:
    #         #разберем файл с вопросами
    #         quests = parse_questions(e.files[0].path)
    #         print(quests)
    #         #return e.files[0] #quests

    # Создадим FilePicker c обработчиком события выбора
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    # и добавим его на страницу
    page.overlay.append(file_picker)
    page.update()

    # #Добавим кнопку  вызова file_picker
    # file_type = ft.FilePickerFileType.CUSTOM
    # page.add(ft.ElevatedButton("Открыть тест...",
    # on_click=lambda _: file_picker.pick_files(file_type=file_type,
    # dialog_title='File', allowed_extensions=['txt'],
    #  allow_multiple=False)))

    mbc: ft.Control = menubar.controls[0]
    sm = mbc.controls[0]  # Ссылка на меню "открыть тест"
    ex: ft.MenuItemButton = mbc.controls[2]  # Ссылка на меню "выход"

    sm.on_click = lambda _: file_picker.pick_files(
        file_type=file_type,
        dialog_title="File",
        allowed_extensions=["txt"],
        allow_multiple=False,
    )  # handle_color_click1
    ex.event_handlers["click"] = lambda _: page.open(confirm_dialog)


ft.app(main)
