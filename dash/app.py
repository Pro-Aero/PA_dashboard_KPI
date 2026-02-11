import streamlit as st

st.set_page_config(
    page_title="Login",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    /* Container central (a "barra" cinza) */
    .highlight-box {
        max-width: 520px;
        margin: auto;
        margin-top: 18vh;
        padding: 2.2rem 2rem;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            rgba(22,27,34,0.95),
            rgba(30,36,45,0.95)
        );
        box-shadow: 0 20px 60px rgba(0,0,0,0.6);
        text-align: center;
    }

    .highlight-title {
        font-size: 1.9rem;
        font-weight: 800;
        letter-spacing: 0.18em;
        color: #ffffff;
        margin-bottom: 0.6rem;
    }

    .highlight-subtitle {
        font-size: 1rem;
        color: #9ca3af;
        margin-bottom: 1.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def hide_sidebar():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def login():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        hide_sidebar()

        st.markdown(
            """
            <style>
            .login-box {
                max-width: 420px;
                margin: auto;
                margin-top: 35vh;
                text-align: center;
            }

            .login-title {
                font-size: 2.2rem;
                font-weight: 800;
                letter-spacing: 0.2em;
                color: white;
                margin-bottom: 2rem;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="login-box">', unsafe_allow_html=True)

        st.markdown(
            '<div class="login-title">ACESSO RESTRITO</div>',
            unsafe_allow_html=True
        )
        
        password = st.text_input(
            "Senha",
            type="password",
            label_visibility="collapsed"
        )

        if st.button("Entrar", use_container_width=True):
            if password == st.secrets.get("APP_PASSWORD"):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Senha inválida")

        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

login()

st.title("Bem-vindo")
st.write("Selecione uma página no menu lateral.")
