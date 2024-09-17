from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

""" VISTAS PARA EL CATALOGO DE PRODUCTOS """

from . models import Categoria, Producto

def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'productos':listaProductos,
        'categorias':listaCategorias,
    }
    return render(request,'index.html', context)


""" VISTAS PARA FILTRAR PRODUCTO POR CATEGORIA """

def productosPorCategoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()

    listaCategorias = Categoria.objects.all()

    context = {
        'categorias':listaCategorias,
        'productos':listaProductos,
    }
    
    return render(request,'index.html',context)


def productosPorNombre(request):
    """ vista para filtrado de productos por nombre """
    nombre = request.POST['nombre']
    
    listaProductos = Producto.objects.filter(nombre__icontains=nombre)
    listaCategorias = Categoria.objects.all()
    
    context = {
        'categorias':listaCategorias,
        'productos':listaProductos
    }
    
    return render(request,'index.html',context)


def productoDetalle(request,producto_id):
    """ vista para el detalle de producto"""
    
    #objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto,pk=producto_id)
    context = {
        'producto':objProducto
    }
    
    return render(request,'producto.html',context)
