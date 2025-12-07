"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import matplotlib.pyplot as plt

    # Crear carpeta de salida
    os.makedirs("files/plots", exist_ok=True)

    # Definir datos
    years = list(range(2001, 2011))
    data = {
        "Televisión": {
            "values": [74, 76, 75, 72, 70, 69, 70, 68, 68, 66],
            "color": "black"
        },
        "Periódico": {
            "values": [45, 43, 48, 46, 40, 35, 34, 34, 30, 31],
            "color": "gray"
        },
        "Radio": {
            "values": [18, 20, 17, 18, 16, 15, 14, 13, 16, 16],
            "color": "lightgray"
        },
        "Internet": {
            "values": [13, 14, 17, 20, 18, 20, 22, 22, 40, 41],
            "color": "dodgerblue",
            "marker": "o"
        }
    }

    # Configurar ghphico
    plt.figure(figsize=(8, 6))

    for label, info in data.items():
        plt.plot(
            years,
            info["values"],
            label=label,
            color=info["color"],
            marker=info.get("marker", None)
        )

    
        plt.text(
            years[0], info["values"][0],
            f"{label} {info['values'][0]}%",
            va="center", ha="right", color=info["color"]
        )

        # Etiqueta final (2010)
        plt.text(
            years[-1], info["values"][-1],
            f"{info['values'][-1]}%",
            va="center", ha="left", color=info["color"]
        )

    # Títulos y formato
    plt.title("Cómo la gente obtiene sus noticias", fontsize=14, weight="bold")
    plt.suptitle(
        "Una proporción creciente cita Internet como su fuente principal de noticias",
        y=0.85, fontsize=10
    )

    plt.xticks(years)
    plt.yticks([])
    plt.box(False)

    # save
    plt.savefig("files/plots/news.png", bbox_inches="tight")
    plt.close() 