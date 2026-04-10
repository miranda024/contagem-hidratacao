import json
import os

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

    def definir_perfil(self, peso, pratica_esporte):
        # Lógica de cálculo da meta diária: 50ml/kg para esportistas, 35ml/kg para sedentários
        if peso <= 0:
            raise ValueError("O peso deve ser maior que zero.")
        
        if pratica_esporte:
            self.dados["meta"] = int(peso * 50) 
        else:
            self.dados["meta"] = int(peso * 35) 
            
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
            return f"Registro adicionado: Você bebeu {quantidade_ml}ml. Total: {self.dados['total_ml']}ml. Faltam {falta}ml para a meta!"
        else:
            return f"Registro adicionado: Você bebeu {quantidade_ml}ml. Total: {self.dados['total_ml']}ml. Parabéns, você atingiu a meta diária!"

    def obter_total(self):
        return self.dados["total_ml"]

    def obter_meta(self):
        return self.dados["meta"]

if __name__ == "__main__":
    rastreador = RastreadorAgua()
    
    # Se a meta for 0, significa que é a primeira vez rodando!
    if rastreador.obter_meta() == 0:
        print("[INFO] Olá! Parece que é a sua primeira vez aqui.")
        print("[INFO] Vamos personalizar a sua meta ideal de hidratação!")
        try:
            peso = float(input("Qual é o seu peso em kg? (ex: 70): "))
            esporte = input("Você pratica atividades físicas regularmente? (s/n): ").strip().lower()
            pratica_esporte = (esporte == 's')
            
            rastreador.definir_perfil(peso, pratica_esporte)
            print(f"[SUCESSO] Perfil criado! Sua meta diária foi definida para {rastreador.obter_meta()}ml.\n")
        except ValueError:
            print("[ERRO] Por favor, digite um peso válido.")
            exit() # Sai do programa se a pessoa digitar letras no peso

    print("--- RASTREADOR DE HIDRATAÇÃO CLI ---")
    print(f"Meta diária calculada: {rastreador.obter_meta()}ml")
    print(f"Total consumido hoje: {rastreador.obter_total()}ml")
    print("------------------------------------")
    
    try:
        entrada = input("Quantos ml você bebeu agora? (Digite apenas números): ")
        qtd = int(entrada)
        mensagem = rastreador.adicionar_agua(qtd)
        print(mensagem)
    except ValueError as e:
        if "maior que zero" in str(e):
            print(f"[ERRO] {e}")
        else:
            print("[ERRO] Por favor, digite um número inteiro válido (ex: 250).")