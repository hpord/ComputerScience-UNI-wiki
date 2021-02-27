import numpy as np
import numbers
import matplotlib.pyplot as plt
from separadores import *
from sklearn.utils import check_array, check_random_state
from sklearn.utils import shuffle as shuffle_
from sklearn.utils.deprecation import deprecated
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

def hacer_blobs(n_muestras=100, n_caracteristica=2, centros=2, cluster_std=1.0,
centro_caja=(-10.0, 10.0), shuffle=True, random_state=None):
    
    generador = check_random_state(random_state)

    if isinstance(centros, numbers.Integral):
        centros = generador.uniform(centro_caja[0], centro_caja[1],
                                    size=(centros, n_caracteristica))
    else:
        centros = check_array(centros)
        n_caracteristica = centros.shape[1]

    if isinstance(cluster_std, numbers.Real):
        cluster_std = np.ones(len(centros)) * cluster_std

    X = []
    y = []

    n_centros = centros.shape[0]
    if isinstance(n_muestras, numbers.Integral):
        n_muestras_por_centro = [int(n_muestras // n_centros)] * n_centros
        for i in range(n_muestras % n_centros):
            n_muestras_por_centro[i] += 1
    else:
        n_muestras_por_centro = n_muestras

    for i, (n, std) in enumerate(zip(n_muestras_por_centro, cluster_std)):
        X.append(centros[i] + generador.normal(scale=std,
                                               size=(n, n_caracteristica)))
        y += [i] * n

    X = np.concatenate(X)
    y = np.array(y)

    if shuffle:
        X, y = shuffle_(X, y, random_state=generador)

    return X, y
def dibujo_ilustracion_matriz_confusion():
    plt.figure(figsize=(8, 8))
    matriz_confusion = np.array([[401, 2], [8, 39]])
    plt.text(0.40, .7, matriz_confusion[0, 0], size=70, horizontalalignment='right')
    plt.text(0.40, .2, matriz_confusion[1, 0], size=70, horizontalalignment='right')
    plt.text(.90, .7, matriz_confusion[0, 1], size=70, horizontalalignment='right')
    plt.text(.90, 0.2, matriz_confusion[1, 1], size=70, horizontalalignment='right')
    plt.xticks([.25, .75], ["predecido 'no nueve'", "predecido 'nueve'"], size=20)
    plt.yticks([.25, .75], ["verdad 'nueve'", "verdad 'no nueve'"], size=20)
    plt.plot([.5, .5], [0, 1], '--', c='k')
    plt.plot([0, 1], [.5, .5], '--', c='k')

    plt.xlim(0, 1)
    plt.ylim(0, 1)

def dibuja_matriz_confusion_binaria():
    plt.text(0.45, .6, "TN", size=100, horizontalalignment='right')
    plt.text(0.45, .1, "FN", size=100, horizontalalignment='right')
    plt.text(.95, .6, "FP", size=100, horizontalalignment='right')
    plt.text(.95, 0.1, "TP", size=100, horizontalalignment='right')
    plt.xticks([.25, .75], ["prediccion negativa", "prediccion positiva"], size=15)
    plt.yticks([.25, .75], ["clase positiva", "clase negativa"], size=15)
    plt.plot([.5, .5], [0, 1], '--', c='k')
    plt.plot([0, 1], [.5, .5], '--', c='k')

    plt.xlim(0, 1)
    plt.ylim(0, 1)

def dibuja_umbral_decision():

    X, y = hacer_blobs(n_muestras=(400, 50), centros=2, cluster_std=[7.0, 2],
                      random_state=22)
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, random_state=0)

    fig, axes = plt.subplots(2, 3, figsize=(15, 8), subplot_kw={'xticks': (), 'yticks': ()})
    plt.suptitle("Umbral de decision")
    axes[0, 0].set_title("datos de entrenamiento")
    dibuja_dispersion_discreta(X_entrenamiento[:, 0], X_entrenamiento[:, 1], y_entrenamiento, ax=axes[0, 0])

    svc = SVC(gamma=.05).fit(X_entrenamiento, y_entrenamiento)
    axes[0, 1].set_title("decision con  umbral 0")
    dibuja_dispersion_discreta(X_entrenamiento[:, 0], X_entrenamiento[:, 1], y_entrenamiento, ax=axes[0, 1])
    dibuja_2d_puntuaciones(svc, X_entrenamiento, funcion="decision_function", alfa=.7,
                   ax=axes[0, 1], cm=ReBl)
    dibuja_separador_2d(svc, X_entrenamiento, ancholinea=3, ax=axes[0, 1])
    axes[0, 2].set_title("decision con umbral -0.8")
    dibuja_dispersion_discreta(X_entrenamiento[:, 0], X_entrenamiento[:, 1], y_entrenamiento, ax=axes[0, 2])
    dibuja_separador_2d(svc, X_entrenamiento, ancholinea=3, ax=axes[0, 2], umbral=-.8)
    dibuja_2d_puntuaciones(svc, X_entrenamiento, funcion="decision_function", alfa=.7,
                   ax=axes[0, 2], cm=ReBl)

    axes[1, 0].set_axis_off()

    mascara_bool= np.abs(X_entrenamiento[:, 1] - 7) < 5
    bla = np.sum(mascara_bool)

    linea = np.linspace(X_entrenamiento.min(), X_entrenamiento.max(), 100)
    axes[1, 1].set_title("Seccion cruzada con umbral 0")
    axes[1, 1].plot(linea, svc.decision_function(np.c_[linea, 10 * np.ones(100)]), c='k')
    dec = svc.decision_function(np.c_[linea, 10 * np.ones(100)])
    contorno = (dec > 0).reshape(1, -1).repeat(10, axis=0)
    axes[1, 1].contourf(linea, np.linspace(-1.5, 1.5, 10), contorno, alpha=0.4, cmap=cm2)
    dibuja_dispersion_discreta(X_entrenamiento[mascara_bool, 0], np.zeros(bla), y_entrenamiento[mascara_bool], 
                               ax=axes[1, 1])
    axes[1, 1].set_xlim(X_entrenamiento.min(), X_entrenamiento.max())
    axes[1, 1].set_ylim(-1.5, 1.5)
    axes[1, 1].set_xticks(())
    axes[1, 1].set_ylabel("Valor de decision")

    contorno2 = (dec > -.8).reshape(1, -1).repeat(10, axis=0)
    axes[1, 2].set_title("Seccion cruzada con umbral  -0.8")
    axes[1, 2].contourf(linea, np.linspace(-1.5, 1.5, 10), contorno2, alpha=0.4, cmap=cm2)
    dibuja_dispersion_discreta(X_entrenamiento[mascara_bool, 0], np.zeros(bla), y_entrenamiento[mascara_bool], 
                               alfa=.1, ax=axes[1, 2])
    axes[1, 2].plot(linea, svc.decision_function(np.c_[linea, 10 * np.ones(100)]), c='k')
    axes[1, 2].set_xlim(X_entrenamiento.min(), X_entrenamiento.max())
    axes[1, 2].set_ylim(-1.5, 1.5)
    axes[1, 2].set_xticks(())
    axes[1, 2].set_ylabel("Valor de decision")
    axes[1, 0].legend(['Clase negativa', 'Clase positiva'])

def mapa_calor(valores, xetiqueta, yetiqueta, xticklabels, yticklabels, cmap=None,
            vmin=None, vmax=None, ax=None, fmt="%0.2f"):
    if ax is None:
        ax = plt.gca()
    # dibuja los puntajes mediosde validación cruzada
    img = ax.pcolor(valores, cmap=cmap, vmin=vmin, vmax=vmax)
    img.update_scalarmappable()
    ax.set_xlabel(xetiqueta)
    ax.set_ylabel(yetiqueta)
    ax.set_xticks(np.arange(len(xticklabels)) + .5)
    ax.set_yticks(np.arange(len(yticklabels)) + .5)
    ax.set_xticklabels(xticklabels)
    ax.set_yticklabels(yticklabels)
    ax.set_aspect(1)

    for p, color, valor in zip(img.get_paths(), img.get_facecolors(),
                               img.get_array()):
        x, y = p.vertices[:-2, :].mean(0)
        if np.mean(color[:3]) > 0.5:
            c = 'k'
        else:
            c = 'w'
        ax.text(x, y, fmt % valor, color=c, ha="center", va="center")
    return img

