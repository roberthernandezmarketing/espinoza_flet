import flet as ft
import spk_colors

def main(page: ft.Page):
    page.title = "APP TITLE"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = spk_colors.spk_bg_dark
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Container(
        alignment=ft.alignment.center,
        padding=1,
        bgcolor=spk_colors.spk_bg_light,

        content=ft.Text(value="TITLE", size=24, color=spk_colors.spk_bg_dark, font_family="Roboto")
    )
    

    page.add(title)

ft.app(target=main)