import base64
import json
import os
import matplotlib.pyplot as plt
import streamlit as st

# --- INICIALIZAÇÃO DA SESSÃO ---
if "senha_admin" not in st.session_state:
    st.session_state.senha_admin = "admin123"

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# Ficheiro para persistência de dados
ARQUIVO_BANCO = "biblioteca.json"


# --- FUNÇÕES DE PERSISTÊNCIA DE DADOS ---
def carregar_dados():
    if os.path.exists(ARQUIVO_BANCO):
        try:
            with open(ARQUIVO_BANCO, "r", encoding="utf-8") as f:
                livros = json.load(f)
                # Converte a capa de string Base64 para bytes de imagem
                for livro in livros:
                    if livro.get("capa"):
                        livro["capa"] = base64.b64decode(livro["capa"])
                    # Garante compatibilidade caso existam registos sem o campo status
                    if "status" not in livro:
                        livro["status"] = "Disponível"
                return livros
        except Exception:
            return []
    return []


def salvar_dados(biblioteca):
    biblioteca_para_salvar = []
    for livro in biblioteca:
        livro_copia = livro.copy()
        # Converte bytes de imagem para string Base64 para guardar no JSON
        if livro_copia.get("capa") and isinstance(livro_copia["capa"], bytes):
            livro_copia["capa"] = base64.b64encode(livro_copia["capa"]).decode("utf-8")
        biblioteca_para_salvar.append(livro_copia)

    with open(ARQUIVO_BANCO, "w", encoding="utf-8") as f:
        json.dump(biblioteca_para_salvar, f, ensure_ascii=False, indent=4)


# Configuração da página
st.set_page_config(
    page_title="Gestão de Biblioteca", page_icon="📚", layout="centered"
)

