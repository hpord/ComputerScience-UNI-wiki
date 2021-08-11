function fusionar(rotulos = [], rangos = [], rotulo1 = 0, rotulo2 = 0) {
    let a = Math.min(rotulo1, rotulo2);
    let b = Math.max(rotulo1, rotulo2);
    if (rangos[a] === rangos[b]) {
        rotulos[b] = a;
        rangos[a]++;
    } else if (rangos[a] > rangos[b]) {
        rotulos[b] = a;
    } else {
        rotulos[a] = b;
    }
    return [rotulos, rangos];
}
function buscar(rotulos = [], elemento = 0) {
    //Buscar el rótulo del árbol que contiene el elemento
    let rotulo = elemento;
    while (rotulos[rotulo] !== rotulo) {
        rotulo = rotulos[rotulo];
    }
    //Compresión caminos
    let i = elemento;
    while (i !== rotulo) {
        [rotulos[i], i] = [rotulo, rotulos[i]];
    }
    return [rotulo, rotulos];
}
function construir(conjuntos = []) {
    let elementos = conjuntos.flat().sort();
    let n = elementos.length;
    let rotulos = [];
    for (let conjunto of conjuntos) {
        let rotulo = Math.min(...conjunto);
        for (let i = 0; i < conjunto.length; i++) {
            rotulos[conjunto[i]] = rotulo;
        }
    }
    let rangos = rotulos.map(v => 0);
    return [rotulos, rangos, elementos];
}
function kruskal(nodos = []) {
    let aristas = {};
    for (let nodo of nodos) {
        if (Array.isArray(nodo.parent)) {
            for (let link of nodo.parent) {
                if (typeof link === "object" && link.hasOwnProperty("value")) {
                    aristas[`${nodo.index},${link.index}`] = link.value;
                }
            }
        }
    }
    let aristasEnOrden = Object.keys(aristas).sort((a, b) => aristas[a] - aristas[b]);
    let conjuntosIniciales = nodos.map(v => [v.index]);
    let [rotulos, rangos, elementos] = construir(conjuntosIniciales);
    let rotulo1, rotulo2;
    let resultado = [];
    for (let arista of aristasEnOrden) {
        let [index1, index2] = arista.split(/,/).map(v => +v);
        [rotulo1, rotulos] = buscar(rotulos, index1);
        [rotulo2, rotulos] = buscar(rotulos, index2);
        if (rotulo1 !== rotulo2) {
            [rotulos, rangos] = fusionar(rotulos, rangos, rotulo1, rotulo2);
            resultado.push(arista);
            if (resultado.length === nodos.length - 1) break;
        }
    }
    return resultado;
}
grafo = [{ "index": 0, "parent": -1 },
{
    "index": 1, "parent":
        [{ "index": 0, "value": 2 }]
},
{
    "index": 2, "parent":
        [{ "index": 0, "value": 5 },
        { "index": 1, "value": 5 }]
},
{
    "index": 3, "parent":
        [{ "index": 1, "value": 3 },
        { "index": 4, "value": 4 }]
},
{
    "index": 4, "parent":
        [{ "index": 1, "value": 2 },
        { "index": 2, "value": 4 },
        { "index": 0, "value": 6 }]
}]

console.log(kruskal(grafo, n = 0));