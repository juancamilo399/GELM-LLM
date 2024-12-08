# Fine Tune LLM: Método Socrático

Este proyecto consiste en la construcción de un modelo fine-tuneado basado en **GPT-4o-mini**. El objetivo principal es crear un modelo educativo que responda bajo el método socrático de enseñanza, promoviendo el aprendizaje mediante preguntas reflexivas y exploración guiada.

## Características del Proyecto

1. **Traducción del Dataset**: El dataset original fue traducido al español utilizando el siguiente [script](translate/main.py).

2. **Fine-Tuning del Modelo**: Se utilizó el siguiente [script](fine_tune.py) para entrenar el modelo base con el dataset traducido.

3. **Interfaz Web**: Se desarrolló una aplicación con Gradio [(`app.py`)](app.py) para interactuar con el modelo de manera sencilla a través de un chatbot.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu máquina:

- **Python 3.11 o superior**
- **pip** (gestor de paquetes de Python)
- **Virtualenv** para la gestión de entornos virtuales
- Acceso a la API de **Open AI**

---

## Instalación y Configuración

Sigue estos pasos para instalar y configurar el proyecto:

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local y accede al directorio del proyecto:

```bash
git clone https://github.com/juancamilo399/GELM-LLM.git

cd GELM-LLM

```

### 2. Crear el entorno virtual

``` bash
python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

```

### 3. Traducción de dataset

``` bash
python translate/main.py
```

### 3. Fine tune del modelo

``` bash
python fine_tune.py
```

### 4. Ejecucion applicación web

``` bash
gradio app.py
```

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE). Puedes usar, modificar y distribuir este proyecto bajo los términos de dicha licencia.

---

## Autores

Este proyecto fue desarrollado por:

- **[Juan Camilo Angel Hernandez](https://github.com/juancamilo399)**
- **[Juan Camilo Rojas Ortiz](https://github.com/Jcro15)**
