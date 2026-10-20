# Caso 31: Equipo de desarrollo

## Reto individual
Consultar la cima de la pila sin retirar el elemento.

## Código base
Se conserva la estructura y los nombres de las clases del código inicial (`Nodo`, `ListaEnlazada`, `Pila` y `Cola`). Se completan los cinco TODO y se añade el método `cima()` a la clase `Pila`.

## Datos de prueba
- DEV01: Corregir error
- DEV02: Probar
- DEV03: Documentar

## Ejecutar
En una terminal, dentro de la carpeta donde está `main.py`, ejecuta:

```bash
python main.py
```

## Método del reto
`cima()` devuelve `self.items[-1]` sin usar `pop()`, por lo que consulta el último elemento sin retirarlo. Si la pila está vacía, devuelve `None`.
