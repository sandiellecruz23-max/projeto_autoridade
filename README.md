# Projeto Autoridade — @sandielle_cruz

Base editorial: três posts semanais, dois Reels e um post de fotos, às quartas, sextas e domingos. Stories conforme os registros disponíveis.

## Primeira automação
Gera um calendário CSV e fichas de produção em Markdown. Não gera legendas por IA, não edita vídeos e não publica no Instagram. As pautas são propostas: só usar quando os materiais reais sustentarem o conteúdo.

## Como usar
Abra Actions → Calendário semanal → Run workflow. O início é opcional (AAAA-MM-DD); semanas entre 1 e 52. Ao finalizar, baixe o artefato calendario-editorial. A rotina também executa às segundas, por volta de 07h17 de Brasília; GitHub pode atrasar execuções. Em repositórios públicos, agendamentos podem ser desativados após 60 dias sem atividade.

Localmente:
```bash
python3 scripts/gerar_calendario.py --inicio 2026-10-07 --semanas 4
```

## Regras
Rotina real, comentários concretos e humor discreto. Road to Ironman é uma assinatura sobre cenas em movimento. Evitar motivacional forçado, suspense vazio e fatos inventados. Não inferir distância, horário, cronologia ou emoções pelas imagens. Textos curtos, cortes simples e cores naturais. Fonte histórica depende de referência inspecionada.

Status: ideia → material recebido → em produção → em revisão → aprovado → publicado. Publicação exige confirmação.

## Próximas etapas
Conectar armazenamento para os registros; acrescentar geração de roteiros e legendas por IA com histórico para evitar repetição; criar revisão; integrar edição e, posteriormente, publicação autorizada.

O repositório está público. Não colocar credenciais, mídia pessoal ou fichas preenchidas com informações privadas nele. A saída usa artefatos do Actions em vez de commits.
