import matplotlib.pyplot as plt

def plot_projection(data, labels, centroids=None, title='Proyección', xlabel='Componente 1', ylabel='Componente 2', figsize=(10, 6)):
    """
    Función para visualizar datos proyectados en un espacio bidimensional.

    Parameters:
    - data: array-like, forma (n_samples, 2)
      Datos proyectados en 2D.
    - labels: array-like, forma (n_samples,)
      Etiquetas para colorear los puntos.
    - centroids: array-like, forma (n_clusters, 2), opcional
      Coordenadas de los centroides a visualizar.
    - title: str, título de la gráfica.
    - xlabel: str, etiqueta del eje X.
    - ylabel: str, etiqueta del eje Y.
    - figsize: tuple, tamaño de la figura.
    """
    if data.shape[0] != len(labels):
        raise ValueError("El número de datos no coincide con el número de etiquetas")

    plt.figure(figsize=figsize)
    scatter = plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o')
    if centroids is not None:
        plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, label='Centroides')
        plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar(scatter, label='Cluster')
    plt.show()
