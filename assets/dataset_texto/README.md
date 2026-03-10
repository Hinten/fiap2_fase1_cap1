# Dataset de Textos — CardioIA (Projeto FIAP Fase 1, Capítulo 1)

## 1. Visão Geral

Este diretório contém o **corpus textual** do projeto **CardioIA**, desenvolvido como parte da **Fase 1 – Capítulo 1** da pós-graduação FIAP (PBL – Project Based Learning). O objetivo desta coleção é fornecer a base de dados textuais que alimentará os módulos de **Processamento de Linguagem Natural (NLP)** nas fases seguintes do projeto.

De acordo com o enunciado (ver [`enunciado/enunciado_resumido.txt`](../enunciado/enunciado_resumido.txt)), a **Parte 2 – Dados Textuais (NLP)** exige:

- No mínimo 2 arquivos `.txt` de fontes como SciELO, BVS, SUS ou Projeto Gutenberg;
- Disponibilização em subpasta do repositório GitHub;
- README explicando como os textos podem ser usados por NLP (análise de sentimentos, extração de sintomas, classificação de tópicos) e justificando sua importância na saúde.

Este dataset **supera amplamente** o mínimo exigido, reunindo **26 documentos** de acesso aberto agrupados em três fontes:

| Grupo | Fonte | Periódico / Organização | Nº de arquivos |
|---|---|---|---|
| **A** | BVS / SciELO | *International Journal of Cardiovascular Sciences* (IJCS) | 5 |
| **B** | BVS / SciELO | *Arquivos Brasileiros de Cardiologia* (Arq Bras Cardiol / ABC) — Sociedade Brasileira de Cardiologia (SBC) | 12 |
| **C** | acc.org / heart.org | Diretrizes ACC/AHA publicadas no *Journal of the American College of Cardiology* (JACC) | 9 |

Os grupos A e B atendem diretamente ao critério de fonte **BVS/SciELO** do enunciado. O grupo C representa literatura de referência internacional amplamente empregada na prática clínica cardiológica brasileira.

---

## 2. Arquivos do Dataset

### 2.A Artigos do IJCS — *International Journal of Cardiovascular Sciences*

#### 2.A.1 `Childhood_Obesity.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Childhood Obesity and Systemic Arterial Hypertension in Children and Adolescents: A Cross-Sectional Study |
| **Autores** | Rafaella Farias da Franca Almeida, Lívia Menezes Escorel, Letícia Odete Guedes de Andrade Carvalho, et al. |
| **Instituições** | Centro Universitário de João Pessoa; FAMENE; Complexo Hospitalar Infantil Arlinda Marques; Instituto Dante Pazzanese de Cardiologia |
| **Periódico** | International Journal of Cardiovascular Sciences (IJCS) |
| **Referência** | Int J Cardiovasc Sci. 2026;39:e20240146 |
| **Fonte / Link** | https://ijcscardiol.org/article/childhood-obesity-and-systemic-arterial-hypertension-in-children-and-adolescents-a-cross-sectional-study/ |
| **Licença / Direitos** | Acesso aberto — IJCS publica sob licença Creative Commons (CC BY); consultar site do periódico para termos completos |
| **Recebido / Aceito** | Recebido: 07/08/2024 · Aceito: 26/03/2025 |
| **Palavras (~)** | 4 743 |

**Justificativa de seleção:**  
Este artigo de corte transversal investiga a relação entre **obesidade infantil** e **hipertensão arterial sistêmica (HAS)** em crianças e adolescentes. Embora o foco seja pediátrico, a HAS e seus fatores de risco (IMC, histórico familiar, sedentarismo) são variáveis centrais em toda a cardiologia clínica. Para NLP, o texto oferece vocabulário clínico padronizado (p.ex. *percentil de pressão arterial*, *circunferência abdominal*, *qui-quadrado*), útil para **extração de entidades clínicas** (NER), **classificação de fatores de risco** e **análise de correlação sintoma–diagnóstico**. A diversidade de autores e instituições brasileiras também contribui para enriquecer o corpus com terminologia do sistema de saúde nacional.

---

#### 2.A.2 `Coronary_Artery_Disease.txt`

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

#### 2.A.3 `Endocarditis.txt`

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

#### 2.A.4 `Obstructive_Sleep_Apnea.txt`

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

#### 2.A.5 `Pharmacological_Treatment_for_Heart_Failure.txt`

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

### 2.B Artigos e Diretrizes da Arq Bras Cardiol — *Arquivos Brasileiros de Cardiologia* (SBC)

> O periódico *Arquivos Brasileiros de Cardiologia* (Arq Bras Cardiol) é o principal periódico da **Sociedade Brasileira de Cardiologia (SBC)**, indexado na **BVS** e no **SciELO**, atendendo ao critério de fonte do enunciado. DOIs apontam para https://doi.org/10.36660/abc.\*

---

#### 2.B.1 `2025 Brazilian Evidence-based Guideline on the.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2025 Brazilian Evidence-based Guideline on the Management of Obesity and Prevention of Cardiovascular Disease and Obesity-Associated Complications: A Position Statement by Five Medical Societies |
| **Autores** | José Francisco Kerr Saraiva, Cynthia M. Valerio, Fabiana H. Rached, Simone Van de Sande-Lee, et al. |
| **Desenvolvimento** | ABESO, SBD, SBC, SBEM e ABS |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2025; 122(9):e20250621 |
| **DOI** | https://doi.org/10.36660/abc.20250621 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 17 860 |

