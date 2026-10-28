---
status: permanent
type: lecture
area: education
related: ["[[Probabilità e Statistica MOC]]", "[[Ingegneria Informatica 2026 - 27 MOC]]", "[[University]]", "[[Metodo di Studio - PACRAR]]", "[[01 - Teoria degli Insiemi, Spazio Campionario e Prime Nozioni di Probabilità]]", "[[02 - Insieme delle Parti, Assiomi della Probabilità e Spazi Finiti]]", "[[15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso]]", "[[03 - Funzioni (Parte I)]]", "[[04 - Funzioni (Parte II)]]", "[[06 - Valore Assoluto, Numeri Naturali e Principio di Induzione]]"]
aliases: ["Lezione 13 Probabilità e Statistica", "PeS Lezione 13", "Variabili Aleatorie Discrete e Valore Atteso", "Distribuzione Geometrica e Schema di Bernoulli", "13 - Variabili Aleatorie e Valore Atteso"]
source: Lezione 13 Probabilità e Statistica del 22/10/2026 - Prof.ssa Giovanna Nappo, Prof. Fabio Spizzichino
title: "13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica"
date: '2026-10-22'
updated: 2026-10-28T08:07
tags: [education/university, education/math, math/probability, math/statistics]
summary: "Variabili aleatorie discrete, densità di probabilità, variabile indicatrice di Bernoulli, valore atteso con linearità e distribuzione geometrica."
course: "Probabilità e Statistica"
sources: ["[[Variabili Aleatorie.pdf]]", "[[Proprietà delle Variabili Aleatorie.pdf]]", "[[Dispense Statistica e Probabilità.pdf]]", "[[Calcolo delle Probabilità.pdf]]"]
---
[[Home MOC|Home]] / [[University|University MOC]] / [[Probabilità e Statistica MOC]] / [[13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica]]

# 13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica

