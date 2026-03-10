# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# CardioIA – Batimentos de Dados

## Nome do grupo

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/in/">Nome do integrante 1</a>
- <a href="https://www.linkedin.com/in/">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/in/">Nome do integrante 3</a>
- <a href="https://www.linkedin.com/in/">Nome do integrante 4</a>
- <a href="https://www.linkedin.com/in/">Nome do integrante 5</a>

## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/in/">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/">Nome do Coordenador</a>


## 📜 Descrição

Este repositório reúne a entrega da **Fase 1 – Capítulo 1** da pós-graduação FIAP, no contexto do projeto **CardioIA** (PBL – *Project Based Learning*).

O objetivo desta fase é atuar como **cientista de dados hospitalar** e construir a base de dados cardiológicos que alimentará todos os módulos de Inteligência Artificial nas próximas sete fases do projeto — incluindo Machine Learning, NLP, Visão Computacional e IoT.

Foram coletados, organizados e documentados **três tipos de dados cardiológicos**:

1. **Dados Numéricos (IoT):** dataset clínico de pacientes cardíacos com variáveis como idade, sexo, pressão arterial, colesterol e frequência cardíaca.
2. **Dados Textuais (NLP):** corpus de artigos científicos e diretrizes cardiológicas de fontes abertas (BVS, SciELO, ACC/AHA), convertidos de PDF para TXT.
3. **Dados Visuais (Visão Computacional):** coleção de imagens de segmentos de batimento cardíaco (ECG), extraídas de dataset público.

Conforme a frase do professor: *"Não estamos apenas coletando dados… estamos construindo as bases de uma cardiologia inteligente que pode salvar vidas."*


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **assets**: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como datasets, imagens e documentos de referência.
  - **assets/dataset_numerico**: dataset numérico clínico (Heart Disease UCI) em formato `.csv`.
  - **assets/dataset_texto**: corpus textual com 26 artigos científicos e diretrizes cardiológicas em formato `.txt`.
  - **assets/dataset_imagens**: amostra local de imagens de segmentos de ECG; o conjunto completo está no Google Drive.
  - **assets/enunciado**: enunciado resumido da atividade.
  - **assets/estrutura_readme**: exemplo de estrutura de README fornecido pela FIAP.

- **src**: scripts auxiliares desenvolvidos para preparação dos dados.

- **README.md**: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🗂️ Parte 1 – Dados Numéricos (IoT)

### Dataset Selecionado

**Heart Disease Dataset – UCI**