st.markdown(
    """
    <style>
    /* Imagem de fundo */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=1920");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Camada mais escura por cima da imagem */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.78);
        z-index: -1;
    }

    /* Aplica sombra preta intensa a todos os títulos e textos */
    h1, h2, h3, p, label, .stMarkdown {
        color: #ffffff !important;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.95), 0px 0px 10px rgba(0, 0, 0, 0.9) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título Principal
st.title("📚 Sistema de Gestão de Biblioteca")

# Inicializa a biblioteca carregando os dados do ficheiro JSON
if "biblioteca" not in st.session_state:
    st.session_state.biblioteca = carregar_dados()

# --- LOGIN DO ADMINISTRADOR ---
st.sidebar.subheader("🔐 Acesso Restrito")

if not st.session_state.autenticado:
    senha_input = st.sidebar.text_input("Palavra-passe Admin:", type="password")
    if st.sidebar.button("Entrar"):
        if senha_input == st.session_state.senha_admin:
            st.session_state.autenticado = True
            st.sidebar.success("Acesso concedido!")
            st.rerun()
        else:
            st.sidebar.error("Palavra-passe incorreta!")
else:
    st.sidebar.success("Sessão ativa (Admin)")

    with st.sidebar.expander("🔑 Alterar Palavra-passe"):
        nova_senha = st.text_input("Nova palavra-passe:", type="password")
        if st.button("Guardar"):
            if nova_senha.strip():
                st.session_state.senha_admin = nova_senha
                st.success("Palavra-passe alterada!")
            else:
                st.warning("A palavra-passe não pode estar vazia.")

    if st.sidebar.button("Sair"):
        st.session_state.autenticado = False
        st.rerun()

st.sidebar.divider()

# --- MENU LATERAL (Navegação) ---
st.sidebar.header("Menu de Opções")
opcao = st.sidebar.radio(
    "Escolha uma ação:",
    [
        "Cadastrar Livro",
        "Listar Livros",
        "Gráfico por Gênero",
        "Remover / Editar",
    ],
)

# --- OPÇÃO 1: CADASTRAR LIVRO ---
if opcao == "Cadastrar Livro":
    st.header("➕ Cadastrar Novo Livro")

    if not st.session_state.autenticado:
        st.warning("⚠️ **Acesso Restrito:** Apenas o administrador pode cadastrar novos livros. Por favor, faça login na barra lateral.")
    else:
        with st.form(key="form_cadastrar", clear_on_submit=True):
            titulo = st.text_input("Título do Livro:")
            autor = st.text_input("Autor:")
            genero = st.text_input("Gênero:")
            quantidade = st.number_input(
                "Quantidade:", min_value=1, step=1, value=1
            )
            status = st.selectbox("Status de Disponibilidade:", ["Disponível", "Emprestado"])

            # Campo para upload da imagem da capa do livro
            capa_arquivo = st.file_uploader(
                "Capa do Livro (Imagem):", type=["png", "jpg", "jpeg"]
            )

            submeter = st.form_submit_button("Cadastrar")

        if submeter:
            if titulo.strip() and autor.strip() and genero.strip():
                # Lê os bytes da imagem enviada (se existir)
                capa_data = (
                    capa_arquivo.read() if capa_arquivo is not None else None
                )

                st.session_state.biblioteca.append({
                    "titulo": titulo.strip().title(),
                    "autor": autor.strip().title(),
                    "genero": genero.strip().title(),
                    "quantidade": int(quantidade),
                    "status": status,
                    "capa": capa_data,
                })

                # Guarda as alterações no ficheiro JSON
                salvar_dados(st.session_state.biblioteca)

                st.success(
                    f"Livro '{titulo.strip().title()}' cadastrado com sucesso!"
                )
            else:
                st.warning("Por favor, preencha todos os campos do formulário!")


# --- OPÇÃO 2: LISTAR LIVROS ---
elif opcao == "Listar Livros":
    st.header("📚 Livros Cadastrados")

    if not st.session_state.biblioteca:
        st.info("Nenhum livro cadastrado até o momento.")
    else:
        # Ordenação alfabética automática pelo título
        livros_ordenados = sorted(
            st.session_state.biblioteca, key=lambda item: item["titulo"].lower()
        )

        st.subheader("Clique no livro para ver a capa e os detalhes:")

        for livro in livros_ordenados:
            status_livro = livro.get("status", "Disponível")
            icone_status = "🟢" if status_livro == "Disponível" else "🔴"

            # Exibe o status direto no cabeçalho
            with st.expander(f"📖 {livro['titulo']} — {livro['autor']} [{icone_status} {status_livro}]"):
                col1, col2 = st.columns([1, 2])

                with col1:
                    if livro.get("capa"):
                        st.image(
                            livro["capa"],
                            caption=f"Capa: {livro['titulo']}",
                            use_container_width="stretch",
                        )
                    else:
                        st.caption(
                            "📷 Nenhuma capa cadastrada para este livro."
                        )

                with col2:
                    st.write(f"**Gênero:** {livro['genero']}")
                    st.write(f"**Quantidade disponível:** {livro['quantidade']}")
                    st.write(f"**Status:** {icone_status} **{status_livro}**")


# --- OPÇÃO 3: GERAR GRÁFICO ---
elif opcao == "Gráfico por Gênero":
    st.header("📊 Distribuição de Livros por Gênero")

    if not st.session_state.biblioteca:
        st.warning("Não há livros cadastrados para gerar o gráfico.")
    else:
        contagem_generos = {}
        for livro in st.session_state.biblioteca:
            g = livro["genero"]
            contagem_generos[g] = contagem_generos.get(g, 0) + livro["quantidade"]

        generos = list(contagem_generos.keys())
        quantidades = list(contagem_generos.values())

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(generos, quantidades, color="skyblue", edgecolor="navy")
        ax.set_xlabel("Gênero")
        ax.set_ylabel("Quantidade de Livros")
        ax.set_title("Quantidade de Livros por Gênero")
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        st.pyplot(fig)


# --- OPÇÃO 4: REMOVER / EDITAR ---
elif opcao == "Remover / Editar":
    st.header("⚙️ Gerenciar Acervo")

    if not st.session_state.autenticado:
        st.warning("⚠️ **Acesso Restrito:** Apenas o administrador pode remover ou editar livros. Por favor, faça login na barra lateral.")
    else:
        if not st.session_state.biblioteca:
            st.info("Nenhum livro disponível para gerenciar.")
        else:
            titulos = [l["titulo"] for l in st.session_state.biblioteca]
            livro_selecionado = st.selectbox("Selecione um livro:", titulos)

            # Localiza o livro selecionado
            livro_obj = next((l for l in st.session_state.biblioteca if l["titulo"] == livro_selecionado), None)

            if livro_obj:
                status_atual = livro_obj.get("status", "Disponível")
                st.write(f"Status atual: **{status_atual}**")

                novo_status = st.radio("Alterar Status:", ["Disponível", "Emprestado"], index=0 if status_atual == "Disponível" else 1)

                col_btn1, col_btn2 = st.columns(2)

                with col_btn1:
                    if st.button("🔄 Atualizar Status"):
                        livro_obj["status"] = novo_status
                        salvar_dados(st.session_state.biblioteca)
                        st.success(f"Status de '{livro_selecionado}' alterado para {novo_status}!")
                        st.rerun()

                with col_btn2:
                    if st.button("🗑️ Remover Livro"):
                        st.session_state.biblioteca = [
                            l
                            for l in st.session_state.biblioteca
                            if l["titulo"] != livro_selecionado
                        ]
                        # Guarda a remoção no ficheiro JSON
                        salvar_dados(st.session_state.biblioteca)
                        st.success(f"Livro '{livro_selecionado}' removido!")
                        st.rerun()