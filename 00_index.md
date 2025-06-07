# Key points

+ spk_colors -> lista de colores predefinidos... import spk_colors
  
+ 00_base_Flet.py -> Esquema basico de Flet
  
+ 03_listaTareas.py -> Listas: agregar, actualizar, mostrar
  + ft.Container
  + ft.Column... controls []
  + ft.Row... controls []
  + ft.Text
  + ft.Colors
  + ft.ListTile
  + ft.Checkbox
  + ft.TextField
  + ft.FilledButton
  + ft.ListView
  + lista por comprension: selection = [t.title.value for t in tareas if t.leading.value]

+ 04_notasAdhesivas.py -> Grid: agregar, eliminar, mostrar, actualizar
  + ft.GridView
    + grid.controls.append
    + grid.controls.remove
  + ft.IconButton
  + on_click=lambda _:
  + page.update()
  
+ 05_galeria_productos.py
  + Manejo de archivos tipo imagen: import os, import base64
  + Manejo de errores con excepciones
  + try / except FileNotFoundError / except Exception as e:
  + ft.Image
  + ft.ElevatedButton
  + ft.ResponsiveRow -> Galeria de imagenes responsive... col={"sm":12, "md":6, "lg":3}
  + ft.Divider _______

+ 06_datatable_excel.py -> Genera Excel a partir de datatable
  + from openpyxl import Workbook
  + ft.DataTable -> data_table.rows.append
  + ft.DataRow
  + ft.DataCell
  + ft.SnackBar
  + page.overlay.append(snack_bar)
  
+ 07_tabs.py -> Tabs + dark mode
  + page.theme_mode
  + ft.Switch 
  + ft.Tabs
  + tabs=[ft.Tab()]
  + 