**Justificativa de seleção:**  
Diretriz de posicionamento elaborada por cinco sociedades médicas brasileiras (ABESO, SBD, SBC, SBEM, ABS) sobre o **manejo da obesidade** e prevenção de **doenças cardiovasculares**. Cobre mecanismos fisiopatológicos, critérios diagnósticos, metas terapêuticas e farmacoterapia (incluindo agonistas de GLP-1). Para NLP, enriquece o corpus com terminologia sobre **comorbidades metabólicas**, **classes farmacológicas antiobesidade** e **linguagem de consenso multiprofissional**, útil para tarefas de **classificação de diretrizes** e **extração de recomendações estruturadas** (grau de evidência/recomendação).

---

#### 2.B.2 `Brazilian Atrial Fibrillation Guidelines.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Brazilian Atrial Fibrillation Guidelines – 2025 |
| **Editor** | Fatima Dumas Cintra |
| **Desenvolvimento** | SOBRAC (Sociedade Brasileira de Arritmia Cardíaca) e SBC (Sociedade Brasileira de Cardiologia) |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2025; 122(9):e20250618 |
| **DOI** | https://doi.org/10.36660/abc.20250618 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 71 872 |

**Justificativa de seleção:**  
Diretriz brasileira completa sobre **fibrilação atrial (FA)**, abrangendo diagnóstico, estratificação de risco tromboembólico (CHA₂DS₂-VASc), anticoagulação, controle de ritmo/frequência e ablação por cateter. Com mais de 70 mil palavras, é o documento mais extenso do Grupo B e concentra amplo vocabulário sobre **arritmias**, **anticoagulantes orais diretos (NOAC/DOAC)** e **eletrofisiologia**. Para NLP, é ideal para **extração de recomendações clínicas**, **classificação de níveis de evidência** e **construção de grafos de conhecimento** sobre FA.

---

#### 2.B.3 `Brazilian Guideline for the Evaluation and Diagnosis of Chest.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Brazilian Guideline for the Evaluation and Diagnosis of Chest Pain in the Emergency Department – 2025 |
| **Coordenadores** | Pedro Gabriel Melo de Barros e Silva, Alexandre de Matos Soeiro |
| **Desenvolvimento** | GECETI/DCC-SBC e FLAME (Federación Latinoamericana de Medicina de Emergencias) |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2025; 122(9):e20250620 |
| **DOI** | https://doi.org/10.36660/abc.20250620 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 46 514 |

**Justificativa de seleção:**  
Diretriz brasileira (com participação latino-americana via FLAME) dedicada à **avaliação e diagnóstico de dor torácica** no pronto-socorro. Inclui protocolos de triagem, biomarcadores cardíacos (troponina de alta sensibilidade), estratificação de risco e critérios de alta precoce. Para NLP, o documento é valioso para **extração de protocolos de triagem**, **reconhecimento de entidades de emergência cardiovascular** e **análise de fluxos de decisão clínica** expressados em linguagem natural.

---

#### 2.B.4 `Cardiogenic Shock Due to Inverted-Pattern Takotsubo Syndrome.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Cardiogenic Shock Due to Inverted-Pattern Takotsubo Syndrome Caused by Pheochromocytoma: Case Report and Literature Review |
| **Autores** | Pedro Ivo De Marqui Moraes, Michell Fayad André Haddad, Daniel Bisi de Bôrtoli Valle, Luiz Otávio de Oliveira Filho, Mayara da Silva Custódio, Dirceu Rodrigues de Almeida |
| **Instituições** | Universidade Federal de São Paulo (UNIFESP), São Paulo, SP – Brazil |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2026; 123(2):e20250558 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 3 003 |

**Justificativa de seleção:**  
Research Letter com relato de caso e revisão da literatura sobre **choque cardiogênico** causado pela **síndrome de Takotsubo de padrão invertido** associada a **feocromocitoma**. O texto apresenta terminologia especializada de cardiomiopatia de estresse, catecolaminas e manejo hemodinâmico. Para NLP, é útil para treinar modelos de **extração de entidades de apresentações clínicas raras**, **análise de relações causa-efeito** (tumor → estimulação simpática → síndrome → choque) e **classificação de relatos de caso** vs. artigos de revisão.

---

#### 2.B.5 `Cardiovascular Computed Tomography and Magnetic.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Cardiovascular Computed Tomography and Magnetic Resonance Imaging Guideline of the Brazilian Society of Cardiology and the Brazilian College of Radiology – 2024 |
| **Coordenadores** | Carlos Eduardo Rochitte, Tiago Augusto Magalhães |
| **Desenvolvimento** | Departamento de Imagem Cardiovascular (DIC/SBC) e Colégio Brasileiro de Radiologia (CBR) |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2024;121(9):e20240608 |
| **DOI** | https://doi.org/10.36660/abc.20240608 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 106 606 |

**Justificativa de seleção:**  
Diretriz SBC/CBR sobre **tomografia computadorizada cardiovascular (TC)** e **ressonância magnética cardíaca (RMC)**, cobrindo indicações, protocolos, interpretação e laudos. Com mais de 106 mil palavras, é o documento mais extenso do Grupo B. Contém terminologia de **imagem cardiovascular** (escore de cálcio, angiotomografia coronariana, mapeamento T1/T2, realce tardio), relevante para projetos de NLP integrados à **Visão Computacional**. Para NLP, apoia **extração de indicações de exames**, **classificação de laudos** e **normalização de terminologia radiológica cardiológica**.

---

#### 2.B.6 `Guideline for Chronic Coronary Syndrome.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Guideline for Chronic Coronary Syndrome – 2025 |
| **Coordenadores** | Luiz A. Machado Cesar, Luis Henrique W. Gowdak, Ricardo Pavanello, João Fernando M. Ferreira |
| **Desenvolvimento** | DCC, DCC/GEAT, DCC/GAPO, DIC — Sociedade Brasileira de Cardiologia (SBC) |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2025; 122(9):e20250619 |
| **DOI** | https://doi.org/10.36660/abc.20250619 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 85 316 |

