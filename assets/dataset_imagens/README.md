# 🫀 Dataset de Segmentos de Batimento Cardíaco para Visão Computacional

> Repositório criado para a disciplina de Inteligência Artificial Aplicada à Saúde.  
> Contém uma curadoria de imagens de segmentos individuais de batimento cardíaco extraídos de sinais de ECG, para uso em projetos de Visão Computacional.

---

## 📁 Imagens do Dataset

> 🔗 **[Acesse as 100+ imagens hospedadas aqui → https://drive.google.com/drive/u/1/folders/1cN4qdgAq8gQM1BwV_S7LcYx4RL-UHw7j]()**

As imagens foram selecionadas a partir do dataset público **ECG Images**, disponível no Kaggle:  
📦 [https://www.kaggle.com/datasets/analiviafr/ecg-images](https://www.kaggle.com/datasets/analiviafr/ecg-images)

- **Tipo de dado:** Segmentos individuais de batimento cardíaco (single-beat ECG segments)
- **Formato:**  `.png`
- **Quantidade:** 100+ imagens
- **Origem:** Dataset público com fins educacionais e de pesquisa

> **Nota sobre o dataset:** As imagens representam batimentos individuais isolados — janelas de sinal cardíaco recortadas ao redor do complexo QRS — e não ECGs completos de 12 derivações. Essa característica torna o dataset especialmente adequado para tarefas de classificação morfológica por batimento e detecção de anomalias em nível unitário.

---

## 🧠 Justificativa: Por que segmentos de batimento cardíaco são valiosos para Visão Computacional?

### O que são esses dados e por que importam

Cada imagem neste dataset representa um único batimento cardíaco extraído de um sinal de ECG e convertido em representação visual. Essa abordagem — tratar cada batimento como uma imagem independente — é amplamente utilizada em pesquisa de IA cardiológica porque permite construir grandes volumes de dados rotulados a partir de gravações relativamente curtas.

O traçado de cada batimento contém informação morfológica rica: a forma, amplitude e duração do complexo QRS, a presença ou ausência de ondas satélites, e padrões de inversão ou deformação que caracterizam condições patológicas específicas. Algoritmos de Visão Computacional são capazes de aprender e generalizar esses padrões com alta precisão.

---

### Como algoritmos de Visão Computacional analisam esses segmentos

#### 1. 🔍 Pré-processamento e segmentação do traçado

O primeiro desafio é isolar o traçado cardíaco do fundo da imagem. Técnicas como **binarização por limiarização (thresholding)**, **filtros de Canny** para detecção de bordas e **operações morfológicas** (erosão e dilatação) limpam ruídos e preparam a imagem para análise. Como as imagens já vêm recortadas por batimento, esse passo é significativamente simplificado em relação a ECGs completos.

#### 2. 📈 Extração de características morfológicas

Após o pré-processamento, é possível extrair automaticamente características visuais como:

- **Altura e largura do pico dominante** (amplitude e duração do QRS)
- **Polaridade do batimento** — se a deflexão principal é positiva ou negativa (padrão vs. invertido)
- **Presença de entalhes ou bifurcações** no complexo, indicativos de bloqueios de ramo
- **Simetria da curva** em relação ao eixo temporal

Essas características podem ser extraídas tanto por métodos clássicos (descritores HOG, momentos de Hu) quanto aprendidas automaticamente por redes convolucionais.

#### 3. 🧩 Classificação morfológica com Deep Learning

Redes Neurais Convolucionais (CNNs) são a abordagem estado-da-arte para classificação de batimentos individuais a partir de imagens. Arquiteturas como **ResNet**, **EfficientNet** e **MobileNet** conseguem aprender, diretamente dos pixels, os padrões que diferenciam batimentos normais de patológicos:

| Morfologia visual | Condição associada |
|---|---|
| Deflexão dominante negativa, QRS largo | Possível bloqueio de ramo esquerdo |
| QRS estreito e simétrico | Batimento sinusal normal |
| Complexo bifásico ou entalhado | Arritmia supraventricular |
| Amplitude muito elevada | Hipertrofia ventricular |
| Batimento de morfologia aberrante isolado | Extrassístole ventricular (PVC) |

#### 4. 🚨 Detecção de anomalias não supervisionada

**Autoencoders Convolucionais** treinados apenas com batimentos normais aprendem a reconstruir padrões saudáveis. Quando um batimento anômalo é apresentado, o erro de reconstrução é elevado — funcionando como um detector de patologia sem necessidade de rótulos. Isso é especialmente útil quando dados patológicos rotulados são escassos.

#### 5. 🔄 Data augmentation e generalização

Imagens de batimentos individuais são naturalmente compatíveis com técnicas de **aumento de dados** (rotação leve, escalonamento, adição de ruído gaussiano), o que amplia artificialmente o volume de treinamento e melhora a robustez dos modelos. Essa característica torna datasets como este particularmente valiosos mesmo com volume limitado.

---

### Por que isso é relevante para projetos de IA na Saúde?

| Desafio real | Como a Visão Computacional responde |
|---|---|
| Volume massivo de batimentos para revisar | Triagem automática em tempo real |
| Escassez de especialistas em cardiologia | Modelos embarcados em dispositivos de monitoramento |
| Variabilidade inter-observador na leitura | Padronização e reprodutibilidade da análise |
| Detecção tardia de arritmias graves | Alertas automáticos em monitores cardíacos |
| Dados rotulados escassos | Aproveitamento de técnicas semi e não supervisionadas |

Classificadores de batimento individual são o bloco fundamental de sistemas maiores de análise de ECG. Um modelo que identifica corretamente cada batimento pode ser combinado com análise de sequência temporal para detectar arritmias complexas — tornando este tipo de dataset um ponto de entrada essencial para qualquer pipeline de IA cardiológica.

---

### Limitações e considerações éticas

Os modelos desenvolvidos com este dataset atuam como ferramentas de **apoio à decisão clínica** (*Clinical Decision Support Systems* — CDSS) e não substituem a avaliação médica. Limitações importantes incluem:

- As imagens representam uma única derivação, sem contexto de 12 derivações
- A generalização entre equipamentos e populações diferentes exige validação cuidadosa
- O desempenho do modelo depende diretamente da qualidade e diversidade dos rótulos fornecidos


*Projeto acadêmico — uso educacional. As imagens utilizadas são de domínio público ou licenciadas para pesquisa.*
