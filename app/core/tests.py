from config.wsgi import *
from core.models import Type, Employee, Category


# LISTAR
# query = Type.objects.all()
# print(query)

# AGREGAR
# t = Type()
# t.name = 'Secretaria'
# t.save()
# t = Type(name = 'Custodio')
# t.save()

# EDITAR
# t = Type.objects.get(pk=1)
# t.name = 'Director General'
# t.save()

# ELIMINAR
# t = Type.objects.get(id=4)
# t.delete()

# LISTAR con método filter
# obj = Type.objects.filter(name__icontains='dir')
# obj = Type.objects.filter(name__startswith='D')
# obj = Type.objects.filter(name__endswith='a')
# obj = Type.objects.filter(name__contains='Dir').count()
# obj = Type.objects.filter(name__contains='Dir').query
# obj = Type.objects.filter(name__startswith='Dir').exclude(id=5) # Se excluye el Dir RRHH que cuenta con id 5 en la tabla

# for i in Type.objects.filter(name__startswith='Dir')[1:]: # que traiga los últimos 2
#     print(i.name)

# e = Employee()
# e.names = 'Juan Carlos Aliaga'
# e.dni = '89111220724'
# e.age = 33
# e.type_id = 2
# e.salary = 350.0
# e.save()

for i in Employee.objects.filter(type_id=2):
    tipo = Type.objects.get(id=i.type_id)
    print(f'Trabajador: {i.names} \nEdad: {i.age} años \nSalario: {i.salary} CUP \nTipo: {tipo.name}')