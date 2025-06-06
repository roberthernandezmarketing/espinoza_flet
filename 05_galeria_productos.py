import flet as ft
import os
import base64

def main(page: ft.Page):
    page.title = "Galeria de productos responsive"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900

    title = ft.Container(
        alignment=ft.alignment.center,
        padding=5,

        content=ft.Text(value="GALERIA DE PRODUCTOS",
                         size=24,
                         color=ft.Colors.GREY_200
                         )
    )

    def create_product(name, price, color, image):
        image_path = os.path.join(os.path.dirname(__file__), "assets", image)
        image_base64_string = None # Inicializamos a None

        try:
            with open(image_path, "rb") as image_file:
                # ¡La corrección clave está aquí!
                # Lee los bytes binarios y codifícalos directamente a una cadena Base64.
                image_base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        except FileNotFoundError:
            print(f"Warning: image {image} not found in {image_path}")
            image_base64_string = None # Aseguramos que sigue siendo None si no se encuentra
        except Exception as e:
            print(f"Error reading or encoding image {image}: {e}")
            image_base64_string = None


        return ft.Container(
            bgcolor=color,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
            width=200,
            height=350,

            content=ft.Column(
                controls=[
                    # Usamos image_base64_string directamente en src_base64
                    ft.Image(
                        src_base64=image_base64_string, 
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN,
                        error_content=ft.Text("Image load error") 
                    )
                    if image_base64_string else ft.Text("Image not found"), 

                    ft.Text(name, size=16, weight=ft.FontWeight.BOLD),
                    # ft.Text(value="ajsdh adsjAH SDSD sjfhs sdfjhsd sdjdfhs sdjfhsdfs dfsjhfs fsdjh fs", size=12),
                    ft.Text(value=f"${price}", size=14),
                    ft.ElevatedButton(text="Add to cart", color=ft.Colors.WHITE),
                ]
            )
        )

    products = [
        create_product(name="Product 1", price=19.99, color=ft.Colors.BLUE_500,   image="product1.png"),
        create_product(name="Product 2", price=29.99, color=ft.Colors.GREEN_500,  image="product4.png"),
        create_product(name="Product 3", price=39.99, color=ft.Colors.ORANGE_500, image="product3.png"),
        create_product(name="Product 4", price=49.99, color=ft.Colors.PURPLE_500, image="product4.png"),
        create_product(name="Product 5", price=39.99, color=ft.Colors.ORANGE_800, image="product8.png"),
        create_product(name="Product 6", price=19.99, color=ft.Colors.BLUE_200,   image="product3.png"),
        create_product(name="Product 7", price=49.99, color=ft.Colors.PURPLE_300, image="product7.png"),
        create_product(name="Product 8", price=29.99, color=ft.Colors.GREEN_700,  image="product8.png"),
    ]

    gallery = ft.ResponsiveRow(
        [ft.Container(product, col={"sm":12, "md":6, "lg":3}) for product in products],
        run_spacing=20,
        spacing=20
    )

    main_container = ft.Column (
        scroll=ft.ScrollMode.AUTO, expand=True, 
        
        controls=
        [
          title,
          ft.Divider(height=20, color=ft.Colors.WHITE24),
          gallery
        ], 
    )


    page.add(main_container)

ft.app(target=main)