**Justificativa de seleção:**  
Diretriz brasileira abrangente sobre **síndrome coronariana crônica (SCC)**, incluindo diagnóstico, estratificação de risco, revascularização e tratamento farmacológico de longo prazo. Com mais de 85 mil palavras e múltiplos capítulos estruturados, é uma fonte primária para **extração de recomendações graduadas** (Classe I/IIa/IIb/III, Níveis A/B/C), **identificação de critérios diagnósticos** e **reconhecimento de nomes de fármacos coronarianos**. A estrutura de seções facilita também o treino de modelos de **segmentação de texto médico**.

---

#### 2.B.7 `Guideline for Perioperative Cardiovascular Evaluation of the.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Guideline for Perioperative Cardiovascular Evaluation of the Brazilian Society of Cardiology – 2024 |
| **Comitê de redação** | Danielle M. Gualandro, Luciana S. Fornari, Bruno Caramelli |
| **Desenvolvimento** | GAPO e DCC — Sociedade Brasileira de Cardiologia (SBC) |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2024;121(9):e20240590 |
| **DOI** | https://doi.org/10.36660/abc.20240590 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 50 405 |

**Justificativa de seleção:**  
Diretriz SBC sobre **avaliação cardiovascular perioperatória**, orientando a conduta cardiológica antes de procedimentos cirúrgicos não cardíacos. Aborda estratificação de risco cirúrgico, uso de betabloqueadores, anticoagulação perioperatória e critérios de adiamento de cirurgia. Para NLP, o documento é rico em **vocabulário de risco cirúrgico**, **protocolos de estratificação** e **relações entre condição cardiovascular e decisão clínica**, útil para treinar sistemas de **suporte a decisão clínica**.

---

#### 2.B.8 `Guidelines on the Diagnosis and Treatment of Hypertrophic.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Guidelines on the Diagnosis and Treatment of Hypertrophic Cardiomyopathy – 2024 |
| **Coordenadores** | Fábio Fernandes, Marcus Vinicius Simões |
| **Desenvolvimento** | Departamento de Insuficiência Cardíaca (DEIC) e GEMIC — Sociedade Brasileira de Cardiologia (SBC) |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2024;121(7):e202400415 |
| **DOI** | https://doi.org/10.36660/abc.20240415 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 46 248 |

**Justificativa de seleção:**  
Diretriz brasileira sobre **cardiomiopatia hipertrófica (CMH)**, cobrindo diagnóstico genético-molecular, ecocardiografia, RMC, estratificação de risco de morte súbita e tratamento (incluindo mavacamten). Para NLP, introduz no corpus terminologia de **genética cardiovascular**, **disfunção diastólica** e **obstrução da via de saída do ventrículo esquerdo (VSVE)**, enriquecendo a capacidade de modelos para **reconhecimento de variantes genéticas** e **classificação de cardiomiopatias**.

---

#### 2.B.9 `Interstitial Myocardial Fibrosis Analysis by Histology and Cardiac.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Interstitial Myocardial Fibrosis Analysis by Histology and Cardiac Magnetic Resonance in Severe Aortic Valve Disease |
| **Autores** | Juliana Hiromi Silva Matsumoto Bello, Lea M.M.F. Demarchi, Rafael Almeida Fonseca, Gabriele N. Lima, et al. |
| **Instituições** | Instituto do Coração (InCor) do HC-FMUSP; Hospital das Clínicas da FMUSP, São Paulo, SP – Brazil |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2026; 123(2):e20250203 |
| **Recebido / Aceito** | Recebido: 20/03/2025 · Aceito: 19/12/2025 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 5 426 |

**Justificativa de seleção:**  
Artigo original (108 pacientes) que compara métodos histológicos (**fração de volume de colágeno — CVF**) com técnicas de **RMC** (realce tardio e mapeamento T1/ECV) para quantificar fibrose miocárdica intersticial na doença valvar aórtica grave. Para NLP, enriquece o corpus com terminologia de **histopatologia cardíaca** e **parametrização de imagens de RMC**, viabilizando a extração de correlações entre achados de biópsia e exames não invasivos — tópico relevante para sistemas de IA que integram NLP e Visão Computacional.

---

#### 2.B.10 `PRKAG2 Cardiomyopathy A Case-Control Study on the Diagnostic.txt`

| Campo | Detalhe |
|---|---|
| **Título** | PRKAG2 Cardiomyopathy: A Case-Control Study on the Diagnostic Yield of Histopathology and Ultrastructural Analysis from Endomyocardial Biopsy |
| **Autores** | Kinulpe Honorato-Sampaio, Carla de Oliveira, Stanley de Almeida Araújo, Frederico Soares Correa, et al. |
| **Instituições** | UFVJM (Diamantina, MG); HC-UFMG (Belo Horizonte, MG); Hospital Biocor-Rede D'Or; University of Oxford (UK); et al. |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2026; 123(2):e20240616 |
| **Recebido / Aceito** | Recebido: 10/03/2025 · Aceito: 13/01/2026 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 6 018 |

**Justificativa de seleção:**  
Estudo caso-controle (18 pacientes com cardiomiopatia PRKAG2 e 11 controles) avaliando o rendimento diagnóstico da **biópsia endomiocárdica** por histopatologia (colorações H&E, PAS, Masson) e microscopia eletrônica de transmissão. Para NLP, é uma fonte valiosa de vocabulário de **genética molecular de cardiomiopatias raras**, **ultraestrutura celular** e **critérios diagnósticos patológicos**, ampliando a cobertura do corpus para doenças cardiovasculares raras e tópicos de precisão diagnóstica.

---

