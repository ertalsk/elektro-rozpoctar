import streamlit as st
import time

# Nastavenie vzhľadu stránky
st.set_page_config(page_title="AI Elektro Rozpočtár", page_icon="⚡", layout="wide")

st.title("⚡ AI Kontrola a Naceňovanie Elektroinštalácií")
st.markdown("Prototyp aplikácie na automatickú kontrolu výkazov výmer a PDF výkresov.")

# Rozdelenie obrazovky
col1, col2 = st.columns(2)

with col1:
    st.header("1. Vstupné dáta")
    excel_file = st.file_uploader("Nahrať slepý rozpočet z Cenkrosu (Excel)", type=["xlsx", "xls"])
    pdf_file = st.file_uploader("Nahrať výkres - Situácia (PDF, JPG, PNG)", type=["pdf", "png", "jpg"])

with col2:
    st.header("2. Analýza a Výsledky")
    if st.button("Spustiť AI kontrolu a naceniť", type="primary"):
        if excel_file and pdf_file:
            # Tu sa simuluje práca AI
            with st.spinner("Párujem položky s cenníkom Hagard:HAL..."):
                time.sleep(2)
                st.success("✅ Cenník úspešne spárovaný! (Nájdených 28/28 položiek)")
            
            with st.spinner("AI skenuje výkres a hľadá elektro značky..."):
                time.sleep(3)
                st.info("🔍 Analýza výkresu dokončená.")
                
            st.markdown("### 🚨 Zistené nezrovnalosti v projekte:")
            st.error("**❌ CHYBA - Chýbajúca práca:** V Exceli je kábel AYKY 3x240+120, ale chýba položka na ukončenie PEN vodiča 120mm2. (Položka 14 rieši len 240mm2).")
            st.warning("**⚠️ UPOZORNENIE - Káble vs. Výkop:** Dĺžka kábla (130m) nesedí s dĺžkou ryhy (60m). Overte uloženie 2 káblov do jednej ryhy.")
            st.success("**🟢 KUSY SÚHLASIA:** Počet poistkových vložiek (18 ks) matematicky súhlasí s počtom montáží.")
            st.success("**🟢 PDF KONTROLA OK:** Značka 'Skriňa SR4' nájdená na výkrese (1 ks) súhlasí s počtom v Exceli (1 ks).")
            
            st.markdown("### 💾 Export")
            st.button("📥 Stiahnuť nacenený rozpočet pre klienta (Excel)")
        else:
            st.warning("👈 Prosím, najprv nahrajte Excel aj Výkres (PDF) vľavej časti obrazovky.")