- **Docenti:** Prof.ssa Giovanna Nappo, Prof. Fabio Spizzichino
- **Data Lezione:** 2026-10-22
- **Materiali Didattici Ufficiali:**
  - \[[[Variabili Aleatorie.pdf#page=1|Appunti d'Aula — Variabili Aleatorie (pp. 1–3)]]]
  - \[[[Proprietà delle Variabili Aleatorie.pdf#page=1|Appunti d'Aula — Proprietà delle Variabili Aleatorie (pp. 1–5)]]]
  - \[[[Dispense Statistica e Probabilità.pdf#page=87|Capitolo 7 — Variabili aleatorie e distribuzioni di probabilità (pp. 80–86)]]]
  - \[[[Dispense Statistica e Probabilità.pdf#page=118|Capitolo 9 — Valore atteso di una variabile aleatoria e relative proprietà (pp. 111–122)]]]
  - \[[[Calcolo delle Probabilità.pdf#page=154|Sheldon Ross — Capitolo 4.1-4.2: Variabili Aleatorie e Variabili Discrete (pp. 135–142)]]]
  - \[[[Calcolo delle Probabilità.pdf#page=161|Sheldon Ross — Capitolo 4.3: Valore Atteso (pp. 142–148)]]]
  - \[[[Calcolo delle Probabilità.pdf#page=193|Sheldon Ross — Capitolo 4.8.1: La Variabile Aleatoria Geometrica (pp. 174–178)]]]
- **Riferimento MOC:** [[Probabilità e Statistica MOC]], [[Ingegneria Informatica 2026 - 27 MOC]]
- **Lezioni Precedenti:** [[01 - Teoria degli Insiemi, Spazio Campionario e Prime Nozioni di Probabilità]], [[02 - Insieme delle Parti, Assiomi della Probabilità e Spazi Finiti]]
- **Lezioni Successive:** [[15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso]]
- **Collegamenti Interdisciplinari:** [[03 - Funzioni (Parte I)]] e [[04 - Funzioni (Parte II)]] (definizione formale di applicazione, dominio, codominio e controimmagine funzionale $X^{-1}(B)$), [[06 - Valore Assoluto, Numeri Naturali e Principio di Induzione]] (successioni numeriche discrete e convergenza della serie geometrica con derivazione termine a termine)

La tredicesima lezione di Elementi di Calcolo delle Probabilità e Statistica sancisce la transizione strutturale dalla teoria assiomatica degli insiemi alla teoria analitica delle <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>variabili aleatorie</b></font></mark>. Nei contesti ingegneristici e informatici, l'interesse computazionale non verte sulla descrizione microscopica dell'esito elementare $\omega$ dello spazio campionario $\Omega$, bensì sulla misurazione numerica o quantitativa prodotta dal fenomeno casuale.

La trattazione definisce formalmente la variabile aleatoria reale e il vettore aleatorio multidimensionale, illustrando il meccanismo analitico del "pensare all'indietro" tramite la controimmagine insiemistica. Viene quindi introdotta la <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>funzione di densità di probabilità discreta</b></font></mark> (PMF) e la sua condizione costitutiva di normalizzazione ad $1$. Successivamente, la <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>variabile indicatrice</b></font></mark> viene caratterizzata come modello bernoulliano elementare per la generazione di variabili composte. Nella seconda parte, l'operatore di <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>valore atteso</b></font></mark> viene formalizzato come baricentro probabilistico; sfruttando la fondamentale proprietà di linearità, se ne ricava l'espressione per la distribuzione binomiale senza ricorrere a calcoli combinatori complessi. La lezione si conclude con la caratterizzazione della <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>variabile geometrica</b></font></mark> (tempo di primo successo) e il calcolo del relativo valore atteso mediante la derivazione termine a termine della serie geometrica.

---

## 1. Variabili Aleatorie e Vettori Aleatori: Transizione da Eventi a Valori Reali

### Motivazione Ingegneristica e Cambio di Paradigma
Nelle prime lezioni ([[01 - Teoria degli Insiemi, Spazio Campionario e Prime Nozioni di Probabilità]]), gli eventi sono stati formulati come sottoinsiemi dello spazio campionario $\Omega$. Nelle applicazioni reali (telecomunicazioni, analisi del rischio, calcolo distribuito), emergono due esigenze pratiche \[[[Variabili Aleatorie.pdf#page=1|Appunti p. 1]]]:
- **Superamento della natura astratta di $\Omega$:** Spesso $\Omega$ è formato da descrizioni qualitative complesse (es. sequenze temporali di pacchetti, esiti fisici di lanci di dadi, vibrazioni sismiche).
- **Quantificazione numerica diretta:** L'utente ha l'esigenza di quantificare guadagni economici, ritardi di rete in millisecondi o la probabilità che una scossa sismica generi danni superiori a una determinata soglia critica $\{X \ge 10^6\}$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=1|Appunti p. 1]]]. La vincita o la misura "non vive su $\Omega$, ma agisce sui numeri reali $\mathbb{R}$".

> [!danger] Definizione: Variabile Aleatoria Reale
> Sia $(\Omega, \mathcal{F}, \mathbb{P})$ uno spazio di probabilità misurabile (si veda [[02 - Insieme delle Parti, Assiomi della Probabilità e Spazi Finiti]]). Una **variabile aleatoria reale** $X$ è un'applicazione che associa a ogni esito elementare $\omega \in \Omega$ uno e un solo valore reale numerico $X(\omega) \in \mathbb{R}$:
> $$X: \Omega \to \mathbb{R}, \quad \omega \mapsto X(\omega)$$
> Tale applicazione deve essere misurabile, ovvero per ogni intervallo o sottoinsieme boreliano $B \subseteq \mathbb{R}$, l'insieme degli eventi che mappano in $B$ appartiene alla $\sigma$-algebra degli eventi $\mathcal{F}$ \[[[Dispense Statistica e Probabilità.pdf#page=87|Dispense p. 80]]], \[[[Calcolo delle Probabilità.pdf#page=154|Ross p. 135]]].

> [!tip]- Flashcard: Definizione di Variabile Aleatoria Reale
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Basic
Front: Cos'è formalmente una variabile aleatoria reale $X$ e qual è il suo scopo operativo?
Back: Una variabile aleatoria reale è un'applicazione misurabile $X: \Omega \to \mathbb{R}$ che assegna a ogni esito elementare $\omega \in \Omega$ un numero reale $X(\omega)$. Il suo scopo operativo è tradurre eventi astratti o qualitativi dello spazio campionario in grandezze numeriche quantitative calcolabili.
Tags: education/university education/math math/probability
END
%%

### Il Meccanismo del "Pensare all'Indietro" (Controimmagine)
Il calcolo delle probabilità di asserzioni numeriche su $X$ avviene risalendo allo spazio di partenza tramite l'operatore di <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>controimmagine funzionale</b></font></mark> (approfondito in [[03 - Funzioni (Parte I)]]):
- Dato un insieme numerico $B \subseteq \mathbb{R}$, l'evento $\{X \in B\}$ è definito rigorosamente da:
  $$\{X \in B\} := X^{-1}(B) = \{\omega \in \Omega \mid X(\omega) \in B\}$$
- La probabilità attribuita all'affermazione numerica coincide con la misura di probabilità dell'evento controimmagine originario:
  $$\mathbb{P}(X \in B) := \mathbb{P}(X^{-1}(B)) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) \in B\})$$
- *Esempio applicativo d'aula:* Se $X(\omega)$ quantifica i danni monetari di una scossa di terremoto, calcolare la probabilità che i danni superino un milione di euro significa individuare l'evento insiemistico $\{\omega \in \Omega \mid X(\omega) \ge 10^6\} = X^{-1}([10^6, +\infty))$ e misurarne la probabilità su $\Omega$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=1|Appunti p. 1]]].

> [!tip]- Flashcard: Controimmagine di una Variabile Aleatoria
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Cloze
Text: Data una variabile aleatoria $X: \Omega \to \mathbb{R}$ e un insieme $B \subseteq \mathbb{R}$, l'evento $\{X \in B\}$ è la {{c1::controimmagine}} definita da {{c2::$\{\omega \in \Omega \mid X(\omega) \in B\}$}}, e la sua probabilità è assegnata da {{c3::$\mathbb{P}(X \in B) = \mathbb{P}(X^{-1}(B))$}}.
Extra: Questo meccanismo consente di "pensare all'indietro", riconducendo affermazioni numeriche ad eventi misurabili dello spazio campionario originario.
Tags: education/university education/math math/probability
END
%%

### Vettori Aleatori
Quando un fenomeno produce simultaneamente molteplici misurazioni numeriche interconnesse, si definisce un <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>vettore aleatorio</b></font></mark> multidimensionale \[[[Variabili Aleatorie.pdf#page=1|Appunti p. 1]]]:

> [!danger] Definizione: Vettore Aleatorio
> Sia $(\Omega, \mathcal{F}, \mathbb{P})$ uno spazio campionario e sia $N \in \mathbb{N}^+$. Un **vettore aleatorio** $N$-dimensionale è un'applicazione:
> $$Z: \Omega \to \mathbb{R}^N, \quad \omega \mapsto Z(\omega) = (X_1(\omega), X_2(\omega), \dots, X_N(\omega))$$
> dove ogni singola componente coordinata $X_i: \Omega \to \mathbb{R}$ ($i = 1, \dots, N$) è a sua volta una variabile aleatoria reale.

> [!example] Esempio: Lancio di Due Dadi
> - Si consideri l'esperimento del lancio simultaneo di due dadi a 6 facce con spazio campionario $\Omega = \{(i, j) \mid 1 \le i, j \le 6\}$.
> - Si definiscono le variabili:
>   $$X(i, j) = i \quad (\text{esito dado 1}), \qquad Y(i, j) = j \quad (\text{esito dado 2})$$
> - L'applicazione $Z(i, j) = (X(i, j), Y(i, j)) = (i, j)$ costituisce un vettore aleatorio $Z: \Omega \to \mathbb{R}^2$ \[[[Variabili Aleatorie.pdf#page=2|Appunti p. 2]]].

> [!example] Esempio: Conteggio delle Teste in Tre Lanci di Moneta
> - Spazio campionario di 3 lanci indipendenti di moneta bilanciata: $\Omega = \{(x_1, x_2, x_3) \mid x_i \in \{T, C\}\}$ con $|\Omega| = 2^3 = 8$ esiti equiprobabili.
> - Si consideri la variabile aleatoria $Y$ indicante il numero totale di "Teste" estratte: $Y(\omega) \in \{0, 1, 2, 3\}$.
> - Determinazione della probabilità per via insiemistica e combinatoria \[[[Variabili Aleatorie.pdf#page=2|Appunti pp. 2–3]]]:
>   - $Y = 0 \iff \omega = (C, C, C) \implies \mathbb{P}(Y=0) = \binom{3}{0}\left(\frac{1}{2}\right)^0\left(\frac{1}{2}\right)^3 = \frac{1}{8}$
>   - $Y = 1 \iff \omega \in \{(T,C,C), (C,T,C), (C,C,T)\} \implies \mathbb{P}(Y=1) = \binom{3}{1}\left(\frac{1}{2}\right)^1\left(\frac{1}{2}\right)^2 = \frac{3}{8}$
>   - $Y = 2 \iff \omega \in \{(T,T,C), (T,C,T), (C,T,T)\} \implies \mathbb{P}(Y=2) = \binom{3}{2}\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^1 = \frac{3}{8}$
>   - $Y = 3 \iff \omega = (T, T, T) \implies \mathbb{P}(Y=3) = \binom{3}{3}\left(\frac{1}{2}\right)^3\left(\frac{1}{2}\right)^0 = \frac{1}{8}$

> [!tip]- Flashcard: Vettore Aleatorio
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Basic
Front: Come viene definito un vettore aleatorio $N$-dimensionale $Z$ su uno spazio campionario $\Omega$?
Back: Un vettore aleatorio $N$-dimensionale è una funzione $Z: \Omega \to \mathbb{R}^N$ che associa a ogni $\omega \in \Omega$ una $N$-upla reale $(X_1(\omega), \dots, X_N(\omega))$, dove ciascuna funzione coordinata $X_i: \Omega \to \mathbb{R}$ è una variabile aleatoria reale.
Tags: education/university education/math math/probability
END
%%

---

## 2. Densità di Probabilità Discreta (Funzione di Massa di Probabilità)

### Struttura degli Spazi Discreti e Partizione Indotta
Quando l'insieme dei possibili valori assunti dalla variabile aleatoria $X$ è finito oppure numerabile, la variabile si dice discreta \[[[Dispense Statistica e Probabilità.pdf#page=87|Dispense p. 80]]], \[[[Calcolo delle Probabilità.pdf#page=158|Ross p. 139]]].

> [!danger] Definizione: Variabile Aleatoria Discreta
> Una variabile aleatoria $X$ si dice **discreta** se la sua immagine (denominata *supporto*) $X(\Omega) \subseteq \mathbb{R}$ è un insieme finito o numerabile:
> $$X(\Omega) = \{x_1, x_2, \dots, x_k, \dots\} \subset \mathbb{R}$$
> In tal caso, la famiglia di eventi puntuali:
> $$H_k^X := \{X = x_k\} = \{\omega \in \Omega \mid X(\omega) = x_k\}, \quad x_k \in X(\Omega)$$
> costituisce una <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>partizione dell'evento certo</b></font></mark> $\Omega$:
> 1. Gli eventi sono a due a due incompatibili: $\{X = x_j\} \cap \{X = x_k\} = \emptyset$ per ogni $j \ne k$;
> 2. L'unione esaustiva ricostruisce l'intero spazio campionario: $\bigcup_{k} \{X = x_k\} = \Omega$.

> [!tip]- Flashcard: Partizione Indotta da Variabile Discreta
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Cloze
Text: Gli eventi puntuali $\{X = x_k\}$ generati da una variabile aleatoria discreta costituiscono una {{c1::partizione}} dello spazio campionario $\Omega$, poiché sono a due a due {{c2::incompatibili (disgiunti)}} e la loro unione coincide con {{c3::l'evento certo $\Omega$}}.
Extra: Questa proprietà garantisce che la somma di tutte le densità puntuali sia esattamente pari ad $1$.
Tags: education/university education/math math/probability
END
%%

### Funzione di Densità di Probabilità Discreta (PMF)
La distribuzione di probabilità di una variabile discreta è descritta dalla sua <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>densità di probabilità discreta</b></font></mark> (indicata in letteratura anglosassone come *Probability Mass Function* — PMF) \[[[Proprietà delle Variabili Aleatorie.pdf#page=1|Appunti p. 1]]]:

> [!danger] Definizione: Densità di Probabilità Discreta
> Sia $X: \Omega \to \mathbb{R}$ una variabile aleatoria discreta. Si definisce **densità di probabilità discreta** di $X$ la funzione $p_X: \mathbb{R} \to [0, 1]$ definita puntualmente da:
> $$p_X(y) := \mathbb{P}(X = y) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) = y\}), \quad \forall y \in \mathbb{R}$$

> [!summary] Proprietà Costitutive della Densità Discreta
> 1. **Positività e Supporto:** $p_X(y) \ge 0$ per ogni $y \in \mathbb{R}$. Se $y \notin X(\Omega)$, allora $p_X(y) = 0$.
> 2. **Condizione di Normalizzazione Fondamentale:** La somma di tutte le probabilità puntuali è rigorosamente pari a $1$:
>    $$\sum_{y \in \mathbb{R}} p_X(y) = \sum_{x_k \in X(\Omega)} \mathbb{P}(X = x_k) = 1$$
> 3. **Misura di Eventi Composti:** Per qualsiasi sottoinsieme $B \subseteq \mathbb{R}$, la probabilità dell'evento $\{X \in B\}$ è ottenuta sommando le densità dei punti appartenenti a $B$:
>    $$\mathbb{P}(X \in B) = \sum_{y \in B \cap X(\Omega)} p_X(y)$$

> [!abstract]- Dimostrazione Formale Passo-Passo: Condizione di Normalizzazione
> - **Idea chiave:** Sfruttare gli assiomi di additività e normalizzazione di Kolmogorov ([[02 - Insieme delle Parti, Assiomi della Probabilità e Spazi Finiti]]) sulla partizione generata dagli eventi puntuali $\{X = x_k\}$.
> - **Passo 1 (Disgiunzione):** Poiché gli insiemi $\{X = x_k\}$ sono a due a due disgiunti, per il terzo assioma di probabilità (additività numerabile):
>   $$\sum_{x_k \in X(\Omega)} p_X(x_k) = \sum_{x_k \in X(\Omega)} \mathbb{P}(X = x_k) = \mathbb{P}\left(\bigcup_{x_k \in X(\Omega)} \{X = x_k\}\right)$$
> - **Passo 2 (Copertura di $\Omega$):** Ogni esito elementare $\omega \in \Omega$ viene mappato in un valore $X(\omega) \in X(\Omega)$. Di conseguenza:
>   $$\bigcup_{x_k \in X(\Omega)} \{\omega \in \Omega \mid X(\omega) = x_k\} = \Omega$$
> - **Passo 3 (Normalizzazione di Kolmogorov):** Sostituendo l'evento certo $\Omega$:
>   $$\sum_{y \in \mathbb{R}} p_X(y) = \mathbb{P}(\Omega) = 1 \quad \blacksquare$$

> [!example] Esempio d'Aula con Partizione Finita
> - Sia $\Omega = \{\omega_1, \omega_2, \omega_3, \omega_4\}$ uno spazio a 4 elementi e sia $X: \Omega \to \{0, 1, 2\}$ definita da $X(\omega_1) = 0$, $X(\omega_2) = 1$, $X(\omega_3) = X(\omega_4) = 2$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=1|Appunti p. 1]]].
> - La funzione densità vale:
>   $$p_X(y) = \begin{cases} \mathbb{P}(\{\omega_1\}) & \text{se } y = 0 \\ \mathbb{P}(\{\omega_2\}) & \text{se } y = 1 \\ \mathbb{P}(\{\omega_3, \omega_4\}) & \text{se } y = 2 \\ 0 & \text{se } y \notin \{0, 1, 2\} \end{cases}$$
> - La normalizzazione è verificata:
>   $$\sum_{y \in \mathbb{R}} p_X(y) = \mathbb{P}(\{\omega_1\}) + \mathbb{P}(\{\omega_2\}) + \mathbb{P}(\{\omega_3, \omega_4\}) = \mathbb{P}\left(\bigcup_{i=1}^4 \{\omega_i\}\right) = \mathbb{P}(\Omega) = 1$$

> [!tip]- Flashcard: Densità di Probabilità Discreta e Normalizzazione
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Basic
Front: Come si definisce la densità di probabilità discreta $p_X(y)$ e qual è la sua condizione fondamentale di normalizzazione?
Back: La densità di probabilità discreta è definita da $p_X(y) := \mathbb{P}(X = y)$ per ogni $y \in \mathbb{R}$. Soddisfa la condizione di normalizzazione $\sum_{y \in \mathbb{R}} p_X(y) = 1$, derivante dal fatto che gli eventi puntuali $\{X=y\}$ partizionano l'evento certo $\Omega$.
Tags: education/university education/math math/probability
END
%%

---

## 3. Variabile Indicatrice di un Evento e Modello di Bernoulli

### La Funzione Indicatrice (Caratteristica)
L'anello di congiunzione algebrico fondamentale tra il calcolo combinatorio degli eventi e le variabili numeriche è la <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>funzione indicatrice</b></font></mark> \[[[Proprietà delle Variabili Aleatorie.pdf#page=1|Appunti pp. 1–2]]], \[[[Dispense Statistica e Probabilità.pdf#page=87|Dispense p. 85]]]:

> [!danger] Definizione: Variabile Indicatrice di un Evento
> Sia $A \subseteq \Omega$ un evento qualsiasi nello spazio di probabilità $(\Omega, \mathcal{F}, \mathbb{P})$. La **funzione indicatrice** di $A$ (indicata con $\mathbb{1}_A$ o $\mathbf{1}_A$) è la variabile aleatoria definita puntualmente da:
> $$\mathbb{1}_A(\omega) := \begin{cases} 1 & \text{se } \omega \in A \\ 0 & \text{se } \omega \notin A \quad (\omega \in A^c) \end{cases}$$
> - **Immagine:** $\mathbb{1}_A(\Omega) \subseteq \{0, 1\}$.
> - **Legame con il successo:** $\omega$ realizza il successo se e solo se $\mathbb{1}_A(\omega) = 1$.

> [!summary] Densità di Probabilità della Variabile Indicatrice
> La funzione di densità discreta di $X = \mathbb{1}_A$ è concentrata unicamente nei due valori binari $y \in \{0, 1\}$:
> $$p_{\mathbb{1}_A}(y) = \begin{cases} \mathbb{P}(A^c) = 1 - \mathbb{P}(A) & \text{se } y = 0 \\ \mathbb{P}(A) & \text{se } y = 1 \\ 0 & \text{se } y \notin \{0, 1\} \end{cases}$$
> La condizione di normalizzazione è banalmente verificata: $p_{\mathbb{1}_A}(0) + p_{\mathbb{1}_A}(1) = (1 - \mathbb{P}(A)) + \mathbb{P}(A) = 1$.

> [!tip]- Flashcard: Funzione Indicatrice e Densità
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Cloze
Text: La funzione indicatrice $\mathbb{1}_A$ dell'evento $A$ assume valore {{c1::$1$}} se $\omega \in A$ e {{c2::$0$}} se $\omega \notin A$. La sua densità di probabilità assegna massa {{c3::$\mathbb{P}(A)$}} a $y=1$ e {{c4::$1-\mathbb{P}(A)$}} a $y=0$.
Extra: Ogni variabile dicotomica $\{0, 1\}$ coincide con l'indicatrice di un opportuno evento dello spazio campionario.
Tags: education/university education/math math/probability
END
%%

### Variabile di Bernoulli e Generazione di Modelli Somma
Una variabile aleatoria binaria $X \sim Be(p)$ non è altro che l'indicatrice di un evento con probabilità $p$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=2|Appunti p. 2]]]:

> [!danger] Definizione: Variabile di Bernoulli
> Una variabile aleatoria reale $X$ si dice di **Bernoulli** di parametro $p \in [0, 1]$, indicata con la notazione:
> $$X \sim Be(p)$$
> se assume valori in $\{0, 1\}$ con distribuzione:
> $$\mathbb{P}(X = 1) = p, \qquad \mathbb{P}(X = 0) = 1 - p$$

Quando consideriamo $n$ prove di Bernoulli indipendenti con eventi di successo $A_1, A_2, \dots, A_n$ di probabilità costante $\mathbb{P}(A_i) = p$, possiamo costruire la variabile somma \[[[Proprietà delle Variabili Aleatorie.pdf#page=2|Appunti p. 2]]]:
$$X(\omega) = \sum_{i=1}^n \mathbb{1}_{A_i}(\omega)$$
- Il valore numerico $X(\omega) = j$ conta esattamente il numero totale di successi realizzati nella sequenza di $n$ prove.
- L'evento $\{X = n\}$ equivale all'intersezione simultanea di tutti i successi: $\omega \in \bigcap_{i=1}^n A_i$.
- Per $n = 1$, si ritrova la variabile di Bernoulli $X = \mathbb{1}_A \sim Be(p)$.
- Per $n > 1$ prove indipendenti, $X$ è la <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>variabile binomiale</b></font></mark> $X \sim Bi(n, p)$ con distribuzione (trattata in dettaglio in [[15 - Variabili di Bernoulli, Binomiali, Ipergeometriche ed Esempi di Valore Atteso]]):
  $$\mathbb{P}(X = j) = \binom{n}{j} p^j (1 - p)^{n-j}, \quad j \in \{0, 1, \dots, n\}$$

> [!tip]- Flashcard: Variabile di Bernoulli e Somma di Indicatrici
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Basic
Front: Come viene definita una variabile di Bernoulli $X \sim Be(p)$ e come genera la variabile binomiale $S_n$?
Back: Una variabile di Bernoulli $X \sim Be(p)$ assume valori in $\{0, 1\}$ con probabilità $\mathbb{P}(X=1)=p$ e $\mathbb{P}(X=0)=1-p$. La somma di $n$ variabili di Bernoulli indipendenti $S_n = \sum_{i=1}^n \mathbb{1}_{A_i}$ definisce una variabile binomiale $S_n \sim Bi(n,p)$ che conta il numero di successi su $n$ prove.
Tags: education/university education/math math/probability
END
%%

---

## 4. Valore Atteso: Definizione, Baricentro Probabilistico ed Esempi Fondamentali

### Definizione Formale e Significato Fisico
Il <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>valore atteso</b></font></mark> (*expected value* o media probabilistica) rappresenta la misura di tendenza centrale fondamentale della teoria della probabilità \[[[Proprietà delle Variabili Aleatorie.pdf#page=3|Appunti p. 3]]], \[[[Dispense Statistica e Probabilità.pdf#page=118|Dispense p. 111]]], \[[[Calcolo delle Probabilità.pdf#page=161|Ross p. 142]]]:

> [!danger] Definizione: Valore Atteso di una Variabile Discreta
> Sia $X: \Omega \to \mathbb{R}$ una variabile aleatoria discreta con densità di probabilità $p_X(y)$. Si definisce **valore atteso** (o speranza matematica) di $X$, indicato con $\mathbb{E}[X]$ (o $E(X)$), la quantità scalare:
> $$\mathbb{E}[X] := \sum_{y \in \mathbb{R}} y \, p_X(y) = \sum_{y \in \mathbb{R}} y \, \mathbb{P}(X = y)$$
> purché la serie (se infinita) sia assolutamente convergente: $\sum_{y} |y| p_X(y) < +\infty$.
> - **Significato Operativo:** Il valore atteso è una **media pesata (ponderata)** dei valori reali $y$ assunti da $X$, dove a ciascun valore $y$ viene assegnato un peso pari alla probabilità di accadimento $p_X(y)$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=3|Appunti p. 3]]].
> - **Analogia Fisica:** Ricordando che la somma dei pesi è unitaria ($\sum p_X(y) = 1$), $\mathbb{E}[X]$ rappresenta esattamente l'ascissa del **baricentro** di un sistema di masse puntiformi distribuite lungo la retta reale.

> [!tip]- Flashcard: Definizione di Valore Atteso
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Basic
Front: Come viene definito formalmente il valore atteso $\mathbb{E}[X]$ di una variabile aleatoria discreta e qual è la sua interpretazione fisica?
Back: Il valore atteso è definito da $\mathbb{E}[X] := \sum_{y \in \mathbb{R}} y \, p_X(y) = \sum_{y \in \mathbb{R}} y \, \mathbb{P}(X=y)$. Rappresenta la media ponderata dei valori assunti dalla variabile pesati con le rispettive probabilità, corrispondendo fisicamente al baricentro delle masse di probabilità distribuite sulla retta reale.
Tags: education/university education/math math/probability
END
%%

### Esempi Fondamentali di Calcolo del Valore Atteso

> [!example] Esempio 1: Gioco d'Azzardo con Dado ed Equità della Scommessa
> - **Regola del gioco:** Uno scommettitore punta $5€$ sul lancio di un dado a 6 facce non truccato ($\Omega = \{1, 2, 3, 4, 5, 6\}$). Se esce il numero $6$, lo scommettitore riscuote un premio lordo di $30€$; se esce qualsiasi altro numero ($\{1, 2, 3, 4, 5\}$), riscuote $0€$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=3|Appunti p. 3]]].
> - **Variabile aleatoria vincita lorda $X$:**
>   $$X(j) = \begin{cases} 30 & \text{se } j = 6 \\ 0 & \text{se } j \in \{1, 2, 3, 4, 5\} \end{cases}$$
> - **Funzione di densità $p_X(y)$:**
>   $$p_X(y) = \begin{cases} 5/6 & \text{se } y = 0 \\ 1/6 & \text{se } y = 30 \\ 0 & \text{se } y \notin \{0, 30\} \end{cases}$$
> - **Calcolo del valore atteso:** Rimuovendo i termini nulli ($0 \cdot p_X(0) = 0$):
>   $$\mathbb{E}[X] = 0 \cdot \frac{5}{6} + 30 \cdot \frac{1}{6} = 0 + 5 = 5€$$
> - **Interpretazione:** Il valore atteso della vincita lorda è esattamente pari a $5€$, che eguaglia il costo della puntata iniziale. Il gioco è pertanto **equo** (valore atteso del guadagno netto nullo: $\mathbb{E}[X - 5] = 5 - 5 = 0$).

> [!example] Esempio 2: Valore Atteso della Funzione Indicatrice (Bernoulli)
> - Sia $X = \mathbb{1}_A$ la funzione indicatrice di un evento $A \subseteq \Omega$ con probabilità $\mathbb{P}(A) = p$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=3|Appunti p. 3]]], \[[[Dispense Statistica e Probabilità.pdf#page=118|Dispense p. 112]]].
> - Applicando direttamente la definizione:
>   $$\mathbb{E}[\mathbb{1}_A] = \sum_{y \in \{0, 1\}} y \, p_{\mathbb{1}_A}(y) = 0 \cdot \mathbb{P}(A^c) + 1 \cdot \mathbb{P}(A) = \mathbb{P}(A)$$
> - Questo risultato stabilisce un'identità cardine: **il valore atteso della funzione indicatrice di un evento coincide esattamente con la probabilità dell'evento stesso**:
>   $$\mathbb{E}[\mathbb{1}_A] = \mathbb{P}(A) = p$$

> [!tip]- Flashcard: Valore Atteso dell'Indicatrice
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Cloze
Text: Il valore atteso della funzione indicatrice $\mathbb{1}_A$ di un evento $A$ è pari a {{c1::$\mathbb{E}[\mathbb{1}_A] = \mathbb{P}(A)$}}.
Extra: Dimostrazione immediata: $\mathbb{E}[\mathbb{1}_A] = 0 \cdot \mathbb{P}(A^c) + 1 \cdot \mathbb{P}(A) = \mathbb{P}(A)$.
Tags: education/university education/math math/probability
END
%%

---

## 5. Proprietà di Linearità del Valore Atteso e Applicazione alla Binomiale

### Il Teorema di Linearità dell'Operatore Valore Atteso
La proprietà computazionale più potente del valore atteso è la sua linearità \[[[Proprietà delle Variabili Aleatorie.pdf#page=4|Appunti p. 4]]], \[[[Dispense Statistica e Probabilità.pdf#page=118|Dispense p. 114]]], \[[[Calcolo delle Probabilità.pdf#page=164|Ross p. 145]]]:

> [!summary] Teorema: Linearità del Valore Atteso
> Siano $X$ e $Y$ due variabili aleatorie qualsiasi definite sullo stesso spazio campionario $\Omega$ aventi valore atteso finito, e siano $a, b \in \mathbb{R}$ costanti scalari. Allora la combinazione lineare $aX + bY$ ammette valore atteso e vale:
> $$\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$$
> In particolare:
> 1. **Omogeneità:** $\mathbb{E}[aX] = a\mathbb{E}[X]$
> 2. **Additività:** $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$
> 3. **Costante scalare:** $\mathbb{E}[c] = c$ per ogni $c \in \mathbb{R}$.

> [!info] Osservazione Fondamentale sull'Indipendenza
> L'additività del valore atteso $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ **non richiede alcuna ipotesi di indipendenza stocastica** tra le variabili $X$ e $Y$. Essa è una proprietà puramente algebrica dell'integrale e delle serie rispetto alla misura di probabilità.

> [!abstract]- Dimostrazione Formale Passo-Passo: Linearità dell'Operatore Somma
> - **Idea chiave:** Esprimere il valore atteso della somma sommando su tutti gli esiti elementari $\omega \in \Omega$ pesati con la probabilità di ciascun punto.
> - **Passo 1 (Definizione su $\Omega$):** Sia $\Omega$ discreto con esiti $\omega$. Il valore atteso di una variabile trasformata $Z = X + Y$ è:
>   $$\mathbb{E}[X + Y] = \sum_{\omega \in \Omega} (X(\omega) + Y(\omega)) \, \mathbb{P}(\{\omega\})$$
> - **Passo 2 (Proprietà distributiva reale):** Distribuendo il fattore $\mathbb{P}(\{\omega\})$:
>   $$\sum_{\omega \in \Omega} (X(\omega) + Y(\omega)) \, \mathbb{P}(\{\omega\}) = \sum_{\omega \in \Omega} X(\omega)\mathbb{P}(\{\omega\}) + \sum_{\omega \in \Omega} Y(\omega)\mathbb{P}(\{\omega\})$$
> - **Passo 3 (Riconoscimento delle componenti):** Le due sommatorie corrispondono esattamente alle definizioni di $\mathbb{E}[X]$ e $\mathbb{E}[Y]$:
>   $$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y] \quad \blacksquare$$

> [!tip]- Flashcard: Linearità del Valore Atteso
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Cloze
Text: L'operatore valore atteso è lineare: per ogni costante $a, b \in \mathbb{R}$ e variabili $X, Y$, vale {{c1::$\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$}}. Tale additività {{c2::NON richiede l'indipendenza stocastica}} tra $X$ e $Y$.
Extra: La linearità consente di calcolare il valore atteso di somme complesse senza ricorrere alla densità congiunta.
Tags: education/university education/math math/probability
END
%%

### Calcolo Immediato del Valore Atteso della Variabile Binomiale
Nel calcolare il valore atteso di una variabile binomiale $X \sim Bi(n, p)$, il calcolo analitico diretto richiederebbe la valutazione della serie:
$$\mathbb{E}[X] = \sum_{j=0}^n j \, \mathbb{P}(X = j) = \sum_{j=0}^n j \binom{n}{j} p^j (1 - p)^{n-j}$$
che implica artifici algebrici sulla formula del coefficiente binomiale \[[[Proprietà delle Variabili Aleatorie.pdf#page=4|Appunti p. 4]]].

Sfruttando invece la linearità del valore atteso e la scomposizione in somma di indicatrici di Bernoulli, il calcolo diviene immediato:
- Si scrive la variabile binomiale $X$ come somma di $n$ prove di Bernoulli $X = \sum_{i=1}^n \mathbb{1}_{A_i}$, dove ciascun evento $A_i$ (successo nell'$i$-esima prova) ha probabilità $\mathbb{P}(A_i) = p$.
- Applicando l'operatore $\mathbb{E}$:
  $$\mathbb{E}[X] = \mathbb{E}\left[\sum_{i=1}^n \mathbb{1}_{A_i}\right] = \sum_{i=1}^n \mathbb{E}[\mathbb{1}_{A_i}]$$
- Poiché per l'Esempio 2 abbiamo $\mathbb{E}[\mathbb{1}_{A_i}] = \mathbb{P}(A_i) = p$:
  $$\mathbb{E}[X] = \sum_{i=1}^n p = n p$$

> [!summary] Proposizione: Valore Atteso della Distribuzione Binomiale
> Se $X \sim Bi(n, p)$, il suo valore atteso è dato direttamente dal prodotto:
> $$\mathbb{E}[X] = n p$$

> [!tip]- Flashcard: Valore Atteso della Binomiale via Linearità
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Basic
Front: Come si ricava il valore atteso di una variabile binomiale $X \sim Bi(n,p)$ sfruttando la linearità?
Back: Si scompone $X$ nella somma di $n$ variabili indicatrici di Bernoulli $X = \sum_{i=1}^n \mathbb{1}_{A_i}$ con $\mathbb{P}(A_i)=p$. Per linearità, $\mathbb{E}[X] = \sum_{i=1}^n \mathbb{E}[\mathbb{1}_{A_i}] = \sum_{i=1}^n p = np$, evitando il calcolo diretto della sommatoria combinatoria.
Tags: education/university education/math math/probability
END
%%

---

## 6. Variabile Aleatoria Geometrica: Tempo di Primo Successo

### Modello Operativo e Formalizzazione Analitica
Si consideri una successione potenzialmente illimitata di prove di Bernoulli indipendenti ed identicamente distribuite $A_1, A_2, \dots, A_n, \dots$, ciascuna con probabilità di successo costante $\mathbb{P}(A_i) = p \in (0, 1)$ e insuccesso $q = 1 - p$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=4|Appunti pp. 4–5]]], \[[[Calcolo delle Probabilità.pdf#page=193|Ross p. 174]]].

> [!danger] Definizione: Variabile Aleatoria Geometrica (Tempo di Primo Successo)
> Si definisce **tempo di primo successo** (o variabile aleatoria geometrica) la variabile aleatoria $T: \Omega \to \mathbb{N}^+$ che conta l'indice della prova in cui si verifica per la prima volta l'evento successo:
> $$T(\omega) := \inf \{j \in \mathbb{N}^+ \mid \omega \in A_j\}$$
> - **Evento $\{T = j\}$:** Il primo successo si verifica esattamente alla prova $j$ se e solo se nelle prime $j-1$ prove si sono verificati solo insuccessi e alla prova $j$ si ottiene il successo:
>   $$\{T = j\} = A_1^c \cap A_2^c \cap \dots \cap A_{j-1}^c \cap A_j, \quad j \ge 1$$
> - **Trattazione d'aula su orizzonte limitato $n$:** Negli appunti d'aula \[[[Proprietà delle Variabili Aleatorie.pdf#page=5|Appunti p. 5]]], il docente ha analizzato lo schema in cui l'esperimento viene arrestato dopo al più $n$ tentativi. In tal caso, $T$ assume valori in $\{1, 2, \dots, n, n+1\}$, dove l'esito $T = n+1$ codifica l'evento "nessun successo nelle $n$ prove":
>   $$\{T = n+1\} = A_1^c \cap A_2^c \cap \dots \cap A_n^c$$

### Funzione di Densità di Probabilità Discreta
Poiché le prove sono stocasticamente indipendenti ([[02 - Insieme delle Parti, Assiomi della Probabilità e Spazi Finiti]]), la probabilità dell'intersezione coincide con il prodotto delle probabilità:
- Per $j \in \{1, \dots, n\}$:
  $$\mathbb{P}(T = j) = \mathbb{P}(A_1^c) \cdot \mathbb{P}(A_2^c) \cdots \mathbb{P}(A_{j-1}^c) \cdot \mathbb{P}(A_j) = (1 - p)^{j-1} p$$
- Per il caso di mancato successo fino alla prova $n$:
  $$\mathbb{P}(T = n+1) = \mathbb{P}(A_1^c \cap \dots \cap A_n^c) = (1 - p)^n$$

> [!summary] Funzione di Massa della Variabile Geometrica
> - **Caso classico a supporto illimitato ($T \in \mathbb{N}^+$):**
>   $$p_T(j) = \mathbb{P}(T = j) = (1 - p)^{j-1} p, \quad j = 1, 2, 3, \dots$$
> - **Caso tronco a $n+1$ valori:**
>   $$p_T(y) = \begin{cases} (1 - p)^{y-1} p & \text{se } y \in \{1, 2, \dots, n\} \\ (1 - p)^n & \text{se } y = n+1 \\ 0 & \text{altrove} \end{cases}$$

> [!tip]- Flashcard: Densità della Variabile Geometrica
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Basic
Front: Qual è la densità di probabilità $p_T(j)$ della variabile geometrica $T$ (tempo di primo successo) e da quale proprietà scaturisce?
Back: La densità è $p_T(j) = \mathbb{P}(T=j) = (1-p)^{j-1}p$ per $j \ge 1$. Scaturisce dall'indipendenza stocastica delle prove, che consente di moltiplicare la probabilità dei $j-1$ fallimenti consecutivi $(1-p)^{j-1}$ per la probabilità del successo all'$j$-esima prova $p$.
Tags: education/university education/math math/probability
END
%%

### Calcolo del Valore Atteso Mediante Derivazione della Serie Geometrica
Il calcolo di $\mathbb{E}[T]$ rappresenta una delle applicazioni analitiche più eleganti del corso, basata sul metodo della derivazione termine a termine rispetto al parametro $p$ \[[[Proprietà delle Variabili Aleatorie.pdf#page=5|Appunti p. 5]]], \[[[Calcolo delle Probabilità.pdf#page=194|Ross p. 175]]].

> [!summary] Teorema: Valore Atteso della Variabile Geometrica
> Data una variabile aleatoria geometrica $T \sim \mathcal{G}(p)$ a supporto numerabile illimitato ($p \in (0, 1]$), il suo valore atteso vale:
> $$\mathbb{E}[T] = \frac{1}{p}$$
> - **Significato Intuitivo:** Se un evento ha probabilità $p = 1/6$ (es. estrazione del $6$ al dado), il numero medio atteso di lanci necessari per osservare il primo $6$ è $\mathbb{E}[T] = \frac{1}{1/6} = 6$ lanci.

> [!abstract]- Dimostrazione Formale Passo-Passo: Calcolo di $\mathbb{E}[T]$ tramite Derivata della Serie Geometrica
> - **Idea chiave:** Riconoscere che il fattore $j(1-p)^{j-1}$ è proporzionale all'opposto della derivata prima di $(1-p)^j$ rispetto a $p$.
> - **Passo 1 (Impostazione della sommatoria):** Per definizione di valore atteso su supporto $\mathbb{N}^+$:
>   $$\mathbb{E}[T] = \sum_{j=1}^\infty j \, p_T(j) = \sum_{j=1}^\infty j (1 - p)^{j-1} p = p \sum_{j=1}^\infty j (1 - p)^{j-1}$$
> - **Passo 2 (Identità differenziale):** Derivando la potenza rispetto alla variabile $p$:
>   $$\frac{d}{dp}\left((1 - p)^j\right) = j(1 - p)^{j-1} \cdot (-1) = -j(1 - p)^{j-1} \iff j(1 - p)^{j-1} = -\frac{d}{dp}\left((1 - p)^j\right)$$
> - **Passo 3 (Scambio sommatoria-derivata):** Sostituendo nella serie ed estraendo l'operatore differenziale lineare (lecito per convergenza uniforme della serie geometrica con $|1-p| < 1$, si veda [[06 - Valore Assoluto, Numeri Naturali e Principio di Induzione]]):
>   $$\mathbb{E}[T] = p \sum_{j=1}^\infty \left(-\frac{d}{dp}(1 - p)^j\right) = -p \frac{d}{dp}\left(\sum_{j=1}^\infty (1 - p)^j\right)$$
> - **Passo 4 (Somma della serie geometrica):** Ponendo $q = 1 - p \in (0, 1)$, la serie geometrica che parte da $j=1$ vale:
>   $$\sum_{j=1}^\infty q^j = \frac{q}{1 - q} = \frac{1 - p}{1 - (1 - p)} = \frac{1 - p}{p} = \frac{1}{p} - 1$$
> - **Passo 5 (Calcolo della derivata):** Calcolando la derivata rispetto a $p$:
>   $$\frac{d}{dp}\left(\frac{1}{p} - 1\right) = -\frac{1}{p^2}$$
> - **Passo 6 (Conclusione algebrica):** Moltiplicando per il coefficiente $-p$:
>   $$\mathbb{E}[T] = -p \cdot \left(-\frac{1}{p^2}\right) = \frac{p}{p^2} = \frac{1}{p} \quad \blacksquare$$
> - **Nota sul caso tronco d'aula:** Nel caso troncato a $n+1$ analizzato a lezione \[[[Proprietà delle Variabili Aleatorie.pdf#page=5|Appunti p. 5]]]:
>   $$\mathbb{E}[T] = \sum_{j=1}^n j(1-p)^{j-1}p + (n+1)(1-p)^n = -p \frac{d}{dp}\left(\sum_{j=1}^n (1-p)^j\right) + (n+1)(1-p)^n$$
>   all'aumentare di $n \to +\infty$, il termine residuo $(n+1)(1-p)^n$ decade esponenzialmente a zero, ripristinando il valore atteso asintotico $1/p$.

> [!tip]- Flashcard: Valore Atteso della Geometrica
%%
TARGET DECK: University::Probabilità e Statistica::13 - Variabili Aleatorie Discrete, Densità di Probabilità, Valore Atteso e Distribuzione Geometrica
START
Cloze
Text: Il valore atteso di una variabile geometrica $T \sim \mathcal{G}(p)$ che conta il tempo di primo successo vale {{c1::$\mathbb{E}[T] = \frac{1}{p}$}}.
Extra: Si ricava elegantemente sfruttando l'identità differenziale $j(1-p)^{j-1} = -\frac{d}{dp}((1-p)^j)$ e la somma della serie geometrica.
Tags: education/university education/math math/probability
END
%%
