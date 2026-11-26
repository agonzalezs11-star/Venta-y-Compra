from django.urls import path
from . import views, models, forms
urlpatterns = [path("", views.inicio, name="inicio")]

lista_cliente, nuevo_cliente, editar_cliente, borrar_cliente = views.construir_vistas(models.Cliente, forms.ClienteForm, "Clientes")
urlpatterns += [
    path("cliente/", lista_cliente, name="lista_cliente"),
    path("cliente/nuevo/", nuevo_cliente, name="nuevo_cliente"),
    path("cliente/<int:pk>/editar/", editar_cliente, name="editar_cliente"),
    path("cliente/<int:pk>/eliminar/", borrar_cliente, name="borrar_cliente"),
]

lista_proveedor, nuevo_proveedor, editar_proveedor, borrar_proveedor = views.construir_vistas(models.Proveedor, forms.ProveedorForm, "Proveedores")
urlpatterns += [
    path("proveedor/", lista_proveedor, name="lista_proveedor"),
    path("proveedor/nuevo/", nuevo_proveedor, name="nuevo_proveedor"),
    path("proveedor/<int:pk>/editar/", editar_proveedor, name="editar_proveedor"),
    path("proveedor/<int:pk>/eliminar/", borrar_proveedor, name="borrar_proveedor"),
]

lista_marca, nuevo_marca, editar_marca, borrar_marca = views.construir_vistas(models.Marca, forms.MarcaForm, "Marcas")
urlpatterns += [
    path("marca/", lista_marca, name="lista_marca"),
    path("marca/nuevo/", nuevo_marca, name="nuevo_marca"),
    path("marca/<int:pk>/editar/", editar_marca, name="editar_marca"),
    path("marca/<int:pk>/eliminar/", borrar_marca, name="borrar_marca"),
]

lista_categoria, nuevo_categoria, editar_categoria, borrar_categoria = views.construir_vistas(models.Categoria, forms.CategoriaForm, "Categorías")
urlpatterns += [
    path("categoria/", lista_categoria, name="lista_categoria"),
    path("categoria/nuevo/", nuevo_categoria, name="nuevo_categoria"),
    path("categoria/<int:pk>/editar/", editar_categoria, name="editar_categoria"),
    path("categoria/<int:pk>/eliminar/", borrar_categoria, name="borrar_categoria"),
]

lista_producto, nuevo_producto, editar_producto, borrar_producto = views.construir_vistas(models.Producto, forms.ProductoForm, "Productos")
urlpatterns += [
    path("producto/", lista_producto, name="lista_producto"),
    path("producto/nuevo/", nuevo_producto, name="nuevo_producto"),
    path("producto/<int:pk>/editar/", editar_producto, name="editar_producto"),
    path("producto/<int:pk>/eliminar/", borrar_producto, name="borrar_producto"),
]

lista_compra, nuevo_compra, editar_compra, borrar_compra = views.construir_vistas(models.Compra, forms.CompraForm, "Compras")
urlpatterns += [
    path("compra/", lista_compra, name="lista_compra"),
    path("compra/nuevo/", nuevo_compra, name="nuevo_compra"),
    path("compra/<int:pk>/editar/", editar_compra, name="editar_compra"),
    path("compra/<int:pk>/eliminar/", borrar_compra, name="borrar_compra"),
]

lista_venta, nuevo_venta, editar_venta, borrar_venta = views.construir_vistas(models.Venta, forms.VentaForm, "Ventas")
urlpatterns += [
    path("venta/", lista_venta, name="lista_venta"),
    path("venta/nuevo/", nuevo_venta, name="nuevo_venta"),
    path("venta/<int:pk>/editar/", editar_venta, name="editar_venta"),
    path("venta/<int:pk>/eliminar/", borrar_venta, name="borrar_venta"),
]
