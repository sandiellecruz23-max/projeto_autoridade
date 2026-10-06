"""Gera pautas e fichas de produção; não gera mídia nem publica."""
import argparse
import csv
from datetime import date, timedelta
from pathlib import Path

PAUTAS = [
 ("O que acontece antes de sair para treinar", "Preparação e saída registradas"),
 ("Um detalhe do treino", "Cenas reais do treino e contexto"),
 ("Recortes da semana", "Fotos e contexto de cada registro"),
 ("Entre uma atividade e outra", "Bastidores e relato da sequência"),
 ("Um treino pelas pequenas cenas", "Equipamento, execução e fechamento"),
 ("Vida além do treino", "Fotos da rotina escolhidas por Sandi"),
]
def gerar(inicio, semanas, destino):
    destino.mkdir(parents=True, exist_ok=True)
    linhas = []
    dia = inicio
    indice = 0
    while len(linhas) < semanas * 3:
        if dia.weekday() in (2, 4, 6):
            pauta, material = PAUTAS[indice % len(PAUTAS)]
            formato = "Fotos/carrossel" if dia.weekday() == 6 else "Reel"
            codigo = dia.isoformat()
            linhas.append(["Ideia", codigo, formato, pauta, material])
            ficha = f"""# {codigo} — {pauta}
Perfil: @sandielle_cruz
Formato: {formato}
Status: Ideia

## Material necessário
{material}. Confirmar o contexto antes de escrever.

## Ficha de produção
- Relato do que aconteceu:
- Arquivos disponíveis (guardar mídia fora do repositório público):
- Fatos confirmados:
- Conceito e abertura:
- Sequência de cenas/fotos:
- Textos na tela:
- Legenda:
- Capa:
- Pendências:
- Aprovação:

## Orientação
Rotina real; sem motivacional forçado. Não inventar horário, distância,
cronologia, sentimentos ou treino concluído. Usar road to Ironman sobre
cena em movimento quando adequado. Textos curtos, cortes simples e cores
naturais. Referência de fonte precisa ser inspecionada.
Esta ficha é uma pauta, não uma publicação pronta.
"""
            (destino / f"{codigo}.md").write_text(ficha, encoding="utf-8")
            indice += 1
        dia += timedelta(days=1)
    with (destino / "calendario.csv").open("w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Status", "Data", "Formato", "Pauta", "Material necessário"])
        escritor.writerows(linhas)
    return linhas

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inicio", default=date.today().isoformat())
    parser.add_argument("--semanas", type=int, default=1)
    parser.add_argument("--saida", default="saida")
    args = parser.parse_args()
    if not 1 <= args.semanas <= 52:
        parser.error("--semanas deve estar entre 1 e 52")
    linhas = gerar(date.fromisoformat(args.inicio), args.semanas, Path(args.saida))
    print(f"{len(linhas)} pautas geradas em {args.saida}")
