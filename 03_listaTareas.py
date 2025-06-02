import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_50
    page.title   = "Listado de Tareas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(value="Lista de tareas",
                     size=30, weight=ft.FontWeight.BOLD)
    
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title=ft.Text(campo_tarea.value),
                                leading=ft.Checkbox(on_change=seleccionar_tarea))
        tareas.append(tarea)
        campo_tarea.value = ""
        actualizar_lista()
            
    def seleccionar_tarea(e):
        # lista por comprension
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        if seleccionadas:
          tareas_seleccionadas.value = "[Tareas Seleccionadas: " + ", ".join(seleccionadas) + "]"
        else: 
          tareas_seleccionadas.value = ""

        page.update()
    
    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()
    
    campo_tarea = ft.TextField(hint_text="Escribe una nueva tarea")
    boton_agregar = ft.FilledButton(text="Agrear tarea", on_click=agregar_tarea)

    lista_tareas = ft.ListView(expand=1, spacing=2)

    # tareas = ["GYM", "Store"]
    tareas = []

    tareas_seleccionadas = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD) 

    page.add(titulo, campo_tarea, boton_agregar, lista_tareas, tareas_seleccionadas)


ft.app(target=main)
