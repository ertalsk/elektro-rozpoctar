import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Elektro Rozpočtár", page_icon="⚡", layout="wide")

st.title("⚡ AI Kontrola a Naceňovanie Elektroinštalácií (ŽIVÁ VERZIA)")
st.markdown("Teraz aplikácia reálne číta dáta z vášho Excelu.")

col1, col2 = st.columns(2)

with col1:
    st.header("1. Vstupné dáta")
    excel_file = st.file_uploader("Nahrať slepý rozpočet z Cenkrosu (Excel)", type=["xlsx", "xls"])
    pdf_file = st.file_uploader("Nahrať výkres (PDF, JPG, PNG)", type=["pdf", "png", "jpg"])

with col2:
    st.header("2. Analýza a Výsledky")
    if st.button("Spustiť kontrolu Excelu", type="primary"):
        if excel_file is not None:
            try:
                # REÁLNE NAČÍTANIE EXCELU
                df = pd.read_excel(excel_file)
                
                st.success(f"✅ Súbor '{excel_file.name}' bol úspešne prečítaný!")
                st.write(f"📊 **Počet nájdených riadkov v tabuľke:** {len(df)}")
                
                # Zobrazenie prvých 10 riadkov z vášho reálneho Excelu
                st.markdown("### Ukážka prečítaných dát:")
                st.dataframe(df.head(10))
                
                # Jednoduchá dynamická analýza
                st.markdown("### 🔍 Rýchly audit obsahu:")
                
                # Spojíme všetky texty v tabuľke do jedného, aby sme v nich mohli hľadať
                vsetok_text = df.astype(str).to_string().lower()
                
                if "kábel" in vsetok_text or "kabel" in vsetok_text:
                    st.info("💡 Aplikácia detekovala v rozpočte káble.")
                if "zásuvka" in vsetok_text or "zasuvka" in vsetok_text:
                    st.info("💡 Aplikácia detekovala v rozpočte zásuvky.")
                if "cenkros" in vsetok_text:
                    st.info("💡 Vyzerá to ako štandardný export z Cenkrosu.")
                    
            except Exception as e:
                st.error(f"Nastala chyba pri čítaní Excelu: {e}")
                st.warning("Skúste nahrať štandardný .xlsx súbor.")
                
        else:
            st.warning("👈 Prosím, nahrajte najprv Excel súbor vľavo.")
            
        if pdf_file is not None:
            st.info(f"📁 PDF súbor '{pdf_file.name}' zaevidovaný. (Umelá inteligencia pre čítanie výkresov vyžaduje zložitejšie nastavenie servera, zatiaľ testujeme len Excel).")
