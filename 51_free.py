import flet as ft

def main(page: ft.Page):
  page.title = "Free Design by rh"
  page.theme_mode = ft.ThemeMode.LIGHT
  page.bgcolor = ft.Colors.RED_200
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.padding = 5

  title=ft.Text(value="Text title", size=24, weight="bold", color=ft.Colors.BLACK, bgcolor=ft.Colors.BLUE_200)

  main_container = ft.Container (
    expand=True,
    bgcolor=ft.Colors.GREY_100,
    alignment=ft.alignment.center,

    content=ft.Row(

      alignment=ft.MainAxisAlignment.CENTER,

      controls=
      [

        ft.Icon(ft.Icons.ALBUM, color=ft.Colors.RED, size=48),

        ft.Text(value="main container", weight="bold", size=48),

        ft.Column(
          alignment=ft.MainAxisAlignment.CENTER, 

          controls=
          [

            ft.Text(value="col1"),
            ft.Text(value="col2"),

          ]

        )

      ]

    )
    
    
  )




  page.add(title, main_container)

ft.app(main)