- 📦 **Fonte original:** [Kaggle – Heart Disease Dataset UCI](https://www.kaggle.com/datasets/ketangangal/heart-disease-dataset-uci)
- 📂 **Arquivo CSV (link público):** [HeartDiseaseTrain-Test.csv](https://github.com/Hinten/fiap2_fase1_cap1/blob/main/assets/dataset_numerico/HeartDiseaseTrain-Test.csv)
- **Registros:** 303 pacientes
- **Variáveis:** 14 variáveis clínicas
- **Origem:** Dataset real, proveniente do repositório público **UCI Machine Learning Repository**

### Variáveis do Dataset

| Variável   | Descrição                                                              |
|------------|------------------------------------------------------------------------|
| `age`      | Idade do paciente (em anos)                                            |
| `sex`      | Sexo do paciente (1 = masculino, 0 = feminino)                         |
| `cp`       | Tipo de dor no peito (0–3)                                             |
| `trestbps` | Pressão arterial em repouso (mmHg)                                     |
| `chol`     | Colesterol sérico (mg/dl)                                              |
| `fbs`      | Glicose em jejum > 120 mg/dl (1 = verdadeiro, 0 = falso)              |
| `restecg`  | Resultado do eletrocardiograma em repouso (0–2)                        |
| `thalach`  | Frequência cardíaca máxima atingida (bpm)                              |
| `exang`    | Angina induzida por exercício (1 = sim, 0 = não)                       |
| `oldpeak`  | Depressão do segmento ST induzida por exercício                        |
| `slope`    | Inclinação do segmento ST de pico do exercício (0–2)                   |
| `ca`       | Número de vasos sanguíneos principais coloridos por fluoroscopia (0–3) |
| `thal`     | Tipo de defeito cardíaco (1 = normal, 2 = fixo, 3 = reversível)        |
| `target`   | Presença de doença cardíaca (1 = doente, 0 = saudável)                 |

### Variáveis Clinicamente Mais Relevantes

| Variável | Importância clínica para IA |
|---|---|
| `age` | Fator de risco primário; risco cardiovascular aumenta significativamente com o envelhecimento |
| `chol` | Níveis elevados favorecem aterosclerose — indicador essencial de risco de infarto |
| `trestbps` | Hipertensão é o principal fator de risco para doenças cardíacas |
| `thalach` | Capacidade funcional do coração; indicador de resposta ao estresse fisiológico |
| `cp` | Principal sintoma de alerta clínico para angina instável e infarto |

### Relação com IoT e Monitoramento

Embora coletado em ambiente clínico controlado, as variáveis do dataset espelham dados que podem ser obtidos por dispositivos IoT na saúde (smartwatches, monitores cardíacos portáteis, medidores digitais de pressão arterial), representando um **cenário simulado de coleta em ecossistema hospitalar inteligente**.


## 📄 Parte 2 – Dados Textuais (NLP)

### Corpus Selecionado

O corpus textual reúne **26 documentos** de acesso aberto agrupados em três fontes:

| Grupo | Fonte | Periódico / Organização | Nº de arquivos |
|---|---|---|---|
| **A** | BVS / SciELO | *International Journal of Cardiovascular Sciences* (IJCS) | 5 |
| **B** | BVS / SciELO | *Arquivos Brasileiros de Cardiologia* (Arq Bras Cardiol / ABC) — Sociedade Brasileira de Cardiologia (SBC) | 12 |
| **C** | acc.org / heart.org | Diretrizes ACC/AHA — *Journal of the American College of Cardiology* (JACC) | 9 |

Os grupos A e B atendem diretamente ao critério de fonte **BVS/SciELO** do enunciado. O grupo C representa literatura de referência internacional amplamente empregada na prática clínica cardiológica brasileira.

Os arquivos estão disponíveis na pasta [`assets/dataset_texto/`](./assets/dataset_texto/).

### Conversão de PDF para TXT

> **Nota:** Os datasets textuais foram originalmente obtidos em formato PDF. Para viabilizar a entrega e o processamento por modelos de NLP, todos os arquivos foram convertidos para formato `.txt` utilizando o script [`src/convert_pdf_to_txt.py`](./src/convert_pdf_to_txt.py).

O script utiliza a biblioteca **PyPDF2** para iterar sobre todos os arquivos `.pdf` presentes em `assets/dataset_texto/` e gerar os correspondentes `.txt` com o mesmo nome. Para executar a conversão:

```bash
python src/convert_pdf_to_txt.py
```

### Como os textos podem ser usados por NLP

Os textos selecionados cobrem temas como doenças arteriais coronarianas, insuficiência cardíaca, arritmias, obesidade e diretrizes clínicas, habilitando diversas aplicações de NLP:

| Aplicação NLP | Descrição |
|---|---|
| **Reconhecimento de Entidades (NER)** | Extração automática de nomes de doenças, medicamentos, exames, biomarcadores e sintomas |
| **Análise de Sentimentos Clínicos** | Identificação de polaridade em relatos de sintomas e prognósticos |
| **Extração de Sintomas** | Mapeamento de sintomas cardíacos (dor no peito, dispneia, palpitações) a diagnósticos |
| **Classificação de Tópicos** | Categorização automática de documentos por condição clínica ou especialidade |
| **Extração de Recomendações** | Parsing estruturado de diretrizes (grau de evidência, classe de recomendação) |
| **Sumarização Automática** | Geração de resumos de artigos científicos longos |

### Importância para IA na Saúde

O uso de NLP em saúde cardiovascular permite:
- Auxiliar o profissional de saúde na triagem rápida de literatura científica;
- Extrair informações estruturadas de prontuários e laudos em linguagem livre;
- Detectar padrões de risco em descrições clínicas antes de exames laboratoriais.

A diversidade de fontes (BVS, SciELO, ACC/AHA, SUS/DATASUS) garante cobertura de vocabulário clínico brasileiro e internacional, enriquecendo o treinamento de modelos de linguagem para o domínio cardiovascular.


## 🖼️ Parte 3 – Dados Visuais (Visão Computacional)

### Dataset Selecionado

**ECG Images – Segmentos de Batimento Cardíaco**

- 📦 **Fonte original:** [Kaggle – ECG Images](https://www.kaggle.com/datasets/analiviafr/ecg-images)
- 🔗 **Link público com 100+ imagens:** [Google Drive](https://drive.google.com/drive/u/1/folders/1cN4qdgAq8gQM1BwV_S7LcYx4RL-UHw7j)
- **Tipo de dado:** Segmentos individuais de batimento cardíaco (*single-beat ECG segments*)
- **Formato:** `.jpg` / `.png`
- **Quantidade:** 100+ imagens
- **Origem:** Dataset público com fins educacionais e de pesquisa

Uma amostra representativa está disponível em [`assets/dataset_imagens/exemplo/`](./assets/dataset_imagens/exemplo/). O dataset completo ultrapassa o limite razoável para versionamento em Git e está hospedado no Google Drive acima.

> **Nota sobre o dataset:** As imagens representam batimentos individuais isolados — janelas de sinal cardíaco recortadas ao redor do complexo QRS — e não ECGs completos de 12 derivações. Essa característica as torna especialmente adequadas para tarefas de classificação morfológica por batimento e detecção de anomalias em nível unitário.

### Como a Visão Computacional analisa esses dados

#### 1. Pré-processamento e segmentação do traçado
Técnicas como binarização por limiarização (*thresholding*), filtros de Canny e operações morfológicas (erosão e dilatação) isolam o traçado cardíaco do fundo da imagem e eliminam ruídos.

#### 2. Extração de características morfológicas
- Altura e largura do pico dominante (amplitude e duração do QRS)
- Polaridade do batimento (deflexão positiva ou negativa)
- Presença de entalhes ou bifurcações no complexo (indicativos de bloqueios de ramo)
- Simetria da curva em relação ao eixo temporal

#### 3. Classificação com Deep Learning

| Morfologia visual | Condição associada |
|---|---|
| Deflexão dominante negativa, QRS largo | Possível bloqueio de ramo esquerdo |
| QRS estreito e simétrico | Batimento sinusal normal |
| Complexo bifásico ou entalhado | Arritmia supraventricular |
| Amplitude muito elevada | Hipertrofia ventricular |
| Batimento de morfologia aberrante isolado | Extrassístole ventricular (PVC) |

Arquiteturas como **ResNet**, **EfficientNet** e **MobileNet** conseguem aprender, diretamente dos pixels, os padrões que diferenciam batimentos normais de patológicos.

#### 4. Detecção de anomalias não supervisionada
**Autoencoders Convolucionais** treinados apenas com batimentos normais funcionam como detectores de patologia sem necessidade de rótulos — especialmente úteis quando dados patológicos rotulados são escassos.

### Por que isso é relevante para IA na Saúde

| Desafio real | Como a Visão Computacional responde |
|---|---|
| Volume massivo de batimentos para revisar | Triagem automática em tempo real |
| Escassez de especialistas em cardiologia | Modelos embarcados em dispositivos de monitoramento |
| Variabilidade inter-observador na leitura | Padronização e reprodutibilidade da análise |
| Detecção tardia de arritmias graves | Alertas automáticos em monitores cardíacos |
| Dados rotulados escassos | Aproveitamento de técnicas semi e não supervisionadas |


## 🔧 Como executar o código

### Pré-requisitos

- Python 3.8+
- Biblioteca `PyPDF2`

### Instalação

```bash
pip install PyPDF2
```

### Conversão de PDFs para TXT

Para converter os arquivos PDF do dataset textual para formato `.txt`:

```bash
python src/convert_pdf_to_txt.py
```

O script buscará automaticamente todos os arquivos `.pdf` em `assets/dataset_texto/` e gerará os arquivos `.txt` correspondentes na mesma pasta.


## 🗃 Histórico de lançamentos

* 0.1.0 - 10/03/2026
    * Entrega inicial: dataset numérico, corpus textual (26 documentos) e dataset de imagens ECG organizados e documentados.


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
