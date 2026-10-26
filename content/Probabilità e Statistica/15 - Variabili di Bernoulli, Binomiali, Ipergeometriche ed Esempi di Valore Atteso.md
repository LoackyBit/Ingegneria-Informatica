---
status: permanent
type: lecture
area: education
related: ["[[Probabilità e Statistica MOC]]", "[[Ingegneria Informatica 2026 - 27 MOC]]", "[[University]]", "[[Metodo di Studio - PACRAR]]", "[[01 - Teoria degli Insiemi, Spazio Campionario e Prime Nozioni di Probabilità]]", "[[02 - Insieme delle Parti, Assiomi della Probabilità e Spazi Finiti]]", "[[13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica]]", "[[03 - Funzioni (Parte I)]]", "[[04 - Funzioni (Parte II)]]", "[[06 - Valore Assoluto, Numeri Naturali e Principio di Induzione]]"]
aliases: ["Lezione 15 Probabilità e Statistica", "PeS Lezione 15", "Variabili di Bernoulli, Binomiali e Ipergeometriche", "Calcolo del Valore Atteso ed Equità del Gioco", "15 - Variabili di Bernoulli e Binomiali"]
source: Lezione 15 Probabilità e Statistica del 26/10/2026 - Prof.ssa Giovanna Nappo, Prof. Fabio Spizzichino
title: "15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso"
date: '2026-10-26'
updated: 2026-10-26T18:25
tags: [education/university, education/math, math/probability, math/statistics]
summary: "Variabili aleatorie di Bernoulli, binomiali e ipergeometriche, con modelli di estrazione senza reinserimento, calcolo del valore atteso ed equità del gioco."
course: "Probabilità e Statistica"
sources: ["[[Tipologie di variabili.pdf]]", "[[Dispense Statistica e Probabilità.pdf]]", "[[Calcolo delle Probabilità.pdf]]"]
---
[[Home MOC|Home]] / [[University|University MOC]] / [[Probabilità e Statistica MOC]] / [[15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso]]

# 15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso

