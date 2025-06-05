import flet as ft

def main(page: ft.Page):
    page.title = "Card Example"
    page.theme_mode = ft.ThemeMode.LIGHT

    def add_note(e):
        pass

    page.add(

        # Main container 
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLUE_GREY_800,

            content=ft.Card(
                shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                elevation=10,
                color=ft.Colors.RED_500,
                # ??? redondes de los bordes?
                # shape=8,
              
                content=ft.Container(
                    width =400,
                    height=200,  
                    padding=0,
                    alignment=ft.alignment.center, 
                    # bgcolor=ft.Colors.BLUE_700,
                    # border_radius=30,

                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30,

                        controls=[
                          
                            ft.ListTile(
                                bgcolor=ft.Colors.RED_700,
                                text_color=ft.Colors.WHITE,
                                
                                leading=ft.Icon(ft.Icons.ALBUM, color=ft.Colors.WHITE),
                                title=ft.Text("The Enchanted Nightingale"),
                                subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein."),
                            ),

                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,

                                controls=
                                [
                                    # ???tamano de los botones, hacerlos iguales los dos
                                    ft.ElevatedButton(
                                        "Buy tickets",
                                        style=ft.ButtonStyle(color=ft.Colors.GREY_800, padding=10)
                                    ),
                                    
                                    ft.TextButton(
                                        "Listen",
                                        style=ft.ButtonStyle(color=ft.Colors.GREY_200, 
                                                             padding=10, bgcolor=ft.Colors.GREY_500)
                                    ),

                                    # ??? formato del icon boton
                                    ft.IconButton(
                                        icon=ft.Icons.ADD, on_click=add_note, 
                                        icon_color=ft.Colors.BLACK, bgcolor=ft.Colors.GREY_100
                                        # style=ft.ButtonStyle(color=ft.Colors.GREY_200, 
                                                            #  padding=10, bgcolor=ft.Colors.PINK_500)
                                    ),
                                ],
                            ),
                        ],
                    )
                ),
            )
        )
    )

ft.app(main)
