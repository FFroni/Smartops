import streamlit as st
import time

# Configurazioni di pagina - DEVE essere la prima istruzione Streamlit
st.set_page_config(
    page_title="Manual Generator",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aggiungi CSS personalizzato per un design moderno ed elegante
st.markdown(
    """
    <style>
    /* Stile globale e font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Contenitore principale */
    .main-container {
        background: linear-gradient(to bottom right, #ffffff, #f8f9fa);
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        margin: 1rem 0;
    }
    
    /* Titolo principale */
    .main-header {
        color: #2E7D32;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
        font-size: 2.4rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Area di upload */
    .upload-container {
        border: 2px dashed #4CAF50;
        background-color: rgba(76, 175, 80, 0.05);
        padding: 2rem;
        border-radius: 12px;
        transition: all 0.3s ease;
        text-align: center;
        margin: 1.5rem 0;
    }
    
    .upload-container:hover {
        background-color: rgba(76, 175, 80, 0.1);
        transform: translateY(-2px);
    }
    
    /* Bottoni */
    .stButton button {
        background-color: #2E7D32 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 500 !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton button:hover {
        background-color: #1B5E20 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Animazione per il messaggio di successo */
    .success-message {
        background-color: rgba(76, 175, 80, 0.1);
        color: #2E7D32;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2E7D32;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Stile per la sidebar */
    .sidebar-content {
        background-color: rgba(46, 125, 50, 0.05);
        padding: 1.2rem;
        border-radius: 10px;
        margin-top: 1rem;
        border-left: 4px solid #2E7D32;
    }
    
    /* Stile per la barra di progresso */
    .stProgress > div > div {
        background-color: #4CAF50 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #666;
        font-size: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar migliorata
with st.sidebar:
    st.markdown("### 📌 Informazioni")
    st.markdown(
        """
        <div class='sidebar-content'>
        <h4>Come funziona</h4>
        <ol>
            <li>Carica il tuo file PDF</li>
            <li>Attendi l'elaborazione</li>
            <li>Scarica il manuale generato</li>
        </ol>
        <p><strong>Nota:</strong> Il processo potrebbe richiedere alcuni minuti in base alla dimensione del file.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class='sidebar-content' style='margin-top: 20px;'>
        <h4>Assistenza</h4>
        <p>Per problemi o domande, contatta il nostro team di supporto all'indirizzo <strong>support@example.com</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Contenitore principale
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Header con animazione
st.markdown("<h1 class='main-header'>📘 Manual Generator</h1>", unsafe_allow_html=True)

# Descrizione
st.markdown(
    """
    <p style='text-align: center; margin-bottom: 2rem; color: #555; font-size: 1.1rem;'>
    Trasforma i tuoi documenti PDF in manuali professionali con un solo click.
    </p>
    """,
    unsafe_allow_html=True
)

# Area di upload migliorata
st.markdown("<div class='upload-container'>", unsafe_allow_html=True)
uploaded_pdf = st.file_uploader("Seleziona o trascina qui il tuo file PDF", type="pdf")
st.markdown("Accettiamo file PDF fino a 10MB", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Processo di generazione
if uploaded_pdf is not None:
    st.markdown(
        "<div class='success-message'>File caricato con successo!</div>",
        unsafe_allow_html=True
    )
    
    # Opzioni di configurazione (aggiunta)
    with st.expander("Opzioni di generazione", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            format_option = st.selectbox(
                "Formato di output",
                ["PDF Standard", "PDF Interattivo", "PDF con indice"]
            )
        with col2:
            style_option = st.selectbox(
                "Stile grafico",
                ["Moderno", "Classico", "Minimalista", "Aziendale"]
            )
    
    st.markdown("<div style='margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    # Pulsante di generazione
    if st.button("Genera Manuale", key="generate_btn"):
        # Mostra una barra di avanzamento per simulare il processo
        progress_text = "Elaborazione del documento in corso..."
        st.text(progress_text)
        
        progress_bar = st.progress(0)
        
        # Simulazione delle fasi del processo
        stages = [
            "Analisi del documento...",
            "Estrazione del contenuto...",
            "Formattazione del manuale...",
            "Generazione dell'indice...",
            "Finalizzazione..."
        ]
        
        stage_weight = 100 / len(stages)
        
        for i, stage in enumerate(stages):
            for percent in range(int(stage_weight)):
                progress_value = min(int(i * stage_weight + percent), 100)
                progress_bar.progress(progress_value)
                time.sleep(0.03)
            st.text(stage)
        
        # Completamento
        progress_bar.progress(100)
        st.markdown(
            "<div class='success-message' style='margin-top: 1rem;'>"
            "<h3>✅ Manuale generato con successo!</h3>"
            "<p>Il tuo documento è pronto per il download</p>"
            "</div>",
            unsafe_allow_html=True
        )
        
        # Legge il file PDF predeterminato (sostituisci 'mainpdf.pdf' con il percorso del tuo file)
        try:
            with open("mainpdf.pdf", "rb") as file:
                pdf_data = file.read()
                
            # Area di download migliorata
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    label="Scarica il manuale generato",
                    data=pdf_data,
                    file_name="manuale_generato.pdf",
                    mime="application/pdf",
                    key="download_btn"
                )
        except:
            st.error("Impossibile caricare il file. Assicurati che 'mainpdf.pdf' esista nella directory dell'applicazione.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class='footer'>
        <p>© 2025 Manual Generator | Tutti i diritti riservati</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)