import streamlit as st
import pandas as pd

# --------------------------------------------------
# App-oppsett
# --------------------------------------------------
st.set_page_config(
    page_title="🏆 Modell Highscore",
    page_icon="🏆",
    layout="centered",
)

st.title("🏆 Modell-Highscore")
st.caption("Rangert etter forklaringsgrad (R²)")

# --------------------------------------------------
# Last inn data
# --------------------------------------------------
@st.cache_data
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
            <p style="margin:0;">R² = <b>{row['Resultat_(R2)']:.4f}</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Full liste
# --------------------------------------------------
st.subheader("📋 Full highscore")

st.dataframe(
    df[["Plass", "Navn", "Resultat_(R2)"]],
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("ℹ️ Høgare R² betyr betre modell")
