import networkx as nx

COLOR_BORDE = '#bbbbbb'
ANCHO_BORDE = 2
TAM_NODOS = 3000
COLOR_FRONTERA_NODO = COLOR_BORDE
ANCHO_FRONTERA_NODO = 3
COLOR_NODO_NORMAL = '#3492d9'
FUENTE_COLOR_NODO = '#2cb64e'
COLOR_NODO_OBSERVADO = '#d96b34'
COLOR_NODO_ACCESIBLE = FUENTE_COLOR_NODO
FORMA_FUENTE_NODO = 'd'
COLOR_ETIQUETA = '#111111'


class Variable:
    def __init__(self, nombre, dominio):
        self.nombre = nombre
        self.dominio = dominio


class BayesNet(nx.DiGraph):
    """Representa una red Bayesiana como un grafo dirigido."""

    def __init__(self):
        super(BayesNet, self).__init__()

    def obtener_antepasados(self, variables):
        """Obtener todos los ancestros de las variables dadas.

        Argumentos
        ---------
        variables : iterable o str

        Retorna
        -------
        Un conjunto con los antepasados.
        """
        a_visitar = set(variables)
        antepasados = set()
        while a_visitar:
            break  # TODO: Implementa esto.
        return antepasados

    def obtener_accesibles(self, x, observado=None, plot=False):
        """Obtiene todos los nodos que son accesibles desde x, dados los nodos observados.

        Argumentos
        ---------
        x : str
            Nodo origen.

        observado : iterable of str
            Un conjunto de variables observadas. El valor predeterminado es None (sin observaciones)

        plot : bool
            Si es TRUE, dibuja la red con colores distintivos para nodos observables, 
            alcanzables y d-separation.

        Retorna
        -------
        El conjunto de nodos accesibles.
        """
        if observado is None:
            observado = []
        observado = set(observado)
        assert x in self.nodes()
        assert observado <= set(self.nodes())
        # Primero, encuentra a todas las antepasados del conjunto observado
        antepasados = self.obtener_antepasados(observado)
        # Luego, realiza una busqueda de variables accesibles a partir de x.
        # Los nodos a visitar se almacenan como tuplas con los siguientes elementos:
        #         * la variable
        #         * True, si la variable se alcanza a traves de un borde entrante
        #           False, si se alcanza a través de un borde de salida.
        # Cualquier variable que se alcanza a traves de una ruta activa se almacena en
        # accesible.
        a_visitar = set([(x, False)])
        visitado = set()
        accesible = set()
        while a_visitar != set():
            actual = a_visitar.pop()
            variable, camino_ingresado = actual
            if actual in visitado:
                continue
            if variable not in observado:
                accesible.add(variable)
            visitado.add(actual)
            # <--- V
            if not camino_ingresado and variable not in observado:
                pass  # TODO: Implementa esto.
            # ---> V
            elif camino_ingresado:
                pass  # TODO: Implementa esto.
        # Solo una convencion para no devolver el nodo de consulta.
        accesible.discard(x)
        # Grafico opcional.
        if plot:
            self.dibujaRB(x, observado, accesible)
        return accesible

    def dibujaRB(self, x=None, observado=None, dependiente=None):
        """Dibuja la red Bayesiana.

        Argumentos
        ---------
        x : str
            La variable origen.

        observado : iterable de str
            Las variables a las que condicionamos.

        dependiente : iterable de str
            Las variables que son dependientes de ``x`` dado ``observado``.
        """
        pos = nx.spectral_layout(self)
        nx.draw_networkx_edges(self, pos,
                               edge_color=COLOR_BORDE,
                               width=ANCHO_BORDE)
        rest = list(
            set(self.nodes()) - set([x]) - set(observado) - set(dependiente))
        if rest:
            obj = nx.draw_networkx_nodes(self, pos, nodelist=rest,
                                         node_size=TAM_NODOS,
                                         node_color=COLOR_NODO_NORMAL)
            obj.set_linewidth(ANCHO_FRONTERA_NODO)
            obj.set_edgecolor(COLOR_FRONTERA_NODO)
        if x:
            obj = nx.draw_networkx_nodes(self, pos, nodelist=[x],
                                         node_size=3000,
                                         node_color=FUENTE_COLOR_NODO,
                                         node_shape=FORMA_FUENTE_NODO)
            obj.set_linewidth(ANCHO_FRONTERA_NODO)
            obj.set_edgecolor(COLOR_FRONTERA_NODO)
        if observado:
            obj = nx.draw_networkx_nodes(self, pos, nodelist=list(observado),
                                         node_size=TAM_NODOS,
                                         node_color=COLOR_NODO_OBSERVADO)
            obj.set_linewidth(ANCHO_FRONTERA_NODO)
            obj.set_edgecolor(COLOR_FRONTERA_NODO)
        if dependiente:
            obj = nx.draw_networkx_nodes(self, pos, nodelist=list(dependiente),
                                         node_size=TAM_NODOS,
                                         node_color=COLOR_NODO_ACCESIBLE)
            obj.set_linewidth(ANCHO_FRONTERA_NODO)
            obj.set_edgecolor(COLOR_FRONTERA_NODO)
        nx.draw_networkx_labels(self, pos, font_color=COLOR_ETIQUETA)
