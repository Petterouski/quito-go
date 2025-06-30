Proyecto Quito-Go: Implementación de Abstract Factory con Docker
Descripción del Proyecto
Este proyecto demuestra una implementación práctica del patrón de diseño Abstract Factory en Python, encapsulado en contenedores Docker. El sistema permite crear familias de productos relacionados sin especificar sus clases concretas, siguiendo principios SOLID y buenas prácticas de diseño.

Características principales:

Implementación limpia del patrón Abstract Factory

Estructura modular fácilmente extensible

Contenerización con Docker para consistencia de entornos

Diseño listo para producción con prácticas modernas

Código completamente documentado y comentado

Prerrequisitos
Antes de ejecutar el proyecto, asegúrese de tener instalado:

Docker (versión 20.10 o superior)

Docker Compose (versión 1.29 o superior)

Git (opcional, solo para clonar el repositorio)

Instalación y Ejecución
Paso 1: Clonar el repositorio (opcional)
bash
git clone https://github.com/Petterouski/quito-go.git
cd quito-go
Paso 2: Construir la imagen Docker
bash
docker-compose build
Paso 3: Ejecutar el contenedor
bash
docker-compose up
Paso 4: Verificar la ejecución
En los logs del contenedor debería ver la siguiente salida:

text
== Usando Fábrica A ==
Operación desde Producto A

== Usando Fábrica B ==
Operación desde Producto B
Paso 5: Detener el contenedor
bash
docker-compose down