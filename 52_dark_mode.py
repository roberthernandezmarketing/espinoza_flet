import flet as ft
import spk_colors

def main(page: ft.Page):
    page.title = "Dark Mode Switch"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = spk_colors.spk_bg_dark
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_maximized = True
    page.padding = 20

    is_dark = True  # Modo oscuro por defecto

    # ---------- Título principal ----------
    title_text = ft.Text(
        value="SparkCard App",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=spk_colors.spk_white,
        font_family="Roboto"
    )

    # ---------- Icono de tema ----------
    theme_icon = ft.IconButton(
        icon=ft.Icons.NIGHTLIGHT_ROUND,  # luna
        icon_color=spk_colors.spk_white,
        tooltip="Cambiar tema",
        on_click=lambda e: toggle_theme()
    )

    # ---------- Texto de contenido ----------
    lorem_text = ft.Text(
        value=(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\n"
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n"
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\n"
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n\n"
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n"
            "Donec sollicitudin molestie malesuada. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus.\n\n"
            "Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.\n\n"
            "Pellentesque in ipsum id orci porta dapibus. Nulla porttitor accumsan tincidunt."
        ),
        size=16,
        color=spk_colors.spk_white,
        expand=True
    )

    # ---------- Callback de cambio de tema ----------
    def toggle_theme():
        nonlocal is_dark
        is_dark = not is_dark

        if is_dark:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = spk_colors.spk_bg_dark
            title_bar.bgcolor = spk_colors.spk_bg_dark
            title_text.color = spk_colors.spk_white
            lorem_text.color = spk_colors.spk_white
            theme_icon.icon = ft.Icons.NIGHTLIGHT_ROUND
            theme_icon.icon_color = spk_colors.spk_white
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = spk_colors.spk_bg_light
            title_bar.bgcolor = spk_colors.spk_bg_light
            title_text.color = spk_colors.spk_bg_dark
            lorem_text.color = spk_colors.spk_bg_dark
            theme_icon.icon = ft.Icons.WB_SUNNY
            theme_icon.icon_color = spk_colors.spk_bg_dark

        page.update()

    # ---------- Barra superior ----------
    title_bar = ft.Container(
        padding=10,
        bgcolor=spk_colors.spk_bg_dark,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                title_text,
                theme_icon
            ]
        )
    )

    # ---------- Columna izquierda ----------
    left_column = ft.Container(
        padding=10,
        content=lorem_text,
        expand=True
    )

    # ---------- Columna derecha: imagen ----------
    image_card = ft.Card(
        elevation=8,
        color=spk_colors.spk_white,
        shadow_color=spk_colors.spk_gray_light,
        content=ft.Container(
            padding=10,
            width=500,
            height=500,
            alignment=ft.alignment.center,
            content=ft.Image(
                src="assets/student.png",
                width=500,
                height=500,
                fit=ft.ImageFit.CONTAIN
            )
        )
    )

    right_column = ft.Container(
        padding=10,
        content=image_card,
        expand=True
    )

    # ---------- Layout principal ----------
    content_layout = ft.Row(
        controls=[left_column, right_column],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True
    )

    # ---------- Añadir a la página ----------
    page.add(title_bar, content_layout)

ft.app(target=main)
