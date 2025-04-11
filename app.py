import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
import joblib

# Título
st.title("🧠 Tablero de Comparación y Predicción de Modelos de Venta")

# Cargar modelos y datos
modelo1 = joblib.load("modelo_sin_smote.pkl")
modelo2 = joblib.load("modelo_con_smote.pkl")
X_test1 = joblib.load("X_test_sin_smote.pkl")
y_test1 = joblib.load("y_test_sin_smote.pkl")
X_test2 = joblib.load("X_test_con_smote.pkl")
y_test2 = joblib.load("y_test_con_smote.pkl")
fi1 = pd.read_csv("importancia_modelo_sin_smote.csv")
fi2 = pd.read_csv("importancia_modelo_con_smote.csv")

# Evaluación
st.header("🔍 Métricas de Evaluación")

def evaluar_modelo(nombre, modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    y_proba = modelo.predict_proba(X_test)[:, 1]
    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    st.markdown(f"### {nombre}")
    st.write(f"**Accuracy:** {acc:.4f}")
    st.write(f"**ROC AUC:** {auc:.4f}")
    st.text(classification_report(y_test, y_pred))

col1, col2 = st.columns(2)

with col1:
    evaluar_modelo("Modelo 1 - Sin SMOTE", modelo1, X_test1, y_test1)

with col2:
    evaluar_modelo("Modelo 2 - Con SMOTE", modelo2, X_test2, y_test2)

# Comparación de importancia de variables
st.header("📊 Comparación de Importancia de Variables")

top_n = st.slider("Top N variables a mostrar:", 5, 30, 15)

fi1_top = fi1.head(top_n).copy()
fi1_top["Modelo"] = "Sin SMOTE"
fi2_top = fi2.head(top_n).copy()
fi2_top["Modelo"] = "Con SMOTE"
fi_merged = pd.concat([fi1_top, fi2_top])

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=fi_merged, y="Feature", x="Importance", hue="Modelo", ax=ax)
plt.title("Importancia de Variables - Comparación")
plt.tight_layout()
st.pyplot(fig)

# Predicción de nuevos datos
st.header("📁 Predecir Nuevos Datos")

opcion = st.radio("¿Cómo querés ingresar los datos?", ["Subir archivo Excel", "Ingresar manualmente"])

if opcion == "Subir archivo Excel":
    archivo = st.file_uploader("Subí tu archivo Excel", type=["xlsx"])
    if archivo:
        try:
            df_nuevo = pd.read_excel(archivo)
            st.write("Vista previa:")
            st.dataframe(df_nuevo.head())
            pred = modelo2.predict(df_nuevo)
            proba = modelo2.predict_proba(df_nuevo)[:, 1]
            df_nuevo["Predicción"] = pred
            df_nuevo["Probabilidad de Venta"] = proba
            st.success("✅ Predicciones generadas con éxito.")
            st.dataframe(df_nuevo)
        except Exception as e:
            st.error(f"❌ Error al predecir: {e}")

elif opcion == "Ingresar manualmente":
    st.info("Completá los datos para una predicción manual:")

    # Acá podés cambiar los campos según tu modelo
    campos = X_test2.columns if isinstance(X_test2, pd.DataFrame) else [f"var{i}" for i in range(10)]
    valores = {}

    for campo in campos:
        valores[campo] = st.text_input(f"{campo}", value="0")

    if st.button("Predecir"):
        try:
            df_manual = pd.DataFrame([valores])
            df_manual = df_manual.astype(float)  # casteamos a float
            pred = modelo2.predict(df_manual)[0]
            proba = modelo2.predict_proba(df_manual)[0, 1]
            st.success(f"✅ Predicción: {pred} | Probabilidad de venta: {proba:.2f}")
        except Exception as e:
            st.error(f"❌ Error al predecir: {e}")

