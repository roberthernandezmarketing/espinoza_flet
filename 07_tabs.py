import flet as ft
import spk_colors

def main(page: ft.Page):
    page.title = "TABS"

    # Start in DARK mode, with switch changes to LIGHT
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = spk_colors.spk_bg_dark

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_maximized = True
    page.padding=0

    title = ft.Container(
        alignment=ft.alignment.center,
        padding=0,
        bgcolor=spk_colors.spk_green,
        content=ft.Text(value=page.title, size=24, color=spk_colors.spk_bg_dark, font_family="Roboto")
    )

    # Change theme
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        # Updated the switch label to reflect the current theme.
        switch_theme.label = (
            "Modo Claro" if page.theme_mode == ft.ThemeMode.LIGHT else "Modo Oscuro"
        )
        # También cambiamos el bgcolor de la página para que la transición sea visible
        page.bgcolor = (
            # ft.Colors.WHITE # Un color claro para el modo claro
            spk_colors.spk_pink # Un color claro para el modo claro
            if page.theme_mode == ft.ThemeMode.LIGHT
            else spk_colors.spk_bg_dark # El gris oscuro para el modo oscuro
        )
        page.update()
    # -----------------------------------

    # --- Define el Switch para el cambio de tema ---
    # Lo creamos aquí para poder asignarlo como contenido de la tab3
    switch_theme = ft.Switch(
        label="Modo Oscuro", # Inicia como oscuro, para que el label sea "Modo Oscuro"
        value=True, # El valor inicial del switch (apagado=claro, encendido=oscuro)
        on_change=theme_changed,
        active_color=spk_colors.spk_green, # Color cuando el switch está activo (on)
        inactive_thumb_color=spk_colors.spk_gray_light, # Color del pulgar cuando inactivo (off)
        inactive_track_color=ft.Colors.GREY_600, # Color de la pista cuando inactivo (off)
        label_position=ft.LabelPosition.LEFT, # Posiciona el label a la izquierda del switch
    )
    # -----------------------------------------------

    content_tab1 = ft.Container(
        padding=20,
        bgcolor=spk_colors.spk_blue,
        expand=True, 
        content=ft.Text(value="Contenido de la Pestaña 1", size=18 , color=spk_colors.spk_white)
    )

    content_tab2 = ft.Container(
        padding=20,
        bgcolor=spk_colors.spk_violet,
        alignment=ft.alignment.top_left,
        expand=True, 
        content=ft.Column(
            controls=[
                ft.Text("Ejemplo de Switches:", color=spk_colors.spk_white, size=16),
                ft.Switch(label="Switch Apagado", value=False, label_position=ft.LabelPosition.RIGHT),
                ft.Switch(label="Switch Encendido", value=True, label_position=ft.LabelPosition.RIGHT),
                ft.Switch(label="Switch Deshabilitado", disabled=True, label_position=ft.LabelPosition.RIGHT),
                ft.Switch(
                    label="Switch con label a la izquierda",
                    label_position=ft.LabelPosition.LEFT),
            ]
        )
    )

    content_tab3 = ft.Container(
        padding=20,
        bgcolor=spk_colors.spk_bg_dark, # Puedes ponerle otro color para diferenciar la pestaña
        expand=True, 
        content=ft.Column(
            controls=[
                ft.Text("Ajustes de Tema:", color=spk_colors.spk_white, size=18),
                switch_theme, # Switch for theme changing
                ft.Divider(height=100, thickness=20, color=spk_colors.spk_green),
                ft.Text("TAB 3", color=spk_colors.spk_white, size=18),
    
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        )
    )

    tabs = ft.Tabs (
        selected_index=0,
        animation_duration=10, 
        divider_color=spk_colors.spk_bg_dark,
        expand=True, 
        indicator_color=spk_colors.spk_green,
        label_color=spk_colors.spk_white,
        unselected_label_color=spk_colors.spk_gray_light,
        # overlay_color={ft.MaterialState.HOVERED: ft.Colors.WHITE10},

        tabs=[
            ft.Tab(text="Tasks", icon=ft.Icons.LIST_ALT, content=content_tab1),
            ft.Tab(text="Profile", icon=ft.Icons.PERSON, content=content_tab2),
            ft.Tab(text="Setup", icon=ft.Icons.SETTINGS, content=content_tab3),
        ]
    )

    page.add(title, tabs)

ft.app(target=main)