#### 2.B.11 `Position Statement on Cardiometabolic Health Across the.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Position Statement on Cardiometabolic Health Across the Woman's Life Course – 2025 |
| **Autores** | Gláucia Maria Moraes de Oliveira, Maria Cristina Costa de Almeida, Cynthia Melissa Valério, et al. |
| **Desenvolvimento** | Departamento de Cardiologia da Mulher (DCM/SBC) — Sociedade Brasileira de Cardiologia |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2025; 122(9):e2025015 |
| **DOI** | https://doi.org/10.36660/abc.20250615 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 60 543 |

**Justificativa de seleção:**  
Posicionamento abrangente da SBC sobre **saúde cardiometabólica feminina** ao longo do ciclo de vida (puberdade, gravidez, menopausa), incluindo hipertensão na gravidez, síndrome metabólica, diabetes e doença cardiovascular aterosclerótica. Para NLP, introduz perspectiva de **equidade de gênero em cardiologia**, enriquecendo o corpus com vocabulário de **saúde da mulher**, **hormônios e risco cardiovascular** e **terminologia obstétrica/ginecológica aplicada à cardiologia**, relevante para sistemas de NLP voltados a disparidades em saúde.

---

#### 2.B.12 `Reference Echocardiographic Values for Cardiac Chambers in Brazil.txt`

| Campo | Detalhe |
|---|---|
| **Título** | Reference Echocardiographic Values for Cardiac Chambers in Brazil: A Multiregional, Multi-Racial Study |
| **Autores** | Ana Clara Tude Rodrigues, Roberto Magalhães Saraiva, Viviane T. Hotta, Gabriel Doreto Rodrigues, et al. |
| **Instituições** | Hospital Israelita Albert Einstein; InCor/HC-FMUSP; Fiocruz; Fleury Medicina e Saúde; múltiplas instituições de todas as regiões do Brasil |
| **Periódico** | Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol) |
| **Referência** | Arq Bras Cardiol. 2026; 123(2):e20250628 |
| **Licença / Direitos** | Acesso aberto — Arq Bras Cardiol publica sob licença Creative Commons; consultar site do periódico para termos completos |
| **Palavras (~)** | 6 203 |

**Justificativa de seleção:**  
Estudo observacional multiregional e multirracial estabelecendo **valores de referência ecocardiográficos** para câmaras cardíacas na população brasileira. A diversidade de centros (todas as regiões do país) e a ênfase em variação étnico-racial tornam este texto relevante para NLP aplicado à **normalização de laudos ecocardiográficos** e **detecção de viés em valores de referência**, tema crítico em governança de dados para IA na saúde.

---

### 2.C Diretrizes ACC/AHA publicadas no JACC — *Journal of the American College of Cardiology*

> Os documentos deste grupo são diretrizes clínicas conjuntas do **American College of Cardiology (ACC)** e da **American Heart Association (AHA)**, publicadas no *Journal of the American College of Cardiology* (JACC). Embora não estejam indexados na BVS/SciELO, são os documentos de referência internacional mais utilizados na cardiologia clínica brasileira e enriquecem o corpus com linguagem de **diretrizes internacionais de alto impacto**.

---

#### 2.C.1 `Guideline for Coronary Artery Revascularization.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2021 ACC/AHA/SCAI Guideline for Coronary Artery Revascularization |
| **Autores (Chair/Vice-Chair)** | Jennifer S. Lawton (Chair), Jacqueline E. Tamis-Holland (Vice-Chair), et al. |
| **Organização** | ACC / AHA / SCAI |
| **Publicação** | J Am Coll Cardiol. 2022;79:e21–e129 |
| **DOI** | https://doi.org/10.1016/j.jacc.2021.09.006 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 87 880 |

**Justificativa de seleção:**  
Diretriz ACC/AHA/SCAI sobre **revascularização coronariana** (intervenção coronariana percutânea — ICP e cirurgia de revascularização miocárdica — CRM), com recomendações graduadas sobre indicações de revascularização, estratégias de stent e acesso vascular. Para NLP, é a principal referência para **extração de indicações de procedimentos cardiovasculares**, **comparação ICP vs. CRM** e **análise de recomendações técnicas intervencionistas**.

---

#### 2.C.2 `Guideline for the Diagnosis and Management of Aortic Disease.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2022 ACC/AHA Guideline for the Diagnosis and Management of Aortic Disease |
| **Autores (Chair/Vice-Chair)** | Eric M. Isselbacher (Chair), Ourania Preventza (Vice-Chair), James Hamilton Black III (Vice-Chair), et al. |
| **Organização** | ACC / AHA (com colaboração de AATS, ACR, SCA, SCAI, STS, SVS, SIR, SVM) |
| **Publicação** | J Am Coll Cardiol. 2022 |
| **DOI** | https://doi.org/10.1016/j.jacc.2022.08.004 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 126 207 |

**Justificativa de seleção:**  
Diretriz ACC/AHA abrangente sobre **doenças da aorta** (aneurismas, dissecção aórtica, síndrome aórtica aguda), integrando perspectivas cirúrgicas, cardiológicas e radiológicas. Com mais de 126 mil palavras, é um dos documentos mais volumosos do corpus. Para NLP, é uma fonte primária para **extração de critérios diagnósticos de emergência aórtica**, **classificações anatômicas** (Stanford, DeBakey) e **indicações cirúrgicas vs. tratamento endovascular**.

---

#### 2.C.3 `Guideline for the Diagnosis and Management of Atrial Fibrillation.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2023 ACC/AHA/ACCP/HRS Guideline for the Diagnosis and Management of Atrial Fibrillation |
| **Autores (Chair/Vice-Chair)** | José A. Joglar (Chair), Mina K. Chung (Vice-Chair), et al. |
| **Organização** | ACC / AHA / ACCP / HRS |
| **Publicação** | J Am Coll Cardiol. 2024;83:109–279 |
| **DOI** | https://doi.org/10.1016/j.jacc.2023.08.017 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 131 960 |

