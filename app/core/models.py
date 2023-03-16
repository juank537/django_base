from django.db import models
from datetime import datetime


class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']


class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=11, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    # gender = models.CharField(max_length=50, default='-')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True,
                               blank=True)  # La carpeta de imágenes se configura en el settings.py
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']  # Descendente ['-id']


class Provincia(models.Model):
    provincia = models.CharField(max_length=100, verbose_name='Provincia')
    codigo = models.PositiveIntegerField(verbose_name='Código')

    def __str__(self):
        return self.provincia

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        db_table = 'provincias'
        ordering = ['codigo']


class Municipio(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    municipio = models.CharField(max_length=100, verbose_name='Municipio')
    codigo = models.PositiveIntegerField(verbose_name='Código')

    def __str__(self):
        return self.municipio

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        db_table = 'municipios'
        ordering = ['codigo']


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'categorias'
        ordering = ['id']


class Cargo(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargos'
        ordering = ['id']


class Area(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
        db_table = 'areas'
        ordering = ['id']


class Empresa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    prefijo = models.PositiveIntegerField(default=0)
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    alias = models.CharField(max_length=60, verbose_name='Alias')
    pizarra = models.CharField(max_length=8, default='-', verbose_name='Pizarra')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')
    logo = models.ImageField(upload_to='logos/%Y/%m/%d', null=True, blank=True, verbose_name='Logo')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'empresas'
        ordering = ['id']


class Extension(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
    display_name = models.CharField(max_length=100, verbose_name='Descripción')
    extension = models.CharField(max_length=5, verbose_name='Extensión')
    name = models.CharField(max_length=60, verbose_name='Nombre')
    middle_name = models.CharField(max_length=60, verbose_name='Primer Apellido')
    last_name = models.CharField(max_length=60, verbose_name='Segundo Apellido')
    email = models.EmailField(verbose_name='Correo electrónico')  # buscar validacion de este tipo de campo
    phone = models.CharField(max_length=8, verbose_name='Teléfono fijo')
    mobile = models.CharField(max_length=8, verbose_name='Celular')
    active = models.BooleanField(default=True, verbose_name='Activo')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')
    date_desactivate = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de eliminación')

    def __str__(self):
        return self.display_name + ' - ' + self.extension

    class Meta:
        verbose_name = 'Extensión'
        verbose_name_plural = 'Extensiones'
        db_table = 'extensiones'
        ordering = ['extension']
