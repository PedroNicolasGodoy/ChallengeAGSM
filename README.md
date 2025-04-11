# 🚗 AGSM - Análisis y Predicción de Ventas

Este repositorio contiene los entregables desarrollados para una entrevista técnica con **AGSM**, una concesionaria de autos en la provincia de Mendoza.

El desafío consistió en, en tan solo **2 días**, entregar dos productos:

1. 📊 Un **tablero de visualización en Power BI** para entender el comportamiento de las ventas.
2. 🧠 Un **modelo predictivo de ventas**, comparando dos enfoques distintos (con y sin SMOTE), desplegado en una app de **Streamlit**.

---

## 🎯 Propósito del Proyecto

El objetivo fue dar respuesta a una serie de requerimientos:

- Crear un **dashboard que muestre el comportamiento de las ventas** en el tiempo.
- Visualizar diferencias por **producto**, **vendedor** y **por qué no se concretó** una venta.
- Desarrollar una **predicción supervisada** para anticipar si un proceso de venta va a finalizar con éxito o no.
- Identificar las **variables que más influyen** en una venta exitosa.

---

## 🖼️ Tablero en Power BI

El tablero fue desarrollado rápidamente, dentro del tiempo disponible, utilizando un solo lienzo que incluye:

- Visualizaciones temporales de ventas.
- Segmentación por **cliente**, **vendedor**, y **producto**.
- Razones por las que no se concretaron ventas.
- Uso de tablas auxiliares creadas a partir del dataset original:
  - `Cliente`
  - `Vendedor`
  - `Calendario`
  - `Medidas Calculadas`

![image](https://github.com/user-attachments/assets/b2e8ebb2-3de7-4d9e-af0f-8fbadf83a0f0)


> ⚠️ El archivo `.pbix` se incluye en este repositorio para su revisión.

---

## 🧠 Predicción de Ventas (Streamlit)

Se desarrollaron dos modelos:

- ✅ Modelo sin balanceo de clases.
- ✅ Modelo balanceado con **SMOTE**.

Ambos modelos fueron evaluados y comparados a través de métricas clave (accuracy, AUC, reporte de clasificación) y visualización de la **importancia de variables**.

Además, la aplicación en Streamlit permite:

- Comparar modelos lado a lado.
- Subir nuevos datos para predecir ventas en tiempo real.
- Visualizar probabilidades de éxito para cada caso.

---

## 📁 Estructura del Proyecto

📁 tu-proyecto/ ├── app.py ├── modelo_con_smote.pkl ├── modelo_sin_smote.pkl ├── X_test_con_smote.pkl ├── y_test_con_smote.pkl ├── X_test_sin_smote.pkl ├── y_test_sin_smote.pkl ├── importancia_modelo_con_smote.csv ├── importancia_modelo_sin_smote.csv ├── dashboard_ventas_AGSM.pbix ├── requirements.txt └── README.md


---

## 🛠️ Instalación y Ejecución Local

1. Cloná el repositorio:

```bash
git clone (https://github.com/PedroNicolasGodoy/ChallengeAGSM.git)
cd tu-repo
```
2. Creá un entorno virtual::
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
3. Instalá las dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecutá el tablero en tu navegador:
```bash
streamlit run app.py
```
Requerimientos
```bash
streamlit
pandas
matplotlib
seaborn
scikit-learn
imbalanced-learn
joblib
openpyxl
```
✨ Resultado Esperado
📈 Visualización clara de datos históricos de ventas (Power BI).

🔍 Predicción efectiva y comparación de modelos (Streamlit).

📁 Aplicación modular y portable para futuras implementaciones.

📬 Contacto
Creado por PedroGodoy

📧 pedronicogodoy@example.com

💼 https://www.linkedin.com/in/pedro-nicolas-godoy/