**Justificativa de seleção:**  
Diretriz ACC/AHA/ACCP/HRS mais atual sobre **fibrilação atrial (FA)**, cobrindo fisiopatologia, diagnóstico, estratificação de risco (CHA₂DS₂-VASc), anticoagulação, controle de frequência/ritmo, cardioversão e ablação. Com cerca de 132 mil palavras, é o documento mais extenso do corpus. Combinado com o arquivo 2.B.2, viabiliza análises comparativas de **diretrizes brasileiras vs. internacionais** sobre o mesmo tema — tarefa de NLP de alto valor para **harmonização de protocolos** e **detecção de divergências de recomendação**.

---

#### 2.C.4 `Guideline for the Evaluation and Diagnosis of Chest Pain.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2021 AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR Guideline for the Evaluation and Diagnosis of Chest Pain |
| **Autores (Chair/Vice-Chair)** | Martha Gulati (Chair), Phillip D. Levy (Vice-Chair), Debabrata Mukherjee (Vice-Chair), et al. |
| **Organização** | AHA / ACC / ASE / CHEST / SAEM / SCCT / SCMR |
| **Publicação** | J Am Coll Cardiol. 78(22):e187–e285 |
| **DOI** | https://doi.org/10.1016/j.jacc.2021.07.053 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 70 274 |

**Justificativa de seleção:**  
Diretriz multissociedade sobre **avaliação e diagnóstico de dor torácica**, abrangendo desde a triagem inicial até a investigação avançada (cintilografia, angiotomografia, RMC). Combinado com o arquivo 2.B.3, possibilita análises comparativas de **recomendações brasileiras vs. norte-americanas** para o mesmo cenário clínico. Para NLP, o documento é especialmente útil para **extração de algoritmos diagnósticos** e **classificação de sintomas torácicos**.

---

#### 2.C.5 `Guideline for the Management of Adults With Congenital Heart Disease.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2025 ACC/AHA/HRS/ISACHD/SCAI Guideline for the Management of Adults With Congenital Heart Disease |
| **Autores (Chair/Vice-Chair)** | Michelle Gurvitz (Chair), Eric V. Krieger (Co-Vice-Chair), Stephanie Fuller (Co-Vice-Chair), et al. |
| **Organização** | ACC / AHA / HRS / ISACHD / SCAI |
| **Publicação** | J Am Coll Cardiol. 2026;87(7):822–976 |
| **DOI** | https://doi.org/10.1016/j.jacc.2025.09.006 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 57 763 |

**Justificativa de seleção:**  
Diretriz ACC/AHA/HRS/ISACHD/SCAI sobre **cardiopatias congênitas no adulto (CCA)**, incluindo comunicação interatrial, comunicação interventricular, tetralogia de Fallot, transposição de grandes artérias e outras lesões complexas. Para NLP, introduz no corpus terminologia específica de **anatomia cardíaca congênita**, **cirurgia paliativa e corretora** e **follow-up de longo prazo**, expandindo a cobertura do corpus para além da cardiologia adquirida.

---

#### 2.C.6 `Guideline for the Management of Heart Failure.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure |
| **Autores (Chair/Vice-Chair)** | Paul A. Heidenreich (Chair), Biykem Bozkurt (Vice-Chair), et al. |
| **Organização** | AHA / ACC / HFSA |
| **Publicação** | J Am Coll Cardiol. 2022;79:e263–e421 |
| **DOI** | https://doi.org/10.1016/j.jacc.2021.12.012 |
| **Fonte** | https://www.acc.org / https://professional.heart.org / https://www.hfsa.org |
| **Palavras (~)** | 125 272 |

**Justificativa de seleção:**  
Diretriz AHA/ACC/HFSA sobre **insuficiência cardíaca (IC)**, abrangendo a nova classificação (HFrEF, HFmrEF, HFpEF), terapia farmacológica quadrupla (IECA/BRA/ARNI, betabloqueadores, MRA, ISGLT2), dispositivos (CDI, TRC) e transplante cardíaco. Junto com o arquivo 2.A.5 (IJCS), permite análise NLP comparativa entre **abordagem brasileira e norte-americana do tratamento da IC** — tarefa relevante para **análise de concordância de recomendações internacionais**.

---

#### 2.C.7 `Guideline for the Management of Hypertrophic Cardiomyopathy.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of Hypertrophic Cardiomyopathy |
| **Autores (Chair/Vice-Chair)** | Steve R. Ommen (Chair), Carolyn Y. Ho (Vice-Chair), et al. |
| **Organização** | AHA / ACC / AMSSM / HRS / PACES / SCMR |
| **Publicação** | J Am Coll Cardiol. 2024;83(23):2324–2405 |
| **DOI** | https://doi.org/10.1016/j.jacc.2024.02.014 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 63 075 |

**Justificativa de seleção:**  
Diretriz AHA/ACC sobre **cardiomiopatia hipertrófica (CMH)**, incluindo diagnóstico genético, imagem, estratificação de risco de morte súbita, tratamento farmacológico (mavacamten) e cirúrgico (miectomia). Combinado com o arquivo 2.B.8 (SBC), o corpus passa a conter diretrizes brasileira e norte-americana sobre o mesmo tema, viabilizando **análise comparativa internacional de recomendações** via NLP — um recurso valioso para sistemas de suporte clínico multilíngues e multiregionais.

---

#### 2.C.8 `Guideline for the Management of Lower Extremity Peripheral Artery Disease.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2024 ACC/AHA/AACVPR/APMA/ABC/SCAI/SVM/SVN/SVS/SIR/VESS Guideline for the Management of Lower Extremity Peripheral Artery Disease |
| **Autores (Chair/Co-Vice-Chair)** | Heather L. Gornik (Chair), Herbert D. Aronow (Co-Vice-Chair), Philip P. Goodney (Co-Vice-Chair), et al. |
| **Organização** | ACC / AHA e múltiplas sociedades vasculares e de reabilitação |
| **Publicação** | J Am Coll Cardiol. 2024 (VOL. 83, NO. 24) |
| **DOI** | https://doi.org/10.1016/j.jacc.2024.02.013 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 80 557 |

