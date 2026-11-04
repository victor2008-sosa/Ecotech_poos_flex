from dominio .empleado import  Empleado

emp = Empleado("juanito", "correo@mail.cl")

emp2 = Empleado(
    nombre="julio",
    correo="julio@gmail.cl"
)

print(emp.mostrar_datos())
print(emp2.mostrar_datos())
