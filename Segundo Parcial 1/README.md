# Trabajo práctico: árboles y grafos en Python

## Contenido
- `main.py`: resolución de los dos ejercicios.
- `datos/pokemon.json`: muestra de 100 Pokémon con número, nombre, tipos, debilidades y datos de megaevolución/Gigamax.
- `datos/personajes.json`: los 12 personajes pedidos y los episodios I–IX en los que aparecen.
- `datos/relaciones.json`: grafo no dirigido; cada objeto representa una relación y su peso es la cantidad de episodios compartidos.

Los archivos JSON contienen listas de objetos. En `pokemon.json`, los tipos y las debilidades son listas, y `megaevolucion`/`gigamax` son valores booleanos (`true` o `false`). En `personajes.json`, `episodios` es una lista de números. En `relaciones.json`, `episodios_compartidos` es un número entero.

## Cómo ejecutar
Requiere Python 3.10 o superior. No necesita instalar librerías.

1. Descomprimí el ZIP.
2. Abrí una terminal dentro de la carpeta `tp_estructuras_python`.
3. Ejecutá:

```bash
python main.py
```

El programa hace las consultas del ejercicio Pokémon. Al principio permite consultar un número y un texto parcial del nombre; presioná Enter si querés omitir esas consultas. Después muestra listados, recorrido por niveles, debilidades y conteos. Luego imprime los resultados del grafo de Star Wars.

## Ejercicio 1: Pokémon
Los tres índices son árboles binarios de búsqueda: por nombre, por número y por tipo. Se puede buscar por número, buscar nombres por coincidencia parcial, listar los tipos Fantasma/Fuego/Acero/Eléctrico, ordenar por número y nombre, recorrer por niveles el árbol por nombre, contar tipos y formas especiales.

**Alcance de los datos:** el JSON contiene 100 Pokémon, no las 1025 especies de todas las generaciones. Como Jolteon, Lycanroc y Tyrantrum no están dentro de los primeros 100, el programa usa sus tipos conocidos para resolver la consulta de debilidades frente a ellos. Los indicadores de megaevolución y Gigamax están incluidos en los datos de esta muestra.

## Ejercicio 2: Star Wars
El grafo es no dirigido y ponderado. Se ejecuta Prim desde C-3PO, Yoda y Leia, se identifican las aristas con el máximo de episodios compartidos, se calculan caminos de menor suma de pesos entre los pares solicitados y se buscan personajes que aparecen en los nueve episodios.

Los archivos de Star Wars son una base de trabajo para los 12 personajes pedidos, basada en sus apariciones en las películas principales I–IX. Las apariciones de personajes en escenas breves, recuerdos o material de archivo pueden variar según el criterio usado por la cátedra; conviene contrastar esta tabla con la fuente que indique el docente. Las relaciones se calculan a partir de los episodios listados.

## Subir a GitHub
1. Creá un repositorio vacío en GitHub.
2. Copiá/subí `main.py`, `README.md` y la carpeta `datos`.
3. Para subir desde una terminal, reemplazá `USUARIO/REPOSITORIO` por tu dirección real:

```bash
git init
git add main.py README.md datos/
git commit -m "Resuelvo trabajo práctico de árboles y grafos"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```