**Justificativa de seleção:**  
Diretriz ACC/AHA sobre **doença arterial periférica dos membros inferiores (DAP-MI)**, incluindo claudicação intermitente, isquemia crítica de membro, diagnóstico por índice tornozelo-braço (ITB) e tratamento (reabilitação, farmacoterapia, revascularização). Para NLP, expande o corpus para além da cardiologia intracardíaca, cobrindo **doença vascular periférica** e permitindo **extração de indicadores de gravidade de isquemia de membro** e **recomendações de intervenção vascular**.

---

#### 2.C.9 `Guideline for the Management of Patients With Acute Coronary Syndromes.txt`

| Campo | Detalhe |
|---|---|
| **Título** | 2025 ACC/AHA/ACEP/NAEMSP/SCAI Guideline for the Management of Patients With Acute Coronary Syndromes |
| **Autores (Chair/Vice-Chair)** | Sunil V. Rao (Chair), Michelle L. O'Donoghue (Vice-Chair), Marc Ruel (Vice-Chair), et al. |
| **Organização** | ACC / AHA / ACEP / NAEMSP / SCAI |
| **Publicação** | J Am Coll Cardiol. 2025;85(22):2135–2237 |
| **DOI** | https://doi.org/10.1016/j.jacc.2024.11.009 |
| **Fonte** | https://www.acc.org / https://professional.heart.org |
| **Palavras (~)** | 77 962 |

**Justificativa de seleção:**  
Diretriz ACC/AHA mais recente (2025) sobre **síndromes coronarianas agudas (SCA)**, abrangendo IAMCSST, IAMSSST e angina instável — desde o atendimento pré-hospitalar (NAEMSP/ACEP) até a alta hospitalar e reabilitação. Para NLP, é a referência mais atualizada para **extração de protocolos de emergência cardiovascular**, **nomenclatura de SCA** e **recomendações de antitrombóticos**, completando o ciclo de cobertura das principais síndromes coronarianas no corpus.

---

## 3. Estatísticas do Dataset

### 3.1 Grupo A — IJCS (*International Journal of Cardiovascular Sciences*)

| Arquivo | Palavras (~) | Linhas | Tipo de Documento |
|---|---|---|---|
| `Childhood_Obesity.txt` | 4 743 | 657 | Artigo original — corte transversal |
| `Coronary_Artery_Disease.txt` | 5 240 | 676 | Artigo original — retrospectivo |
| `Endocarditis.txt` | 2 645 | 400 | Artigo original — epidemiológico descritivo |
| `Obstructive_Sleep_Apnea.txt` | 3 935 | 484 | Artigo original — caso-controle |
| `Pharmacological_Treatment_for_Heart_Failure.txt` | 5 487 | 645 | Artigo original — corte transversal |
| **Subtotal Grupo A** | **~22 050** | **2 862** | — |

### 3.2 Grupo B — Arq Bras Cardiol (*Arquivos Brasileiros de Cardiologia* / SBC)

| Arquivo | Palavras (~) | Linhas | Tipo de Documento |
|---|---|---|---|
| `2025 Brazilian Evidence-based Guideline on the.txt` | 17 860 | 2 478 | Posicionamento / diretriz (5 sociedades) |
| `Brazilian Atrial Fibrillation Guidelines.txt` | 71 872 | 9 081 | Diretriz SOBRAC/SBC |
| `Brazilian Guideline for the Evaluation and Diagnosis of Chest.txt` | 46 514 | 5 744 | Diretriz SBC/FLAME |
| `Cardiogenic Shock Due to Inverted-Pattern Takotsubo Syndrome.txt` | 3 003 | 396 | Research Letter / relato de caso |
| `Cardiovascular Computed Tomography and Magnetic.txt` | 106 606 | 13 162 | Diretriz SBC/CBR |
| `Guideline for Chronic Coronary Syndrome.txt` | 85 316 | 11 055 | Diretriz SBC |
| `Guideline for Perioperative Cardiovascular Evaluation of the.txt` | 50 405 | 6 794 | Diretriz SBC |
| `Guidelines on the Diagnosis and Treatment of Hypertrophic.txt` | 46 248 | 5 761 | Diretriz SBC |
| `Interstitial Myocardial Fibrosis Analysis by Histology and Cardiac.txt` | 5 426 | 707 | Artigo original |
| `PRKAG2 Cardiomyopathy A Case-Control Study on the Diagnostic.txt` | 6 018 | 832 | Artigo original — caso-controle |
| `Position Statement on Cardiometabolic Health Across the.txt` | 60 543 | 7 935 | Posicionamento SBC |
| `Reference Echocardiographic Values for Cardiac Chambers in Brazil.txt` | 6 203 | 808 | Artigo original — multicêntrico |
| **Subtotal Grupo B** | **~506 014** | **64 753** | — |

### 3.3 Grupo C — JACC (*Journal of the American College of Cardiology* / ACC-AHA)

