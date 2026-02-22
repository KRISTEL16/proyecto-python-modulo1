import streamlit as st

st.set_page_config(page_title="Proyecto Analytics", layout="wide")
st.title("📊 Sistema Integral de Gestión Financiera")

# --- EJERCICIO 1: VARIABLES Y CONDICIONALES ---
st.header("1. Verificador de Presupuesto")
pre_total = st.number_input("Presupuesto Total:", min_value=0.0, key="e1_p")
gas_total = st.number_input("Gasto Total:", min_value=0.0, key="e1_g")

if st.button("Evaluar Presupuesto"):
    dif = pre_total - gas_total
    if gas_total <= pre_total:
        st.success(f"✅ Dentro del presupuesto. Saldo: ${dif:.2f}")
    else:
        st.error(f"❌ Excedido por: ${abs(dif):.2f}")

st.divider()

# --- EJERCICIO 2: LISTAS Y DICCIONARIOS ---
st.header("2. Registro de Actividades")
if 'actividades' not in st.session_state:
    st.session_state.actividades = []

col1, col2 = st.columns(2)
with col1:
    n_act = st.text_input("Nombre de Actividad:")
    t_act = st.selectbox("Tipo:", ["Gasto Fijo", "Inversión", "Variable"])
with col2:
    p_act = st.number_input("Presupuesto Sugerido:", min_value=0.0, key="e2_p")
    g_act = st.number_input("Gasto Real:", min_value=0.0, key="e2_g")

if st.button("Agregar Actividad"):
    st.session_state.actividades.append({
        "nombre": n_act, "tipo": t_act, "presupuesto": p_act, "gasto_real": g_act
    })
    st.success("¡Actividad registrada!")

if st.session_state.actividades:
    st.table(st.session_state.actividades)

st.divider()

# --- EJERCICIO 3: PROGRAMACIÓN FUNCIONAL (MAP/LAMBDA) ---
st.header("3. Retorno Esperado")
tasa = st.number_input("Tasa de Retorno (ej: 0.10):", value=0.10)
meses = st.number_input("Meses:", value=12)

def calcular_retorno(act, t, m):
    return act['presupuesto'] * t * m

if st.button("Calcular Retornos"):
    if st.session_state.actividades:
        resultados = list(map(lambda x: f"{x['nombre']}: ${calcular_retorno(x, tasa, meses):.2f}", st.session_state.actividades))
        for res in resultados:
            st.write(f"📈 {res}")
    else:
        st.warning("Agrega actividades en el ejercicio 2 primero.")

st.divider()

# --- EJERCICIO 4: POO (CLASES) ---
st.header("4. Análisis de Objetos")

class Actividad:
    def __init__(self, d):
        self.nombre = d['nombre']
        self.presupuesto = d['presupuesto']
        self.gasto = d['gasto_real']
    
    def esta_en_presupuesto(self):
        return self.gasto <= self.presupuesto

if st.button("Analizar con POO"):
    if st.session_state.actividades:
        for data in st.session_state.actividades:
            obj = Actividad(data)
            if obj.esta_en_presupuesto():
                st.success(f"✔️ {obj.nombre}: Cumple el presupuesto")
            else:
                st.warning(f"⚠️ {obj.nombre}: Excede el presupuesto")
    else:
        st.warning("No hay datos para analizar.")