- **Docenti:** Prof.ssa Giovanna Nappo, Prof. Fabio Spizzichino
- **Data Lezione:** 2026-10-26
- **Materiali Didattici Ufficiali:**
  - \[[[Tipologie di variabili.pdf#page=1|Appunti Completi d'Aula — Tipologie di Variabili (pp. 1–4)]]]
  - \[[[Dispense Statistica e Probabilità.pdf#page=75|Capitolo 6 — Probabilità binomiali e ipergeometriche; estrazioni casuali da urne di composizione nota (pp. 68–79)]]]
  - \[[[Dispense Statistica e Probabilità.pdf#page=118|Capitolo 9 — Valore atteso di una variabile aleatoria e relative proprietà (pp. 111–125)]]]
  - \[[[Calcolo delle Probabilità.pdf#page=161|Sheldon Ross — Capitolo 4.3: Valore Atteso (pp. 142–145)]]]
  - \[[[Calcolo delle Probabilità.pdf#page=170|Sheldon Ross — Capitolo 4.6: Le Variabili Aleatorie di Bernoulli e Binomiali (pp. 151–160)]]]
  - \[[[Calcolo delle Probabilità.pdf#page=198|Sheldon Ross — Capitolo 4.8.3: La Variabile Aleatoria Ipergeometrica (pp. 179–182)]]]
- **Riferimento MOC:** [[Probabilità e Statistica MOC]], [[Ingegneria Informatica 2026 - 27 MOC]]
- **Lezioni Precedenti:** [[01 - Teoria degli Insiemi, Spazio Campionario e Prime Nozioni di Probabilità]], [[02 - Insieme delle Parti, Assiomi della Probabilità e Spazi Finiti]], [[13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica]]
- **Collegamenti Interdisciplinari:** [[03 - Funzioni (Parte I)]] e [[04 - Funzioni (Parte II)]] (proprietà formali delle funzioni indicatrici e composizione di mappe aleatorie), [[06 - Valore Assoluto, Numeri Naturali e Principio di Induzione]] (successioni di prove indipendenti, combinatoria binomiale e proprietà di convergenza)

La quindicesima lezione di Elementi di Calcolo delle Probabilità e Statistica si apre con la conclusione della correzione del Foglio di Esercizi III (incentrato su probabilità condizionata, formula di Bayes e indipendenza stocastica) e prosegue con la caratterizzazione formale delle principali famiglie parametriche di <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>variabili aleatorie discrete</b></font></mark>. Nei contesti ingegneristici e informatici, la modellizzazione dei processi stocastici richiede schemi ricorrenti per quantificare successi e fallimenti, sia in prove ripetute e indipendenti (con reinserimento), sia in campionamenti esaustivi da popolazioni finite bipartite (senza reinserimento).

La trattazione consolida la distinzione tra la variabile elementare di Bernoulli e l'estensione a prove multiple fornita dalla <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>variabile binomiale</b></font></mark>, per poi introdurre la <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>variabile ipergeometrica</b></font></mark> attraverso esempi guidati di biologia computazionale e modelli di urne bicolori. Nella seconda parte, l'operatore di <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>valore atteso</b></font></mark> viene applicato allo studio dell'equità nei giochi d'azzardo e all'analisi di scenari con vincita geometrica/esponenziale, illustrando la divergenza asintotica del payoff atteso a fronte di una probabilità di vincita infinitesima.

---

## 1. Variabile di Bernoulli: La Prova Binaria Elementare

### Fondamenti e Definizione Formale
L'unità atomica di tutti i processi aleatori discreti a due esiti è costituita dalla prova dicotomica o esperimento bernoulliano \[[[Dispense Statistica e Probabilità.pdf#page=75|Dispense p. 68]]], \[[[Calcolo delle Probabilità.pdf#page=170|Ross p. 151]]].

> [!danger] Definizione: Variabile Aleatoria di Bernoulli
> Una variabile aleatoria reale $X: \Omega \to \mathbb{R}$ si dice **variabile di Bernoulli** di parametro $p \in [0, 1]$, indicata con la notazione:
> $$X \sim Be(p)$$
> se assume esclusivamente valori nell'insieme binario $\{0, 1\}$ con distribuzione di probabilità (funzione di massa):
> $$\begin{cases} \mathbb{P}(X = 1) = p \\ \mathbb{P}(X = 0) = 1 - p = q \end{cases}$$
> - **Convenzione operativa:** L'esito $X = 1$ identifica convenzionalmente il "successo", mentre $X = 0$ identifica il "fallimento".

> [!tip]- Flashcard: Definizione di Variabile di Bernoulli
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Basic
Front: Come viene definita formalmente una variabile aleatoria di Bernoulli $X \sim Be(p)$ e qual è la sua funzione di massa?
Back: Una variabile di Bernoulli $X \sim Be(p)$ assume valori nel codominio binario $\{0, 1\}$ con parametro $p \in [0, 1]$. La sua funzione di massa assegna probabilità $\mathbb{P}(X=1) = p$ (successo) e $\mathbb{P}(X=0) = 1 - p$ (fallimento).
Tags: education/university education/math math/probability
END
%%

### Rappresentazione Mediante Funzione Indicatrice
Il legame strutturale tra eventi insiemistici e variabili numeriche (approfondito in [[13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica]]) è mediato dalla <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>funzione indicatrice</b></font></mark> di un evento \[[[Dispense Statistica e Probabilità.pdf#page=75|Dispense p. 68]]]:
- Per qualunque evento $A \subseteq \Omega$ nello spazio di probabilità $(\Omega, \mathcal{F}, \mathbb{P})$, la funzione indicatrice $\mathbb{1}_A: \Omega \to \{0, 1\}$ definita da:
  $$\mathbb{1}_A(\omega) = \begin{cases} 1 & \text{se } \omega \in A \\ 0 & \text{se } \omega \notin A \end{cases}$$
  è una variabile di Bernoulli di parametro $p = \mathbb{P}(A)$:
  $$X = \mathbb{1}_A \sim Be(p)$$

> [!summary] Proprietà: Valore Atteso e Varianza di Bernoulli
> Data $X \sim Be(p)$, i momenti primo e secondo e la varianza sono dati da:
> - **Valore atteso:** $\mathbb{E}[X] = 0 \cdot (1 - p) + 1 \cdot p = p$
> - **Momento secondo:** $\mathbb{E}[X^2] = 0^2 \cdot (1 - p) + 1^2 \cdot p = p$
> - **Varianza:** $\operatorname{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = p - p^2 = p(1 - p)$

> [!tip]- Flashcard: Valore Atteso e Varianza di Bernoulli
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Cloze
Text: Data una variabile di Bernoulli $X \sim Be(p)$, il suo valore atteso è {{c1::$\mathbb{E}[X] = p$}} e la sua varianza è {{c2::$\operatorname{Var}(X) = p(1-p)$}}.
Extra: La varianza assume il suo valore massimo pari a $1/4$ nel caso di massima incertezza, ossia per $p = 1/2$.
Tags: education/university education/math math/probability
END
%%

> [!example] Esempio: Lancio di una Moneta Equilibrata
> - Spazio campionario: $\Omega = \{T, C\}$ con esiti equiprobabili.
> - Variabile: $X(T) = 1$ e $X(C) = 0$.
> - Allora $X \sim Be(1/2)$ con $\mathbb{E}[X] = 1/2$ e $\operatorname{Var}(X) = 1/4$ \[[[Tipologie di variabili.pdf#page=1|Appunti p. 1]]].

---

## 2. Variabile Binomiale: Prove Ripetute e Indipendenti

### Formalizzazione del Modello Binomiale
Quando un esperimento bernoulliano elementare viene replicato un numero fissato $n$ di volte in condizioni di <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>indipendenza stocastica</b></font></mark> e con probabilità di successo $p$ costante (schema delle prove bernoulliane ripetute), l'interesse computazionale si concentra sul conteggio complessivo dei successi ottenuti \[[[Calcolo delle Probabilità.pdf#page=170|Ross p. 151]]].

> [!danger] Definizione: Variabile Aleatoria Binomiale
> Una variabile aleatoria discreta $S_n: \Omega \to \mathbb{R}$ si dice **binomiale** di parametri $n \in \mathbb{N}^+$ e $p \in [0, 1]$, indicata con la notazione:
> $$S_n \sim Bi(n, p) \quad \text{oppure} \quad S_n \sim B(n, p)$$
> se assume valori nell'insieme discreto $\{0, 1, \dots, n\}$ con funzione di densità discreta (PMF):
> $$\mathbb{P}(S_n = j) = \binom{n}{j} p^j (1 - p)^{n - j}, \quad j \in \{0, 1, \dots, n\}$$
> dove:
> - $n$ rappresenta la lunghezza della sequenza (numero totale di prove indipendenti);
> - $p$ è la probabilità di successo in ciascuna singola prova;
> - $\binom{n}{j} = \frac{n!}{j!(n - j)!}$ è il coefficiente binomiale, pari al numero di configurazioni distinte in cui possono presentarsi $j$ successi su $n$ posizioni.

> [!tip]- Flashcard: PMF della Variabile Binomiale
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Cloze
Text: La densità di probabilità discreta di una variabile binomiale $S_n \sim Bi(n, p)$ per $j \in \{0, 1, \dots, n\}$ è data da {{c1::$\mathbb{P}(S_n = j) = \binom{n}{j} p^j (1-p)^{n-j}$}}.
Extra: Il coefficiente binomiale conta il numero di sequenze ordinate contenenti esattamente $j$ successi e $n-j$ fallimenti, ciascuna avente probabilità elementare pari a $p^j (1-p)^{n-j}$.
Tags: education/university education/math math/probability
END
%%

### Rappresentazione Come Somma di Indicatrici e Momenti
La struttura algebrica della variabile binomiale emerge direttamente dalla scomposizione in variabili bernoulliane indipendenti \[[[Dispense Statistica e Probabilità.pdf#page=75|Dispense p. 69]]]:

> [!summary] Proposizione: Decomposizione in Indicatrici, Media e Varianza
> Sia $S_n \sim Bi(n, p)$. Allora $S_n$ è rappresentabile come somma di $n$ variabili di Bernoulli indipendenti e identicamente distribuite ($X_i \overset{\text{iid}}{\sim} Be(p)$):
> $$S_n = \sum_{i=1}^n X_i, \quad X_i = \mathbb{1}_{A_i}$$
> dove $A_i$ è l'evento "successo all'i-esima prova". Ne conseguono immediatamente:
> - **Valore atteso (per linearità):**
>   $$\mathbb{E}[S_n] = \mathbb{E}\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n \mathbb{E}[X_i] = \sum_{i=1}^n p = n p$$
> - **Varianza (per indipendenza):**
>   $$\operatorname{Var}(S_n) = \sum_{i=1}^n \operatorname{Var}(X_i) = \sum_{i=1}^n p(1 - p) = n p (1 - p)$$

> [!abstract]- Dimostrazione Formale Passo-Passo: Normalizzazione della PMF Binomiale
> Per dimostrare che $\sum_{j=0}^n \mathbb{P}(S_n = j) = 1$, si applica il teorema dello sviluppo binomiale di Newton:
> $$\sum_{j=0}^n \binom{n}{j} p^j (1 - p)^{n - j} = (p + (1 - p))^n = (1)^n = 1$$
> La somma su tutti i valori del supporto discreto ricostruisce esattamente la misura dello spazio campionario $\Omega$.

> [!tip]- Flashcard: Media e Varianza della Distribuzione Binomiale
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Basic
Front: Come si calcolano il valore atteso e la varianza di una variabile binomiale $S_n \sim Bi(n, p)$ sfruttando la decomposizione in prove bernoulliane?
Back: Decomponendo $S_n = \sum_{i=1}^n X_i$ con $X_i \overset{\text{iid}}{\sim} Be(p)$:
1. Per linearità del valore atteso: $\mathbb{E}[S_n] = \sum_{i=1}^n \mathbb{E}[X_i] = n p$.
2. Per l'indipendenza delle prove, la varianza della somma è la somma delle varianze: $\operatorname{Var}(S_n) = \sum_{i=1}^n \operatorname{Var}(X_i) = n p (1 - p)$.
Tags: education/university education/math math/probability
END
%%

### Esempio d'Aula: Lanci Multipli di una Moneta
Si consideri il lancio ripetuto di una moneta per $n = 3$ volte, con probabilità di successo (testa) $p = 1/2$.
Sia $S_3$ il numero totale di teste ottenute su 3 lanci: $S_3 \sim Bi(3, 1/2)$ \[[[Tipologie di variabili.pdf#page=1|Appunti p. 1]]].

> [!example] Calcolo Operativo: Probabilità di Ottenere Almeno Due Teste
> Si vuole determinare la probabilità dell'evento $\{S_3 \ge 2\}$:
> - Essendo gli eventi $\{S_3 = 2\}$ e $\{S_3 = 3\}$ disgiunti:
>   $$\mathbb{P}(S_3 \ge 2) = \mathbb{P}(S_3 = 2) + \mathbb{P}(S_3 = 3)$$
> - Applicando la densità binomiale:
>   $$\mathbb{P}(S_3 = 2) = \binom{3}{2}\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^{3 - 2} = 3 \cdot \frac{1}{4} \cdot \frac{1}{2} = \frac{3}{8}$$
>   $$\mathbb{P}(S_3 = 3) = \binom{3}{3}\left(\frac{1}{2}\right)^3\left(\frac{1}{2}\right)^0 = 1 \cdot \frac{1}{8} \cdot 1 = \frac{1}{8}$$
> - Sommando i contributi:
>   $$\mathbb{P}(S_3 \ge 2) = \frac{3}{8} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2}$$

---

## 3. Variabile Ipergeometrica: Estrazioni Senza Reinserimento

### Motivazione Didattica: L'Esempio del Lago
A differenza dello schema binomiale (in cui le prove sono indipendenti e la probabilità $p$ resta costante grazie al reinserimento o all'infinità della sorgente), nei campionamenti da popolazioni finite senza reinserimento l'estrazione di un elemento altera la composizione della popolazione residua, introducendo una <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>dipendenza stocastica</b></font></mark> tra le prove successive \[[[Dispense Statistica e Probabilità.pdf#page=79|Dispense p. 72]]], \[[[Calcolo delle Probabilità.pdf#page=198|Ross p. 179]]].

L'esempio guida introdotto dal docente illustra la genesi combinatoria del modello \[[[Tipologie di variabili.pdf#page=2|Appunti p. 2]]]:
- **Scenario:** Un lago contiene una popolazione complessiva di 150 pesci, suddivisi in $m_1 = 100$ salmoni e $m_2 = 50$ orate.
- **Esperimento:** Una rete da pesca preleva simultaneamente (o in sequenza senza reinserimento) un campione casuale di $n = 30$ pesci.
- **Obiettivo:** Determinare la probabilità di catturare esattamente 20 salmoni (e conseguentemente 10 orate), ossia l'evento $E = \{20 \text{ salmoni}, 10 \text{ orate}\}$.

```
Popolazione Totale N = 150
┌──────────────────────────────┬──────────────────────────────┐
│     m1 = 100 Salmoni         │       m2 = 50 Orate          │
└──────────────┬───────────────┴──────────────┬───────────────┘
               │                              │
               ▼                              ▼
      Estrai k = 20 salmoni          Estrai n - k = 10 orate
               │                              │
               └──────────────┬───────────────┘
                              ▼
                Campione Pescato: n = 30 pesci
```

1. **Ordinamento e Spazio Campionario:**
   - I pesci vengono etichettati: indici $[1, 100]$ per i salmoni, indici $[101, 150]$ per le orate.
   - Lo spazio campionario non ordinato è costituito da tutti i possibili sottoinsiemi di cardinalità 30 scelti tra 150:
     $$\Omega = \{A \subseteq \{1, \dots, 150\} \mid \#A = 30\} \implies \#\Omega = \binom{150}{30}$$
2. **Cardinalità dell'Evento Favorevole:**
   - Per scegliere 20 salmoni tra i 100 disponibili vi sono $\binom{100}{20}$ modi.
   - Per scegliere 10 orate tra le 50 disponibili vi sono $\binom{50}{10}$ modi.
   - Per il principio fondamentale del calcolo combinatorio (regola del prodotto), i casi favorevoli sono:
     $$\#E = \binom{100}{20} \cdot \binom{50}{10}$$
3. **Probabilità Classica:**
   $$\mathbb{P}(E) = \frac{\#E}{\#\Omega} = \frac{\binom{100}{20}\binom{50}{10}}{\binom{150}{30}}$$

### Definizione Formale e Condizioni di Ammissibilità
Questo meccanismo di selezione identifica la legge ipergeometrica \[[[Calcolo delle Probabilità.pdf#page=198|Ross p. 179]]]:

> [!danger] Definizione: Variabile Aleatoria Ipergeometrica
> Sia data una popolazione finita di $N = m_1 + m_2$ elementi bipartiti in due categorie: $m_1$ elementi di tipo 1 ("successi") e $m_2$ elementi di tipo 2 ("fallimenti").
> Si estrae senza reinserimento un campione casuale di ampiezza $n \le N$.
> La variabile aleatoria $X$ che conta il numero di elementi di tipo 1 presenti nel campione estratto si dice **ipergeometrica di parametri $m_1, m_2, n$**:
> $$X \sim \text{Hyp}(m_1, m_2, n)$$
> e la sua funzione di densità discreta è:
> $$\mathbb{P}(X = k) = \frac{\binom{m_1}{k}\binom{m_2}{n - k}}{\binom{m_1 + m_2}{n}}$$

> [!summary] Proprietà: Condizioni sui Parametri e Supporto Effettivo
> Affinché i coefficienti binomiali siano definiti e diversi da zero, devono valere le seguenti assunzioni di coerenza combinatoria \[[[Tipologie di variabili.pdf#page=2|Appunti p. 2]]]:
> - $m_1 + m_2 \ge n$ (la dimensione campionaria non può eccedere la popolazione totale);
> - $k \le m_1$ (non si possono estrarre più successi di quanti ne esistano);
> - $n - k \le m_2 \iff k \ge n - m_2$ (il numero di fallimenti estratti non può superare la disponibilità $m_2$);
> - $k \ge 0$ e $k \le n$.
>
> Il <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>supporto effettivo</b></font></mark> della variabile $X$ è dunque delimitato dagli estremi interi:
> $$\max(0, n - m_2) \le k \le \min(n, m_1)$$

> [!tip]- Flashcard: Definizione e Supporto della Variabile Ipergeometrica
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Basic
Front: Qual è la formula della densità discreta per una variabile ipergeometrica $X \sim \text{Hyp}(m_1, m_2, n)$ e quali sono i limiti del suo supporto?
Back: La densità discreta è data da:
$$\mathbb{P}(X=k) = \frac{\binom{m_1}{k}\binom{m_2}{n-k}}{\binom{m_1+m_2}{n}}$$
I limiti del supporto discreto $k$ sono definiti da:
$$\max(0, n - m_2) \le k \le \min(n, m_1)$$
garantendo che non si estraggano più elementi di quanti ne esistano in ciascuna delle due categorie.
Tags: education/university education/math math/probability
END
%%

### Il Modello delle Urne Bicolori
La formalizzazione astratta si traduce nel classico modello delle estrazioni da urne \[[[Tipologie di variabili.pdf#page=3|Appunti p. 3]]]:
- **Composizione dell'urna:** $m_1$ palline nere e $m_2$ palline bianche.
- **Procedura:** Si estraggono $n$ palline in blocco senza reinserimento.
- **Variabile:** $X$ rappresenta la somma delle palline nere estratte:
  $$X = \sum_{i=1}^n \mathbb{1}_{\{\text{l'i-esima estratta è nera}\}}$$
  Allora $X \sim \text{Hyp}(m_1, m_2, n)$.

> [!info] Intuizione Concettuale: Valore Atteso dell'Ipergeometrica e Confronto con la Binomiale
> Sebbene le singole estrazioni senza reinserimento non siano indipendenti, la probabilità marginale che l'i-esima pallina estratta sia di tipo 1 rimane costante per motivi di simmetria:
> $$\mathbb{P}(\text{i-esima pallina è nera}) = \frac{m_1}{m_1 + m_2}$$
> Di conseguenza, per la linearità del valore atteso, la media della variabile ipergeometrica coincide formalmente con quella di una binomiale con parametro $p = \frac{m_1}{m_1 + m_2}$:
> $$\mathbb{E}[X] = n \cdot \frac{m_1}{m_1 + m_2} = n p$$
> La varianza differisce invece da quella binomiale per il fattore di correzione per popolazioni finite (noto come *fattore di frazionamento* o *riduzione della varianza*):
> $$\operatorname{Var}(X) = n p (1 - p) \cdot \frac{N - n}{N - 1}$$
> Per $N \to \infty$ con $p$ costante, il fattore tende a 1 e la distribuzione ipergeometrica converge alla binomiale \[[[Calcolo delle Probabilità.pdf#page=198|Ross p. 181]]].

> [!tip]- Flashcard: Valore Atteso dell'Ipergeometrica
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Cloze
Text: Il valore atteso di una variabile ipergeometrica $X \sim \text{Hyp}(m_1, m_2, n)$ è {{c1::$\mathbb{E}[X] = n \cdot \frac{m_1}{m_1 + m_2}$}}.
Extra: Coincide con la media di una binomiale di parametro $p = \frac{m_1}{m_1+m_2}$ grazie alla linearità del valore atteso applicata alle indicatrici marginali simmetriche.
Tags: education/university education/math math/probability
END
%%

---

## 4. Esempi di Calcolo del Valore Atteso ed Equità del Gioco

### Concetto di Gioco Equo (Onesto)
L'aspettativa matematica o valore atteso $\mathbb{E}[X]$ (introdotto in [[11 - Variabili Aleatorie, Densità Discreta, Valore Atteso e Distribuzione Geometrica]]) rappresenta il baricentro probabilistico della distribuzione e fornisce il criterio rigoroso per definire l'equità economica di una scommessa \[[[Dispense Statistica e Probabilità.pdf#page=118|Dispense p. 111]]], \[[[Calcolo delle Probabilità.pdf#page=161|Ross p. 142]]].

> [!summary] Criterio di Equità di una Scommessa
> Sia un gioco in cui il partecipante versa una puntata iniziale certa di $C$ unità monetarie e riceve al termine dell'esperimento aleatorio una vincita lorda $V: \Omega \to \mathbb{R}^+$.
> - Il guadagno netto del giocatore è la variabile aleatoria:
>   $$G = V - C$$
> - Il gioco si dice **equo (onesto)** se il valore atteso del guadagno netto è nullo:
>   $$\mathbb{E}[G] = 0 \iff \mathbb{E}[V - C] = 0 \iff \mathbb{E}[V] = C$$
> - Se $\mathbb{E}[V] < C$, il gioco è favorevole al banco (sfavorevole al giocatore).

### Esempio 1: Lancio di Due Dadi e Scommessa su Somma 7
Si consideri il lancio simultaneo di due dadi a sei facce non truccati. Si scommette sull'evento "la somma delle due facce è pari a 7" con puntata di $1€$ \[[[Tipologie di variabili.pdf#page=3|Appunti p. 3]]].

- **Domanda:** Di quanto deve essere moltiplicata la puntata iniziale di $1€$ da parte del banco (moltiplicatore di vincita lorda $p$) affinché il gioco risulti matematicamente equo?

> [!example] Risoluzione Dettagliata
> 1. **Spazio campionario:**
>    $$\Omega = \{1, \dots, 6\}^2 = \{(i, j) \mid i, j \in \{1, \dots, 6\}\} \implies \#\Omega = 6 \times 6 = 36$$
> 2. **Variabile di vincita lorda:**
>    $$V(i, j) = \begin{cases} p & \text{se } i + j = 7 \\ 0 & \text{se } i + j \neq 7 \end{cases}$$
> 3. **Individuazione delle configurazioni favorevoli:**
>    L'evento $\{V = p\} = \{i + j = 7\}$ è costituito dalle coppie:
>    $$\{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)\} \implies \#\{V = p\} = 6$$
> 4. **Densità di probabilità di $V$:**
>    $$\mathbb{P}(V = p) = \frac{6}{36} = \frac{1}{6}, \quad \mathbb{P}(V = 0) = 1 - \frac{1}{6} = \frac{5}{6}$$
> 5. **Calcolo del valore atteso della vincita:**
>    $$\mathbb{E}[V] = \sum_{y \in \{0, p\}} y \, p_V(y) = 0 \cdot \mathbb{P}(V = 0) + p \cdot \mathbb{P}(V = p) = 0 \cdot \frac{5}{6} + p \cdot \frac{1}{6} = \frac{p}{6}$$
> 6. **Condizione di equità:**
>    Imponendo che il valore atteso della vincita eguagli la puntata di $1€$:
>    $$\mathbb{E}[V] = 1 \implies \frac{p}{6} = 1 \implies p = 6$$
>
> **Conclusione:** Il banco deve restituire $6€$ lordi (un moltiplicatore pari a 6 volte la puntata) affinché la scommessa sia equa.

> [!tip]- Flashcard: Calcolo Moltiplicatore di Vincita Equo (Due Dadi)
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Basic
Front: Lancio di due dadi regolari a 6 facce con scommessa sulla somma pari a 7 e puntata di 1€. Come si determina il moltiplicatore di vincita lorda $p$ affinché il gioco sia equo?
Back: L'evento somma 7 ha cardinalità 6 su 36 esiti, quindi probabilità $1/6$. La variabile vincita lorda $V$ assume valori $p$ con probabilità $1/6$ e $0$ con probabilità $5/6$. Il valore atteso è $\mathbb{E}[V] = p \cdot (1/6)$. Imponendo la condizione di equità $\mathbb{E}[V] = 1€$, si ricava $p/6 = 1 \implies p = 6$.
Tags: education/university education/math math/probability
END
%%

### Esempio 2: Moltiplicazione Esponenziale e Divergenza del Valore Atteso
Il secondo esempio d'aula analizza un modello aleatorio con vincita moltiplicativa, che mette in luce la discrepanza tra il valore atteso matematico e la probabilità reale di conseguire un profitto \[[[Tipologie di variabili.pdf#page=3|Appunti pp. 3–4]]].

- **Regole del gioco:**
  - Si lancia una moneta equilibrata ($p = 1/2$) per $n$ volte consecutive (prove bernoulliane indipendenti).
  - Ad ogni esito "testa", il premio accumulato si triplica (moltiplicatore $\times 3$).
  - Non appena si verifica un esito "croce", la scommessa fallisce e il giocatore perde tutto ($V = 0$).
  - Per incassare il premio moltiplicato, è necessario ottenere una sequenza ininterrotta di $n$ teste.

> [!danger] Analisi Formale: Vincita, Probabilità e Media Asintotica
> Siano gli eventi elementari:
> $$A_i = \{\text{testa all'i-esimo lancio}\}, \quad \mathbb{P}(A_i) = \frac{1}{2}, \quad i = 1, \dots, n$$
> 
> 1. **Espressione algebrica della vincita:**
>    La vincita complessiva $V$ è data dal prodotto delle vincite parziali:
>    $$V = (3 \mathbb{1}_{A_1})(3 \mathbb{1}_{A_2}) \dots (3 \mathbb{1}_{A_n}) = 3^n \prod_{i=1}^n \mathbb{1}_{A_i} = 3^n \mathbb{1}_{A_1 \cap A_2 \cap \dots \cap A_n}$$
>
> 2. **Probabilità di vincita:**
>    Poiché i lanci sono stocasticamente indipendenti:
>    $$\mathbb{P}(\text{vincere}) = \mathbb{P}(V = 3^n) = \mathbb{P}\left(\bigcap_{i=1}^n A_i\right) = \prod_{i=1}^n \mathbb{P}(A_i) = \left(\frac{1}{2}\right)^n = \frac{1}{2^n}$$
>    Al crescere del numero di lanci $n$:
>    $$\lim_{n \to +\infty} \mathbb{P}(\text{vincere}) = \lim_{n \to +\infty} \frac{1}{2^n} = 0$$
>
> 3. **Calcolo del valore atteso della vincita:**
>    Sfruttando la proprietà fondamentale $\mathbb{E}[\mathbb{1}_A] = \mathbb{P}(A)$:
>    $$\mathbb{E}[V] = \mathbb{E}\left[3^n \mathbb{1}_{\bigcap_{i=1}^n A_i}\right] = 3^n \mathbb{E}\left[\mathbb{1}_{\bigcap_{i=1}^n A_i}\right] = 3^n \mathbb{P}\left(\bigcap_{i=1}^n A_i\right) = 3^n \cdot \frac{1}{2^n} = \left(\frac{3}{2}\right)^n$$
>    Al divergere del numero di lanci $n$:
>    $$\lim_{n \to +\infty} \mathbb{E}[V] = \lim_{n \to +\infty} \left(\frac{3}{2}\right)^n = +\infty$$

> [!info] Significato Epistemologico: La Vincita Sorpassa la Probabilità
> Come evidenziato negli appunti d'aula \[[[Tipologie di variabili.pdf#page=4|Appunti p. 4]]], questo scenario introduce a paradossi storici del calcolo delle probabilità (affine al celebre **Paradosso di San Pietroburgo**):
> - **Crescita della remunerazione vs rarità dell'evento:** L'entità della vincita promessa ($3^n$) cresce con base 3, surclassando esponenzialmente il tasso di decadimento della probabilità di successo ($(1/2)^n$), la cui base è 2.
> - **Comportamento per $n$ elevato:** Per $n$ molto grande, vincere diventa un evento quasi impossibile (probabilità che tende a 0). Tuttavia, se l'evento raro si realizza, l'entità della ricompensa è così smisurata da trascinare la media aritmetica teorica a $+\infty$.
> - **Implicazione decisionale:** Se un individuo si basasse esclusivamente sul valore atteso per valutare la convenienza della scommessa ($\mathbb{E}[V] \to +\infty$), sarebbe disposto a pagare qualsiasi somma finita per partecipare, pur sapendo che con probabilità prossima a 1 perderà l'intero capitale investito. Ciò dimostra l'inadeguatezza del semplice valore atteso lineare per descrivere le scelte razionali in condizioni di rischio estremo, motivando l'introduzione della teoria dell'utilità attesa.

> [!tip]- Flashcard: Vincita Esponenziale e Valore Atteso Divergente
%%
TARGET DECK: University::Probabilità e Statistica::15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso
START
Basic
Front: In un gioco con moneta bilanciata a $n$ prove indipendenti, la vincita triplica per ogni testa consecutiva ma si azzera alla prima croce. Quanto valgono la probabilità di vincita e il valore atteso?
Back: 1. Probabilità di vincita: $\mathbb{P}(V = 3^n) = (1/2)^n \to 0$ per $n \to +\infty$.
2. Valore atteso: $\mathbb{E}[V] = 3^n \mathbb{P}(V = 3^n) = 3^n (1/2)^n = (3/2)^n \to +\infty$ per $n \to +\infty$.
La crescita esponenziale del premio supera il decadimento della probabilità, generando un valore atteso divergente pur con probabilità di successo infinitesima.
Tags: education/university education/math math/probability
END
%%

---

## 5. Quadro Sinottico Comparativo delle Distribuzioni Discrete

La seguente tabella riassume e confronta le principali famiglie discrete finora trattate nel corso:

| Distribuzione | Parametri | Supporto $X(\Omega)$ | PMF $\mathbb{P}(X = k)$ | Valore Atteso $\mathbb{E}[X]$ | Schema Sperimentale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bernoulli** | $p \in [0, 1]$ | $\{0, 1\}$ | $p^k (1 - p)^{1 - k}$ | $p$ | Singola prova dicotomica (successo/fallimento) |
| **Binomiale** | $n \in \mathbb{N}^+$, $p \in [0, 1]$ | $\{0, 1, \dots, n\}$ | $\binom{n}{k} p^k (1 - p)^{n - k}$ | $n p$ | Conteggio successi su $n$ prove indipendenti con reinserimento |
| **Geometrica** | $p \in (0, 1]$ | $\{1, 2, 3, \dots\}$ | $(1 - p)^{k - 1} p$ | $\frac{1}{p}$ | Tempo di primo successo in prove bernoulliane ripetute |
| **Ipergeometrica** | $m_1, m_2, n \in \mathbb{N}$ | $\{\max(0, n - m_2), \dots, \min(n, m_1)\}$ | $\frac{\binom{m_1}{k}\binom{m_2}{n - k}}{\binom{m_1 + m_2}{n}}$ | $n \cdot \frac{m_1}{m_1 + m_2}$ | Estrazione casuale di $n$ elementi senza reinserimento da popolazione finita bipartita |

---
**SUMMARY**
Variabili aleatorie di Bernoulli, binomiali e ipergeometriche, con modelli di estrazione senza reinserimento, calcolo del valore atteso ed equità del gioco.
