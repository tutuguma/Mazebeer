# Mazebeer
Mazebeer es una herramienta simple pero poderosa para encontrar rutas óptimas en un mapa bidimensional.El mismo se basa en el algoritmo de búsqueda A* para determinar el camino más corto entre un punto de inicio y un punto final, evitando obstáculos en el mapa.

Visualización intuitiva: Observa tu mapa en una cuadrícula clara, donde:

⬜ indica espacios libres y transitables.
🚧 marca edificios u obstáculos infranqueables.
💧 representa agua u obstáculos que requieren rutas alternativas.
🔥 señala áreas bloqueadas temporalmente.
🧔 ilumina la ruta óptima encontrada.
🍺 marca el destino final, ¡tu recompensa por encontrar el camino!
Interacción amigable:

Personaliza tu mapa: Define sus dimensiones (filas y columnas) para adaptarlo a tus necesidades.
Coloca obstáculos estratégicamente: Decide dónde ubicar los obstáculos y elige su tipo (edificios, agua, áreas temporales).
Elige tu camino: Indica el punto de inicio y el destino final de tu ruta.
Inteligencia A:* PathFinderPy emplea el algoritmo A* para encontrar la ruta más corta y eficiente, considerando tanto la distancia recorrida como la distancia estimada al destino.
