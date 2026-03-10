# 🫀 Dataset Numérico – Heart Disease UCI | CardioIA

> Repositório criado para a disciplina de Inteligência Artificial Aplicada à Saúde.  
> Contém a documentação e organização do dataset numérico clínico utilizado para o desenvolvimento de modelos de Machine Learning na área cardiovascular.

---

## 1. Objetivo da Etapa

Nesta primeira etapa do projeto **CardioIA – Batimentos de Dados**, o objetivo é coletar e organizar um conjunto de dados numéricos relacionados à saúde cardiovascular.

Esses dados servirão como base para o desenvolvimento de futuros módulos de Inteligência Artificial do projeto, como:

- sistemas de triagem automática
- previsão de doenças cardíacas
- análise de risco clínico
- monitoramento remoto de pacientes

Além disso, esta etapa busca introduzir conceitos iniciais de **Governança de Dados**, organização de datasets e preparação de dados para aplicações em Machine Learning.

---

## 2. Dataset Selecionado

O dataset utilizado é:

**Heart Disease Dataset – UCI**

📦 Fonte original: [https://www.kaggle.com/datasets/ketangangal/heart-disease-dataset-uci](https://www.kaggle.com/datasets/ketangangal/heart-disease-dataset-uci)

📂 Arquivo CSV (link público): [HeartDiseaseTrain-Test.csv](https://github.com/Hinten/fiap2_fase1_cap1/blob/main/assets/dataset_numerico/HeartDiseaseTrain-Test.csv)

Este dataset contém informações clínicas de pacientes utilizadas para prever a presença de doenças cardíacas. Ele é amplamente utilizado em pesquisas acadêmicas e projetos de ciência de dados na área da saúde, sendo originalmente proveniente do repositório público da **UCI Machine Learning Repository**.

---

## 3. Estrutura do Dataset

O conjunto de dados possui aproximadamente:

- **303 registros** (pacientes)
- **14 variáveis clínicas**

Cada linha representa um paciente e suas características médicas coletadas em ambiente clínico.

Exemplo simplificado da estrutura:

| age | sex | cp | trestbps | chol | thalach | exang | target |
|-----|-----|----|----------|------|---------|-------|--------|
| 63  | 1   | 3  | 145      | 233  | 150     | 0     | 1      |
| 37  | 1   | 2  | 130      | 250  | 187     | 0     | 1      |
| 41  | 0   | 1  | 130      | 204  | 172     | 0     | 1      |

Onde cada registro representa um paciente avaliado clinicamente.

---

## 4. Variáveis Principais do Dataset

A seguir estão as variáveis presentes no dataset e suas respectivas descrições:

| Variável   | Descrição                                                   |
|------------|-------------------------------------------------------------|
| `age`      | Idade do paciente (em anos)                                 |
| `sex`      | Sexo do paciente (1 = masculino, 0 = feminino)              |
| `cp`       | Tipo de dor no peito (0–3)                                  |
| `trestbps` | Pressão arterial em repouso (mmHg)                          |
| `chol`     | Colesterol sérico (mg/dl)                                   |
| `fbs`      | Glicose em jejum > 120 mg/dl (1 = verdadeiro, 0 = falso)   |
| `restecg`  | Resultado do eletrocardiograma em repouso (0–2)             |
| `thalach`  | Frequência cardíaca máxima atingida (bpm)                   |
| `exang`    | Angina induzida por exercício (1 = sim, 0 = não)            |
| `oldpeak`  | Depressão do segmento ST induzida por exercício             |
| `slope`    | Inclinação do segmento ST de pico do exercício (0–2)        |
| `ca`       | Número de vasos sanguíneos principais coloridos por fluoroscopia (0–3) |
| `thal`     | Tipo de defeito cardíaco (1 = normal, 2 = fixo, 3 = reversível) |
| `target`   | Presença de doença cardíaca (1 = doente, 0 = saudável)     |

---

## 5. Variáveis Clinicamente Mais Relevantes

Algumas variáveis possuem maior importância clínica e podem ser especialmente úteis para modelos de Inteligência Artificial.

### 🔹 Idade (`age`)
A idade é um dos fatores de risco mais relevantes para doenças cardiovasculares. O risco de problemas cardíacos aumenta significativamente com o envelhecimento, tornando essa variável essencial para qualquer modelo preditivo na área.

### 🔹 Colesterol (`chol`)
Níveis elevados de colesterol podem levar ao acúmulo de placas nas artérias, processo conhecido como **aterosclerose**, aumentando o risco de infarto e outras doenças cardiovasculares.

### 🔹 Pressão Arterial em Repouso (`trestbps`)
A hipertensão é um dos principais fatores de risco para doenças cardíacas, podendo causar danos progressivos ao sistema cardiovascular ao longo do tempo.

### 🔹 Frequência Cardíaca Máxima (`thalach`)
A frequência cardíaca máxima atingida durante esforço físico pode indicar a capacidade do coração de responder ao estresse fisiológico, sendo um indicador funcional importante.

### 🔹 Tipo de Dor no Peito (`cp`)
A dor no peito é um dos principais sintomas relacionados a doenças cardíacas, podendo indicar condições como angina instável ou infarto agudo do miocárdio.

---

## 6. Relação com IoT e Monitoramento de Pacientes

Embora o dataset tenha sido coletado em ambiente clínico controlado, as variáveis presentes podem ser facilmente associadas a dados coletados por dispositivos **IoT na área da saúde**, como:

- smartwatches e wearables
- monitores cardíacos portáteis
- dispositivos digitais de pressão arterial
- sensores hospitalares integrados
- sistemas de telemedicina

| Variável do Dataset      | Possível Origem IoT                          |
|--------------------------|----------------------------------------------|
| Frequência cardíaca      | Smartwatch ou monitor cardíaco               |
| Pressão arterial         | Medidor digital conectado                    |
| Sintomas (dor no peito)  | Aplicativo de monitoramento do paciente      |
| ECG / Segmento ST        | Sensores cardíacos vestíveis                 |

Dessa forma, o dataset pode representar um **cenário simulado de coleta de dados em um ecossistema hospitalar inteligente**, servindo de base para modelos que futuramente operarão com dados em tempo real.

O arquivo `.csv` do dataset está disponível publicamente no repositório GitHub, conforme link indicado na seção 2.