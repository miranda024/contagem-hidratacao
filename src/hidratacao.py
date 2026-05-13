import json
import os
import requests
import streamlit as st

class RastreadorAgua:
    def __init__(self, arquivo='dados_agua.json'):
        self.arquivo = arquivo
        self.dados = self._carregar_dados()

    def _carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        return {"total_ml": 0, "registros": [], "meta": 0}

    def _salvar_dados(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.dados, f)

    # Parâmetro adicional_clima adicionado com valor padrão 0 para manter compatibilidade
    def definir_perfil(self, peso, pratica_esporte, adicional_clima=0):
        if peso <= 0:
            raise ValueError("O peso deve ser maior que zero.")
        
        if pratica_esporte:
            self.dados["meta"] = int(peso * 50) + adicional_clima
        else:
            self.dados["meta"] = int(peso * 35) + adicional_clima
            
        self._salvar_dados()

    def adicionar_agua(self, quantidade_ml):
        if quantidade_ml <= 0:
            raise ValueError("A quantidade de água deve ser maior que zero.")
        if self.dados["meta"] == 0:
            raise ValueError("A meta diária não foi configurada.")

        self.dados["registros"].append(quantidade_ml)
        self.dados["total_ml"] += quantidade_ml
        self._salvar_dados()

        falta = self.dados["meta"] - self.dados["total_ml"]
        if falta > 0:
            return f"Registro adicionado! Faltam {falta}ml para a meta."
        else:
            return "Parabéns, você atingiu a meta diária!"

    def obter_total(self):
        return self.dados["total_ml"]

    def obter_meta(self):
        return self.dados["meta"]

# --- INTEGRAÇÃO COM API PÚBLICA ---
def obter_temperatura(cidade, api_key):
    """Consome a API do OpenWeather para buscar a temperatura atual."""
    if not cidade or not api_key:
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            return dados['main']['temp']
        else:
            return None
    except Exception:
        return None

# --- INTERFACE WEB (GUI) ---
def main():
    st.set_page_config(page_title="Rastreador de Hidratação", page_icon="💧")
    st.title("💧 Rastreador de Hidratação Inteligente")

    rastreador = RastreadorAgua()

    # Menu lateral para configuração e API
    st.sidebar.header("⚙️ Configurações do Perfil")
    peso = st.sidebar.number_input("Seu peso (kg)", min_value=1.0, value=70.0, step=0.5)
    pratica_esporte = st.sidebar.checkbox("Pratico esportes regularmente")

    st.sidebar.markdown("---")
    st.sidebar.subheader("🌡️ Integração de Clima")
    st.sidebar.write("Dias quentes exigem mais água!")
    cidade = st.sidebar.text_input("Sua Cidade (ex: São Paulo)")
    api_key = st.sidebar.text_input("Chave API OpenWeather", type="password")

    if st.sidebar.button("Salvar e Calcular Meta"):
        adicional_clima = 0
        if cidade and api_key:
            temp = obter_temperatura(cidade, api_key)
            if temp is not None:
                st.sidebar.success(f"Temperatura atual: {temp}°C")
                if temp >= 30:
                    st.sidebar.warning("🔥 Está muito quente! Adicionando 500ml à sua meta.")
                    adicional_clima = 500
            else:
                st.sidebar.error("Erro ao buscar clima. Verifique a cidade ou a chave API.")
        
        rastreador.definir_perfil(peso, pratica_esporte, adicional_clima)
        st.success("Perfil atualizado com sucesso!")

    # Área Principal de Exibição
    meta = rastreador.obter_meta()
    total = rastreador.obter_total()

    if meta > 0:
        st.header(f"Sua Meta Diária: {meta}ml")
        st.subheader(f"Total Consumido: {total}ml")

        # Barra de progresso visual
        progresso = min(total / meta, 1.0)
        st.progress(progresso)

        if total >= meta:
            st.balloons()
            st.success("🎉 Parabéns! Você atingiu sua meta diária de hidratação!")
        else:
            st.info(f"Faltam {meta - total}ml para você atingir a meta.")

        st.markdown("---")
        st.subheader("Adicionar Consumo")
        qtd_agua = st.number_input("Quantidade de água (ml)", min_value=0, step=50, value=250)

        if st.button("Registrar Água 🥤"):
            if qtd_agua > 0:
                mensagem = rastreador.adicionar_agua(qtd_agua)
                st.success(mensagem)
                st.rerun() # Atualiza a tela imediatamente
            else:
                st.error("Digite um valor maior que zero.")
    else:
        st.info("👈 Por favor, configure seu perfil na barra lateral para começar!")

if __name__ == "__main__":
    main()