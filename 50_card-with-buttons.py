import flet as ft

def main(page: ft.Page):
    page.title = "Card Example"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(

        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLUE_GREY_400,

            content=ft.Card(
              
                content=ft.Container(
                    width =400,
                    height=180,  
                    padding=0,
                    alignment=ft.alignment.center, 

                    content=ft.Column(

                        controls=[
                          
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.ALBUM, color=ft.Colors.WHITE),
                                title=ft.Text("The Enchanted Nightingale"),
                                subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein."),
                                # bgcolor=ft.Colors.GREY_50,
                                text_color=ft.Colors.WHITE,
                            ),

                            ft.Row(
                                controls=
                                [
                                    ft.ElevatedButton(
                                        "Buy tickets",
                                        style=ft.ButtonStyle(color=ft.Colors.GREY_800)
                                    ),
                                    
                                    ft.TextButton(
                                        "Listen",
                                        style=ft.ButtonStyle(color=ft.Colors.GREY_100)
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    )
                ),
                shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                elevation=10,
                color=ft.Colors.RED_500,
            )
        )
    )

ft.app(main)
