import flet as ft
from openpyxl import Workbook
from datetime import datetime

def main(page: ft.Page):
    page.title = "DataTable & Excel"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Container(
        alignment=ft.alignment.center,
        padding=5,
        bgcolor=ft.Colors.PINK_500,

        content=ft.Text(value=page.title, size=24, color=ft.Colors.GREY_200)
    )
    
    data_table = ft.DataTable(
        bgcolor=ft.Colors.BLUE_GREY_700,
        border=ft.border.all(width=2, color=ft.Colors.BLUE_GREY_200),
        border_radius=10,
        vertical_lines=ft.BorderSide(3, color=ft.Colors.BLUE_GREY_200),
        horizontal_lines=ft.BorderSide(1, color=ft.Colors.BLUE_GREY_400),

        columns= [
          ft.DataColumn(ft.Text(value="ID", color=ft.Colors.BLUE_200, width=20)),
          ft.DataColumn(ft.Text(value="Name", color=ft.Colors.BLUE_200, width=200)),
          ft.DataColumn(ft.Text(value="Age", color=ft.Colors.BLUE_200, width=50)),
        ],

        rows=[]
    )

    def add_row(e):
      new_row = ft.DataRow(
        cells=[
          ft.DataCell(ft.Text(str(len(data_table.rows) + 1), color=ft.Colors.WHITE)),
          ft.DataCell(ft.Text(input_name.value, color=ft.Colors.WHITE)),
          ft.DataCell(ft.Text(input_age.value, color=ft.Colors.WHITE)),
        ]
      )

      data_table.rows.append(new_row)
      input_name.value = ""
      input_age.value  = ""

      page.update()

    def save_excel(e):
      wb = Workbook()
      ws = wb.active
      ws.title = "BBDD"
      ws.append(["ID", "Name", "Age"])

      for row in data_table.rows:
          ws.append([cell.content.value for cell in row.cells])

      date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
      file_name = f"PY_data_table_{date_time}.xlsx"

      wb.save(file_name)
      print (f"\nFile saved: {file_name}")

      snack_bar = ft.SnackBar(
        bgcolor=ft.Colors.WHITE,
        width=100,

        content=ft.Text(f"File saved: {file_name}", color=ft.Colors.BLACK)
      )

      page.overlay.append(snack_bar)
      snack_bar.open = True
      page.update()

    input_name = ft.TextField(label="Name", bgcolor=ft.Colors.BLUE_GREY_700, color=ft.Colors.WHITE)
    input_age  = ft.TextField(label="Age", bgcolor=ft.Colors.BLUE_GREY_700, color=ft.Colors.WHITE, width=80)
    add_button = ft.ElevatedButton(text="Add", on_click=add_row, color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE, width=120)
    save_button = ft.ElevatedButton(text="Save to Excel", on_click=save_excel, color=ft.Colors.WHITE, bgcolor=ft.Colors.GREEN, width=120)


    input_container = ft.Row (
      alignment=ft.MainAxisAlignment.CENTER,

      controls=[
          input_name,
          input_age,
          add_button,
          save_button
      ]
    )


    page.add(title, data_table, input_container)

ft.app(target=main)