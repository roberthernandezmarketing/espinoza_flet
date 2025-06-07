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

    # Cambia dinámicamente los colores según el modo
    def update_theme():
        is_light = page.theme_mode == ft.ThemeMode.LIGHT
        page.bgcolor = spk_colors.spk_bg_light if is_light else spk_colors.spk_bg_dark
        title_text.color = spk_colors.spk_bg_dark if is_light else spk_colors.spk_white
        title_bar.bgcolor = spk_colors.spk_bg_light if is_light else spk_colors.spk_bg_dark
        theme_switch.label = "Modo Claro" if is_light else "Modo Oscuro"
        for text in lorem_texts:
            text.color = spk_colors.spk_bg_dark if is_light else spk_colors.spk_white
        page.update()

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        update_theme()

    # ---------- Título + switch ----------
    title_text = ft.Text(
        value="SparkCard App",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=spk_colors.spk_white,
        font_family="Roboto"
    )

    theme_switch = ft.Switch(
        scale=.8,  # switch height
        value=True,
        label="Modo Oscuro",
        on_change=toggle_theme,
        active_color=spk_colors.spk_green,
        inactive_thumb_color=spk_colors.spk_gray_light,
        inactive_track_color=ft.Colors.GREY_600,
        label_position=ft.LabelPosition.LEFT
    )

    title_bar = ft.Container(
        padding=10,
        bgcolor=spk_colors.spk_bg_dark,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[title_text, theme_switch]
        )
    )

    # ---------- Texto largo con múltiples párrafos ----------
    lorem_paragraph = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    )

    lorem_texts = [
        ft.Text(value=lorem_paragraph, size=16, color=spk_colors.spk_white),
        ft.Text(value=lorem_paragraph, size=16, color=spk_colors.spk_white),
        ft.Text(value=lorem_paragraph, size=16, color=spk_colors.spk_white),
        ft.Text(value=lorem_paragraph, size=16, color=spk_colors.spk_white),
        ft.Text(value=lorem_paragraph, size=16, color=spk_colors.spk_white),
    ]

    left_column = ft.Container(
        padding=10,
        expand=True,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=15,
            controls=lorem_texts
        )
    )

    # ---------- Imagen con ruta correcta ----------
    image_card = ft.Card(
        elevation=8,
        color=spk_colors.spk_blue,
        shadow_color=spk_colors.spk_gray_light,
        content=ft.Container(
            padding=10,
            width=350,
            height=350,
            alignment=ft.alignment.center,
            content=ft.Image(
                src="assets/student.png",  # Ruta actualizada
                width =500,
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

    # ---------- Layout principal de contenido ----------
    content_layout = ft.Row(
        controls=[left_column, right_column],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True
    )

    # ---------- Mostrar en la página ----------
    page.add(title_bar, content_layout)
    update_theme()  # Inicializar los colores

ft.app(target=main)
