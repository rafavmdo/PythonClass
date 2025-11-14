# placar_raid.py
import json

ARQUIVO_RANKING = 'ranking_raid.json' 
MAX_SCORES = 5

def carregar_scores():
    """Tenta carregar os scores do arquivo. Se não existir, retorna uma lista padrão."""
    try:
        with open(ARQUIVO_RANKING, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [{'iniciais': 'AAA', 'pontos': 0} for _ in range(MAX_SCORES)]

def salvar_scores(scores):
    """Salva a lista de scores no arquivo."""
    with open(ARQUIVO_RANKING, 'w') as f:
        json.dump(scores, f, indent=4)

def adicionar_score(iniciais, pontos):
    """Adiciona um novo score à lista, ordena e mantém apenas os 5 melhores."""
    scores = carregar_scores()
    scores.append({'iniciais': iniciais, 'pontos': pontos})
    scores_ordenados = sorted(scores, key=lambda item: item['pontos'], reverse=True)
    scores_finais = scores_ordenados[:MAX_SCORES]
    salvar_scores(scores_finais)
    return scores_finais