import flet as ft 

def main(page: ft.Page):
    page.bgcolor    = ft.Colors.BLUE_50
    page.title      = "Notas Adhesivas"
    page.padding    = 20
    page.theme_mode = "light"

    def add_note(e):
       new_note = create_note("New note")
       grid.controls.append(new_note)
       page.update()

    def delete_note(note):
       grid.controls.remove(note)   # Delete a grid element
       page.update()

    def create_note(text):
        note_content = ft.TextField(
          value=text, 
          multiline=True,
          bgcolor=ft.Colors.BLUE_GREY_50)
        
        note = ft.Container (
          content=ft.Column(
            [note_content, ft.IconButton(icon=ft.Icons.DELETE,
                                         on_click=lambda _: delete_note(note))]),

          width=200,
          height=200,
          bgcolor=ft.Colors.AMBER_400,  # gold color
          border_radius=10,
          padding=10
        )
        return note
    
    grid = ft.GridView(
      expand=True,          # Fill all container
      max_extent=220,       # Max width size of Grid
      child_aspect_ratio=1, # width = heigh
      horizontal=False,     # orientation by default is False
      spacing=20,           # if horizontal = False -> under
      run_spacing=20,       # if horizontal = False -> lateral
    )

    notes = [
      "GYM",
      "Barber",
      "Car Wash",
      "Super",
      "School",
      "Office",
      "Meeting 3pm"
    ]

    for note in notes:
      grid.controls.append(create_note(note))   # Create a grid element

    page.add(
       
      ft.Row([

        ft.Text(value="Mis notas Adhesivas", size=24, weight="bold", color=ft.Colors.BLACK),

        ft.IconButton(icon=ft.Icons.ADD, on_click=add_note, icon_color=ft.Colors.BLACK)

      ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), 

      grid
             
    )



ft.app(target=main)