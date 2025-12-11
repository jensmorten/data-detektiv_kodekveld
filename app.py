import streamlit as st
import pandas as pd

# --------------------------------------------------
# App-oppsett
# --------------------------------------------------
st.set_page_config(
    page_title="Data-detektiv kodekveld",
    page_icon="🏆",
    layout="centered",
)

st.title("🏆 Data-detektiv kodekveld")
st.caption("Rangert etter forklaringsgrad (R²)")

# --------------------------------------------------
# Last inn data
# --------------------------------------------------
def load_data():
    df = pd.read_csv("resultat.csv", sep=",")
    return df

df = load_data()

required_cols = {"Navn", "Resultat_R2"}
if not required_cols.issubset(df.columns):
    st.error(f"CSV må innehalde kolonnene: {required_cols}")
    st.stop()

# --------------------------------------------------
# Sorter og rydd
# --------------------------------------------------
df = (
    df.sort_values("Resultat_R2", ascending=False)
      .reset_index(drop=True)
)

beste_r2 = df.iloc[0]["Resultat_R2"]

if "beste_r2" not in st.session_state:
    st.session_state.beste_r2 = beste_r2
else:
    if beste_r2 > st.session_state.beste_r2:
        st.balloons()
        st.session_state.beste_r2 = beste_r2
df["Plass"] = df.index + 1

# --------------------------------------------------
# Topp 3 – highlight
# --------------------------------------------------
st.subheader("🥇 Topp 3")

for i in range(min(3, len(df))):
    row = df.iloc[i]

    medal = ["🥇", "🥈", "🥉"][i]

    st.markdown(
        f"""
        <div style="
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 8px;
            background-color: #f5f5f5;
            ">
            <h4 style="margin:0;">{medal} {row['Navn']}</h4>
            <p style="margin:0;">R² = <b>{row['Resultat_R2']:.4f}</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Full liste
# --------------------------------------------------
st.subheader("📋 Full highscore")

st.dataframe(
    df[["Plass", "Navn", "Resultat_R2"]],
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("ℹ️ Høyere R² betyr bedre modell")
# --------------------------------------------------
# Forklaring av R²
# --------------------------------------------------
st.divider()
st.subheader("ℹ️ Hva betyr R²?")

st.markdown(
"""
**Verdiområde**  
Den beste mulige R²-verdien er **1,0**, som betyr perfekt tilpasning der modellen
forklarer all variasjon i den avhengige variabelen.  

En R²-verdi på **0,0** betyr at modellen ikke forklarer noe av variasjonen – den
gjør det ikke bedre enn en konstant modell som alltid predikerer gjennomsnittet.  

R² kan også være **negativ** hvis modellen presterer dårligere enn en slik konstant modell.

**Tolkning**  
En R²-verdi på for eksempel **0,83** betyr at **83 % av variasjonen** i den
avhengige variabelen forklares av de uavhengige variablene i modellen.

**Beregning**
"""
)

st.latex(r"""
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
""")

st.latex(r"""
\text{der:} \\[0.3em]

SS_{\text{res}} = \text{summen av kvadrerte residualer}
\\
\\[0.6em]

SS_{\text{tot}} = \text{total varians}
\\
""")