| Arquivo | Palavras (~) | Linhas | Tipo de Documento |
|---|---|---|---|
| `Guideline for Coronary Artery Revascularization.txt` | 87 880 | 8 532 | Diretriz ACC/AHA/SCAI |
| `Guideline for the Diagnosis and Management of Aortic Disease.txt` | 126 207 | 12 663 | Diretriz ACC/AHA |
| `Guideline for the Diagnosis and Management of Atrial Fibrillation.txt` | 131 960 | 14 654 | Diretriz ACC/AHA/ACCP/HRS |
| `Guideline for the Evaluation and Diagnosis of Chest Pain.txt` | 70 274 | 7 419 | Diretriz AHA/ACC e multissociedade |
| `Guideline for the Management of Adults With Congenital Heart Disease.txt` | 57 763 | 17 472 | Diretriz ACC/AHA |
| `Guideline for the Management of Heart Failure.txt` | 125 272 | 12 279 | Diretriz AHA/ACC/HFSA |
| `Guideline for the Management of Hypertrophic Cardiomyopathy.txt` | 63 075 | 6 528 | Diretriz AHA/ACC |
| `Guideline for the Management of Lower Extremity Peripheral Artery Disease.txt` | 80 557 | 8 821 | Diretriz ACC/AHA e multissociedade |
| `Guideline for the Management of Patients With Acute Coronary Syndromes.txt` | 77 962 | 8 662 | Diretriz ACC/AHA |
| **Subtotal Grupo C** | **~820 950** | **97 030** | — |

### 3.4 Resumo Geral

| Grupo | Fonte | Nº Arquivos | Palavras (~) | Linhas |
|---|---|---|---|---|
| A | IJCS (BVS) | 5 | ~22 050 | 2 862 |
| B | Arq Bras Cardiol / SBC (BVS/SciELO) | 12 | ~506 014 | 64 753 |
| C | JACC / ACC-AHA | 9 | ~820 950 | 97 030 |
| **Total** | — | **26** | **~1 349 014** | **164 645** |

- **Número de arquivos:** 26 (excede amplamente o mínimo de 2 exigido pelo enunciado)
- **Idioma:** Inglês científico
- **Domínio:** Cardiologia clínica, saúde cardiovascular e saúde pública
- **Distribuição temática:** Hipertensão · Obesidade · Doença coronariana · Insuficiência cardíaca · Fibrilação atrial · Cardiomiopatias · Doenças da aorta · Doença vascular periférica · Cardiopatia congênita · Endocardite · Apneia do sono · Imagem cardiovascular · Perioperatório · Saúde da mulher

---

## 4. Aplicações em NLP

Os textos foram selecionados com foco em sua utilidade para as principais tarefas de NLP aplicadas à cardiologia:

| Tarefa NLP | Como os textos contribuem |
|---|---|
| **Extração de entidades clínicas (NER)** | O corpus cobre nomes de doenças (HAS, DAC, IC, FA, CMH, EI, AOS, SCA), exames (angiografia, ecocardiografia, RMC, TC), medicamentos (IECA, NOAC, ISGLT2, betabloqueadores, mavacamten) e biomarcadores (PCR, NLR, troponina, BNP), fornecendo exemplos reais de entidades biomédicas anotáveis em múltiplos contextos clínicos. |
| **Classificação de tópicos** | Os 26 documentos abrangem subtópicos distintos da cardiologia, possibilitando treinar classificadores de especialidade médica, tipo de documento (artigo original vs. diretriz vs. posicionamento) e triagem de literatura. |
| **Extração de recomendações graduadas** | As diretrizes SBC e ACC/AHA contêm sistematicamente recomendações com Classe (I/IIa/IIb/III) e Nível de evidência (A/B/C), viabilizando treino de modelos de extração de recomendações estruturadas. |
| **Extração de relações** | Os textos contêm explicitamente relações do tipo *fator de risco → doença*, *medicamento → indicação*, *variável → desfecho*, fundamentais para construção de grafos de conhecimento clínico. |
| **Análise comparativa Brasil vs. internacional** | Pares de diretrizes sobre o mesmo tema (FA: 2.B.2 vs. 2.C.3; CMH: 2.B.8 vs. 2.C.7; dor torácica: 2.B.3 vs. 2.C.4; IC: 2.A.5 vs. 2.C.6) permitem análises de divergência e convergência entre recomendações nacionais e internacionais. |
| **Sumarização automática** | Os abstracts estruturados (Background, Objectives, Methods, Results, Conclusion) são pares ideais de texto completo–resumo para treino de modelos de sumarização extratora e abstrativa. |
| **Análise de sentimentos clínicos** | Expressões de certeza/incerteza ("may serve as", "remains underexplored", "is recommended", "may be considered") permitem modelar o grau de evidência clínica afirmada pelos autores. |
| **Question Answering (QA)** | A estrutura dos documentos permite criar pares pergunta–resposta sobre epidemiologia, fatores de risco, diagnóstico e tratamento, úteis para chatbots de suporte clínico. |

---

## 5. Pré-processamento Recomendado

Antes de utilizar os textos em pipelines de NLP, recomenda-se:

1. **Limpeza de artefatos de PDF:** Os arquivos foram convertidos de PDF para `.txt`; podem conter quebras de linha no meio de sentenças, hifenizações e caracteres especiais residuais que devem ser normalizados.
2. **Segmentação de sentenças:** Utilizar bibliotecas como `spaCy` (modelo `en_core_sci_md` do SciSpaCy) ou `NLTK` para segmentação precisa em texto científico.
3. **Tokenização:** Preservar expressões compostas como *C-reactive protein*, *neutrophil-to-lymphocyte ratio* e siglas (HF, CAD, OSA, AF) como tokens únicos.
4. **Remoção de metadados:** Remover cabeçalhos de página (e.g., "Arq Bras Cardiol. 2025;122(9):...", "J Am Coll Cardiol. 2022;79:..."), rodapés e informações de endereço antes de tarefas de modelagem.
5. **Normalização de referências bibliográficas:** As seções de *References* podem ser isoladas ou removidas dependendo da tarefa.
6. **Divisão por seção:** Separar Abstract, Introduction, Methods, Results, Discussion e Conclusion (artigos originais) ou capítulos temáticos (diretrizes) para tarefas seção-específicas.
7. **Tratamento de tabelas de recomendação:** Diretrizes contêm tabelas com classes e níveis de evidência que requerem tratamento específico para manter a estrutura semântica.

