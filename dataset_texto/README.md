# Dataset de Textos — CardioIA (Projeto FIAP Fase 1, Capítulo 1)

## 1. Visão Geral

Este diretório contém o **corpus textual** do projeto **CardioIA**, desenvolvido como parte da **Fase 1 – Capítulo 1** da pós-graduação FIAP (PBL – Project Based Learning). O objetivo desta coleção é fornecer a base de dados textuais que alimentará os módulos de **Processamento de Linguagem Natural (NLP)** nas fases seguintes do projeto.

De acordo com o enunciado (ver [`enunciado/enunciado.txt`](../enunciado/enunciado.txt)), a **Parte 2 – Dados Textuais (NLP)** exige:

- No mínimo 2 arquivos `.txt` de fontes como SciELO, BVS, SUS ou Projeto Gutenberg;
- Disponibilização em subpasta do repositório GitHub;
- README explicando como os textos podem ser usados por NLP (análise de sentimentos, extração de sintomas, classificação de tópicos) e justificando sua importância na saúde.

Este dataset **supera** o mínimo exigido, reunindo **5 artigos científicos** de acesso aberto publicados pelo *International Journal of Cardiovascular Sciences* (IJCS), periódico indexado na **BVS (Biblioteca Virtual em Saúde)** e acessível via [ijcscardiol.org](https://ijcscardiol.org/), que atende aos critérios de fonte aceita pelo enunciado.

---

## 2. Arquivos do Dataset

### 2.1 `Childhood_Obesity.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Childhood Obesity and Systemic Arterial Hypertension in Children and Adolescents: A Cross-Sectional Study |
| **Autores** | Rafaella Farias da Franca Almeida, Lívia Menezes Escorel, Letícia Odete Guedes de Andrade Carvalho, et al. |
| **Instituições** | Centro Universitário de João Pessoa; FAMENE; Complexo Hospitalar Infantil Arlinda Marques; Instituto Dante Pazzanese de Cardiologia |
| **Periódico** | International Journal of Cardiovascular Sciences (IJCS) |
| **Referência** | Int J Cardiovasc Sci. 2026;39:e20240146 |
| **DOI** | https://doi.org/10.36660/ijcs.20240146 |
| **Fonte / Link** | https://ijcscardiol.org/article/childhood-obesity-and-systemic-arterial-hypertension-in-children-and-adolescents-a-cross-sectional-study/ |
| **Licença / Direitos** | Acesso aberto — IJCS publica sob licença Creative Commons (CC BY); consultar site do periódico para termos completos |
| **Recebido / Aceito** | Recebido: 07/08/2024 · Aceito: 26/03/2025 |
| **Palavras (~)** | 4 743 |

**Justificativa de seleção:**  
Este artigo de corte transversal investiga a relação entre **obesidade infantil** e **hipertensão arterial sistêmica (HAS)** em crianças e adolescentes. Embora o foco seja pediátrico, a HAS e seus fatores de risco (IMC, histórico familiar, sedentarismo) são variáveis centrais em toda a cardiologia clínica. Para NLP, o texto oferece vocabulário clínico padronizado (p.ex. *percentil de pressão arterial*, *circunferência abdominal*, *qui-quadrado*), útil para **extração de entidades clínicas** (NER), **classificação de fatores de risco** e **análise de correlação sintoma–diagnóstico**. A diversidade de autores e instituições brasileiras também contribui para enriquecer o corpus com terminologia do sistema de saúde nacional.

---

### 2.2 `Coronary_Artery_Disease.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Inflammatory and Atherogenic Markers as Predictors of Coronary Artery Disease in Patients with Suspected Coronary Artery Disease Undergoing Coronary Angiography |
| **Autores** | Veysi Can, Fuat Polat |
| **Instituições** | Van Regional Training and Research Hospital (Turquia); Istanbul Dr Siyami Ersek Thoracic and Cardiovascular Surgery Training and Research Hospital (Turquia) |
| **Periódico** | International Journal of Cardiovascular Sciences (IJCS) |
| **Referência** | Int J Cardiovasc Sci. 2026;39:e20250039 |
| **DOI** | https://doi.org/10.36660/ijcs.20250039 |
| **Fonte / Link** | https://ijcscardiol.org/article/inflammatory-and-atherogenic-markers-as-predictors-of-coronary-artery-disease-in-patients-with-suspected-coronary-artery-disease-undergoing-coronary-angiography/ |
| **Licença / Direitos** | Acesso aberto — IJCS publica sob licença Creative Commons (CC BY); consultar site do periódico para termos completos |
| **Recebido / Aceito** | Recebido: 25/02/2025 · Aceito: 21/07/2025 |
| **Palavras (~)** | 5 240 |

**Justificativa de seleção:**  
Este estudo retrospectivo com 767 pacientes avalia **marcadores inflamatórios** (PCR, NLR, PLR) como preditores da **doença arterial coronariana (DAC)**. É o texto mais rico em terminologia de **biomarcadores** e metodologia estatística (curva ROC, AUC, regressão multivariável), tornando-o ideal para treinar modelos de **extração de informação clínica** e **classificação de risco cardiovascular**. A dimensão internacional (autores turcos publicando no IJCS) diversifica o corpus linguisticamente. Para NLP, serve como referência para **reconhecimento de entidades biomédicas** (nomes de exames, proteínas, razões diagnósticas) e **análise de relações** entre marcadores e desfechos.

---

### 2.3 `Endocarditis.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Endocarditis – A 27-Year Epidemiological Analysis of Mortality in Brazil |
| **Autores** | Leticia da Costa Santana Silva, Luana Yasmim Fernández Avelaneda Castanheira, Maria Dalila Santos Salim, Ruy Felipe Melo Viegas, et al. |
| **Instituições** | Universidade de Taubaté, Taubaté, SP – Brazil |
| **Periódico** | International Journal of Cardiovascular Sciences (IJCS) |
| **Referência** | Int J Cardiovasc Sci. 2026;39:e20250124 |
| **DOI** | https://doi.org/10.36660/ijcs.20250124 |
| **Fonte / Link** | https://ijcscardiol.org/article/endocarditis-a-27-year-epidemiological-analysis-of-mortality-in-brazil/ |
| **Licença / Direitos** | Acesso aberto — IJCS publica sob licença Creative Commons (CC BY); consultar site do periódico para termos completos |
| **Recebido / Aceito** | Recebido: 23/07/2025 · Aceito: 08/09/2025 |
| **Palavras (~)** | 2 645 |

**Justificativa de seleção:**  
Este artigo epidemiológico analisa **40.157 mortes** por endocardite infecciosa (EI) no Brasil entre 1996 e 2022, usando dados do Sistema de Informações sobre Mortalidade (SIM/DATASUS) do SUS. Sua seleção atende diretamente à exigência do enunciado de utilizar fontes do **SUS** e contribui com vocabulário epidemiológico (CID-10, disparidades regionais, tendências temporais). Para NLP, é particularmente útil para **análise de tendências temporais em linguagem clínica**, **classificação por região geográfica** e **extração de estatísticas de mortalidade**, além de servir como exemplo de linguagem científica concisa que pode ser usada em tarefas de **sumarização automática**.

---

### 2.4 `Obstructive_Sleep_Apnea.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Obstructive Sleep Apnea as a Risk Factor for Ischemic Heart Disease |
| **Autores** | Soham Samajpaty, Alexander Konstantinovich Zhuravlov, Emilianovich Dmitrii, Ilin Yuriy Sergeivich |
| **Instituições** | Pirogov Russian National Research Medical University; City Clinic Hospital Nº 31 named after GM Savelyova, Moscou – Rússia |
| **Periódico** | International Journal of Cardiovascular Sciences (IJCS) |
| **Referência** | Int J Cardiovasc Sci. 2026;39:e20240250 |
| **DOI** | https://doi.org/10.36660/ijcs.20240250 |
| **Fonte / Link** | https://ijcscardiol.org/article/obstructive-sleep-apnea-as-a-risk-factor-for-ischemic-heart-disease/ |
| **Licença / Direitos** | Acesso aberto — IJCS publica sob licença Creative Commons (CC BY); consultar site do periódico para termos completos |
| **Recebido / Aceito** | Recebido: 18/01/2025 · Aceito: 08/09/2025 |
| **Palavras (~)** | 3 935 |

**Justificativa de seleção:**  
Estudo caso-controle com 122 participantes avaliando a **apneia obstrutiva do sono (AOS)** como fator de risco para a **cardiopatia isquêmica (CI)**. O questionário STOP-Bang e as métricas de risco (OR, RR, AR) introduzem no corpus uma camada de linguagem voltada à **avaliação de risco clínico estruturado**. Para NLP, esse texto é valioso para **extração de fatores de risco** e suas magnitudes, **identificação de escalas e questionários clínicos** e **modelagem de relações causal-associativa** entre condições comórbidas. A perspectiva de pesquisadores russos publicando no IJCS adiciona diversidade de estilo de escrita ao corpus.

---

### 2.5 `Pharmacological_Treatment_for_Heart_Failure.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Evidence-Based Pharmacological Treatment for Heart Failure in Brazil |
| **Autores** | Luísa Preiss Marques da Rocha, Kathleen Asturian, Isabel Machado Canabarro, Lidia Einsfeld, Diogo Pilger |
| **Instituições** | Universidade Federal do Rio Grande do Sul (UFRGS); Universidade Federal de Santa Catarina (UFSC); Hospital de Clínicas de Porto Alegre (HCPA) |
| **Periódico** | International Journal of Cardiovascular Sciences (IJCS) |
| **Referência** | Int J Cardiovasc Sci. 2026;39:e20250058 |
| **DOI** | https://doi.org/10.36660/ijcs.20250058 |
| **Fonte / Link** | https://ijcscardiol.org/article/evidence-based-pharmacological-treatment-for-heart-failure-in-brazil/ |
| **Licença / Direitos** | Acesso aberto — IJCS publica sob licença Creative Commons (CC BY); consultar site do periódico para termos completos |
| **Recebido / Aceito** | Recebido: 17/02/2025 · Aceito: 25/08/2025 |
| **Palavras (~)** | 5 487 |

**Justificativa de seleção:**  
Este estudo descritivo de corte transversal analisa o **acesso ao tratamento farmacológico da insuficiência cardíaca (IC)** no Sistema Único de Saúde (SUS) em 387 municípios brasileiros. Por tratar diretamente de políticas de saúde pública e medicamentos essenciais (inibidores do sistema renina-angiotensina, betabloqueadores, antagonistas de aldosterona, ISGLT2), é o texto mais rico em **terminologia farmacológica e de gestão em saúde**. Para NLP, é ideal para tarefas de **classificação de políticas de saúde**, **extração de nomes de medicamentos e classes farmacológicas**, e **análise de disparidades no acesso** — tópicos diretamente relevantes para IA aplicada à cardiologia no contexto do SUS.

---

## 3. Estatísticas do Dataset

| Arquivo | Palavras (~) | Linhas | Tipo de Estudo |
|---|---|---|---|
| `Childhood_Obesity.txt` | 4 743 | 657 | Corte transversal |
| `Coronary_Artery_Disease.txt` | 5 240 | 676 | Retrospectivo / caso-controle |
| `Endocarditis.txt` | 2 645 | 400 | Epidemiológico descritivo |
| `Obstructive_Sleep_Apnea.txt` | 3 935 | 484 | Caso-controle |
| `Pharmacological_Treatment_for_Heart_Failure.txt` | 5 487 | 645 | Descritivo de corte transversal |
| **Total** | **~22 050** | **2 862** | — |

- **Número de arquivos:** 5 (excede o mínimo de 2 exigido pelo enunciado)
- **Idioma:** Inglês científico (artigos de periódico internacional)
- **Domínio:** Cardiologia clínica e saúde pública cardiovascular
- **Fonte:** International Journal of Cardiovascular Sciences (IJCS) — indexado na BVS/SciELO
- **Distribuição temática:** Hipertensão pediátrica · Doença arterial coronariana · Endocardite · Apneia do sono · Insuficiência cardíaca

---

## 4. Aplicações em NLP

Os textos foram selecionados com foco em sua utilidade para as principais tarefas de NLP aplicadas à cardiologia:

| Tarefa NLP | Como os textos contribuem |
|---|---|
| **Extração de entidades clínicas (NER)** | Os artigos são ricos em nomes de doenças (HAS, DAC, IC, EI, AOS), exames (angiografia, STOP-Bang), medicamentos (IECA, ISGLT2, betabloqueadores) e biomarcadores (PCR, NLR, PLR), fornecendo exemplos reais de entidades biomédicas anotáveis. |
| **Classificação de tópicos** | Cada artigo pertence a um subtópico distinto da cardiologia, permitindo treinar classificadores de especialidade médica e triagem de literatura. |
| **Extração de relações** | Os textos contêm explicitamente relações do tipo *fator de risco → doença*, *medicamento → indicação*, *variável → desfecho*, fundamentais para construção de grafos de conhecimento clínico. |
| **Sumarização automática** | Os abstracts estruturados (Background, Objectives, Methods, Results, Conclusion) são pares ideais de texto completo–resumo para treino de modelos de sumarização extratora e abstrativa. |
| **Análise de sentimentos clínicos** | Expressões de certeza/incerteza ("may serve as", "remains underexplored", "highlights ongoing challenges") permitem modelar o grau de evidência clínica afirmada pelos autores. |
| **Question Answering (QA)** | A estrutura dos artigos permite criar pares pergunta–resposta sobre epidemiologia, fatores de risco, diagnóstico e tratamento, úteis para chatbots de suporte clínico. |

---

## 5. Pré-processamento Recomendado

Antes de utilizar os textos em pipelines de NLP, recomenda-se:

1. **Limpeza de artefatos de PDF:** Os arquivos foram convertidos de PDF para `.txt`; podem conter quebras de linha no meio de sentenças, hifenizações e caracteres especiais residuais que devem ser normalizados.
2. **Segmentação de sentenças:** Utilizar bibliotecas como `spaCy` (modelo `en_core_sci_md` do SciSpaCy) ou `NLTK` para segmentação precisa em texto científico.
3. **Tokenização:** Preservar expressões compostas como *C-reactive protein*, *neutrophil-to-lymphocyte ratio* e siglas (HF, CAD, OSA) como tokens únicos.
4. **Remoção de metadados:** Remover cabeçalhos de página (e.g., "Int J Cardiovasc Sci. 2026;39:..."), rodapés e informações de endereço antes de tarefas de modelagem.
5. **Normalização de referências bibliográficas:** As seções de *References* podem ser isoladas ou removidas dependendo da tarefa.
6. **Divisão por seção:** Separar Abstract, Introduction, Methods, Results, Discussion e Conclusion para tarefas seção-específicas.

---

## 6. Conformidade com o Enunciado

| Requisito do Enunciado | Status |
|---|---|
| Mínimo 2 arquivos `.txt` | ✅ 5 arquivos entregues |
| Fontes: SciELO / BVS / SUS / Projeto Gutenberg | ✅ IJCS indexado na BVS; um artigo usa dados do SUS (DATASUS) |
| Disponibilização em subpasta do GitHub | ✅ Diretório `dataset_texto/` |
| README explicando uso em NLP | ✅ Seção 4 deste README |
| Justificativa de importância na saúde | ✅ Todos os artigos abordam condições cardiovasculares prevalentes |
| Links públicos acessíveis | ✅ DOIs e URLs do IJCS listados na Seção 7 |

---

## 7. Links das Fontes

| Arquivo | URL da Fonte | DOI |
|---|---|---|
| `Childhood_Obesity.txt` | https://ijcscardiol.org/article/childhood-obesity-and-systemic-arterial-hypertension-in-children-and-adolescents-a-cross-sectional-study/ | https://doi.org/10.36660/ijcs.20240146 |
| `Coronary_Artery_Disease.txt` | https://ijcscardiol.org/article/inflammatory-and-atherogenic-markers-as-predictors-of-coronary-artery-disease-in-patients-with-suspected-coronary-artery-disease-undergoing-coronary-angiography/ | https://doi.org/10.36660/ijcs.20250039 |
| `Endocarditis.txt` | https://ijcscardiol.org/article/endocarditis-a-27-year-epidemiological-analysis-of-mortality-in-brazil/ | https://doi.org/10.36660/ijcs.20250124 |
| `Obstructive_Sleep_Apnea.txt` | https://ijcscardiol.org/article/obstructive-sleep-apnea-as-a-risk-factor-for-ischemic-heart-disease/ | https://doi.org/10.36660/ijcs.20240250 |
| `Pharmacological_Treatment_for_Heart_Failure.txt` | https://ijcscardiol.org/article/evidence-based-pharmacological-treatment-for-heart-failure-in-brazil/ | https://doi.org/10.36660/ijcs.20250058 |
| **Site do periódico (IJCS)** | https://ijcscardiol.org/ | — |

---

## 8. Observações Legais

- Todos os artigos são publicados em regime de **acesso aberto** pelo IJCS sob licença **Creative Commons (CC BY)**, o que permite reprodução, distribuição e adaptação com a devida atribuição aos autores originais.
- O uso neste projeto é estritamente **acadêmico e não comercial**, em conformidade com os termos das licenças Creative Commons e com as diretrizes do projeto CardioIA (FIAP).
- Ao utilizar ou redistribuir estes textos, citar sempre o artigo original com título, autores, periódico, volume, ano e DOI conforme os metadados listados na Seção 2.

---

*Referência ao enunciado completo: [`enunciado/enunciado.txt`](../enunciado/enunciado.txt)*