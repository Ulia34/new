import flet as ft
from components.mybutton import MyButton
from components.menu import navMenu

from flet import TextField


def main(page: ft.Page):
    page.title = "Пример"
    page.add(navMenu())

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