---

## 6. Conformidade com o Enunciado

| Requisito do Enunciado | Status |
|---|---|
| Mínimo 2 arquivos `.txt` | ✅ 26 arquivos entregues (Grupos A, B e C) |
| Fontes: SciELO / BVS / SUS / Projeto Gutenberg | ✅ Grupos A e B indexados na BVS/SciELO; artigos do Grupo B publicados pela SBC; arquivo 2.A.3 usa dados do SUS (DATASUS) |
| Disponibilização em subpasta do GitHub | ✅ Diretório `assets/dataset_texto/files/` |
| README explicando uso em NLP | ✅ Seção 4 deste README |
| Justificativa de importância na saúde | ✅ Todos os documentos abordam condições cardiovasculares de alta prevalência e mortalidade |
| Links públicos acessíveis | ✅ DOIs e URLs listados por arquivo nas Seções 2 e 7 |

---

## 7. Links das Fontes

### Grupo A — IJCS

| Arquivo | URL da Fonte | DOI |
|---|---|---|
| `Childhood_Obesity.txt` | https://ijcscardiol.org/article/childhood-obesity-and-systemic-arterial-hypertension-in-children-and-adolescents-a-cross-sectional-study/ | — |
| `Coronary_Artery_Disease.txt` | https://ijcscardiol.org/article/inflammatory-and-atherogenic-markers-as-predictors-of-coronary-artery-disease-in-patients-with-suspected-coronary-artery-disease-undergoing-coronary-angiography/ | https://doi.org/10.36660/ijcs.20250039 |
| `Endocarditis.txt` | https://ijcscardiol.org/article/endocarditis-a-27-year-epidemiological-analysis-of-mortality-in-brazil/ | https://doi.org/10.36660/ijcs.20250124 |
| `Obstructive_Sleep_Apnea.txt` | https://ijcscardiol.org/article/obstructive-sleep-apnea-as-a-risk-factor-for-ischemic-heart-disease/ | https://doi.org/10.36660/ijcs.20240250 |
| `Pharmacological_Treatment_for_Heart_Failure.txt` | https://ijcscardiol.org/article/evidence-based-pharmacological-treatment-for-heart-failure-in-brazil/ | https://doi.org/10.36660/ijcs.20250058 |
| **Site do periódico (IJCS)** | https://ijcscardiol.org/ | — |

### Grupo B — Arq Bras Cardiol / SBC

| Arquivo | DOI |
|---|---|
| `2025 Brazilian Evidence-based Guideline on the.txt` | https://doi.org/10.36660/abc.20250621 |
| `Brazilian Atrial Fibrillation Guidelines.txt` | https://doi.org/10.36660/abc.20250618 |
| `Brazilian Guideline for the Evaluation and Diagnosis of Chest.txt` | https://doi.org/10.36660/abc.20250620 |
| `Cardiogenic Shock Due to Inverted-Pattern Takotsubo Syndrome.txt` | https://doi.org/10.36660/abc.20250558 |
| `Cardiovascular Computed Tomography and Magnetic.txt` | https://doi.org/10.36660/abc.20240608 |
| `Guideline for Chronic Coronary Syndrome.txt` | https://doi.org/10.36660/abc.20250619 |
| `Guideline for Perioperative Cardiovascular Evaluation of the.txt` | https://doi.org/10.36660/abc.20240590 |
| `Guidelines on the Diagnosis and Treatment of Hypertrophic.txt` | https://doi.org/10.36660/abc.20240415 |
| `Interstitial Myocardial Fibrosis Analysis by Histology and Cardiac.txt` | https://doi.org/10.36660/abc.20250203 |
| `PRKAG2 Cardiomyopathy A Case-Control Study on the Diagnostic.txt` | https://doi.org/10.36660/abc.20240616 |
| `Position Statement on Cardiometabolic Health Across the.txt` | https://doi.org/10.36660/abc.20250615 |
| `Reference Echocardiographic Values for Cardiac Chambers in Brazil.txt` | https://doi.org/10.36660/abc.20250628 |
| **Site do periódico (ABC/SBC)** | https://abccardiol.org/ |

### Grupo C — JACC / ACC-AHA

| Arquivo | DOI |
|---|---|
| `Guideline for Coronary Artery Revascularization.txt` | https://doi.org/10.1016/j.jacc.2021.09.006 |
| `Guideline for the Diagnosis and Management of Aortic Disease.txt` | https://doi.org/10.1016/j.jacc.2022.08.004 |
| `Guideline for the Diagnosis and Management of Atrial Fibrillation.txt` | https://doi.org/10.1016/j.jacc.2023.08.017 |
| `Guideline for the Evaluation and Diagnosis of Chest Pain.txt` | https://doi.org/10.1016/j.jacc.2021.07.053 |
| `Guideline for the Management of Adults With Congenital Heart Disease.txt` | https://doi.org/10.1016/j.jacc.2025.09.006 |
| `Guideline for the Management of Heart Failure.txt` | https://doi.org/10.1016/j.jacc.2021.12.012 |
| `Guideline for the Management of Hypertrophic Cardiomyopathy.txt` | https://doi.org/10.1016/j.jacc.2024.02.014 |
| `Guideline for the Management of Lower Extremity Peripheral Artery Disease.txt` | https://doi.org/10.1016/j.jacc.2024.02.013 |
| `Guideline for the Management of Patients With Acute Coronary Syndromes.txt` | https://doi.org/10.1016/j.jacc.2024.11.009 |
| **Site ACC** | https://www.acc.org |
| **Site AHA** | https://professional.heart.org |

---
