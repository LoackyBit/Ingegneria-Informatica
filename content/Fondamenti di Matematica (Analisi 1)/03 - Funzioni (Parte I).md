---
status: permanent
type: lecture
area: education
related: ["[[Fondamenti di Matematica (Analisi 1) MOC]]", "[[Ingegneria Informatica 2026 - 27 MOC]]", "[[University]]", "[[Metodo di Studio - PACRAR]]", "[[01 - Logica Proposizionale, Predicati e Metodi di Dimostrazione]]", "[[02 - Teoria degli Insiemi]]", "[[01 - Teoria degli Insiemi, Spazio Campionario e Prime Nozioni di Probabilità]]"]
aliases: ["Lezione 3 Fondamenti di Matematica", "FdM Lezione 3", "Coppie Ordinate, Relazioni e Funzioni", "Funzioni (Parte 1)"]
source: Lezione 3 FdM del 25/09/2026 - Prof. Saverio Salzo
title: "03 - Coppie Ordinate, Relazioni e Funzioni"
date: '2026-09-25'
updated: 2026-09-28T07:54
tags: [education/university, education/math, tech/logic]
summary: "Coppie ordinate di Kuratowski, prodotto cartesiano assiomatico, relazioni binarie e grafi, funzioni come terne, immagini dirette, controimmagini e famiglie."
course: "Fondamenti di Matematica Analisi 1"
sources: ["[[Lezione 3 FdM.pdf]]"]
---
[[Home MOC|Home]] / [[University|University MOC]] / [[Fondamenti di Matematica (Analisi 1) MOC]] / [[03 - Funzioni (Parte I)]]

# 03 - Coppie Ordinate, Relazioni e Funzioni

- **Docente:** Prof. Saverio Salzo / Canale A-L
- **Data Lezione:** 2026-09-25
- **Materiali Didattici Ufficiali:** \[[[Lezione 3 FdM.pdf#page=1|Dispensa Lezione 03 — Funzioni (parte I) (Prof. Salzo)]]]
- **Riferimento MOC:** [[Fondamenti di Matematica (Analisi 1) MOC]], [[Ingegneria Informatica 2026 - 27 MOC]]
- **Lezione Precedente:** [[02 - Teoria degli Insiemi]]
- **Collegamento Interdisciplinare:** [[01 - Teoria degli Insiemi, Spazio Campionario e Prime Nozioni di Probabilità]] (in cui prodotti cartesiani, relazioni binarie e funzioni indicatrici fondano lo spazio degli esiti $\Omega$, gli eventi aleatori e le variabili aleatorie)

La terza lezione di Fondamenti di Matematica compie il passaggio fondamentale dalla pura algebra insiemistica statica alla teoria delle strutture e delle corrispondenze. Nella [[02 - Teoria degli Insiemi|teoria assiomatica degli insiemi ZF]], gli enti non possiedono un ordine intrinseco: in virtù dell'assioma di estensionalità, la coppia non ordinata $\{x, y\}$ coincide invariabilmente con $\{y, x\}$.

Per consentire lo sviluppo della geometria analitica, del calcolo infinitesimale e dell'informatica teorica, è indispensabile disporre di collezioni ordinate di elementi in cui la prima coordinata sia distinguibile dalla seconda senza alcuna ambiguità. L'obiettivo centrale della lezione è definire la <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>coppia ordinata</b></font></mark> come oggetto puramente insiemistico (secondo la costruzione di Kuratowski), ricavare assiomaticamente il <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>prodotto cartesiano</b></font></mark>, formalizzare le <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>relazioni binarie</b></font></mark> e giungere alla nozione rigorosa di <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>funzione</b></font></mark> come terna ordinata con relazione funzionale univoca \[[[Lezione 3 FdM.pdf#page=1|Dispensa p. 1]]].

---

## 1. Coppie Ordinate e Relazioni

Nella lezione precedente abbiamo visto che, dati due insiemi $x$ e $y$, l'assioma della coppia non ordinata assicura l'esistenza dell'insieme $\{x, y\}$. In tale insieme l'ordine di elencazione è privo di significato matematico:
$$\{x, y\} = \{y, x\}$$
Tale uguaglianza discende direttamente dall'assioma di estensionalità: un generico elemento $z$ appartiene a $\{x, y\}$ se e solo se $z = x \lor z = y$, che è logicamente equivalente a $z = y \lor z = x$.

Per definire punti su un piano o sequenze di istruzioni occorre un oggetto che distingua l'ordine: scambiando l'ordine degli elementi, l'oggetto risultante deve cambiare (a meno che i due elementi non coincidano). Anziché introdurre un nuovo assioma primitivo, la teoria ZF definisce la coppia ordinata per via puramente costruttiva a partire dagli assiomi già consolidati.

### Definizione di Kazimierz Kuratowski

La costruzione canonica universalmente adottata nella matematica moderna è dovuta al matematico polacco <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>Kazimierz Kuratowski</b></font></mark> (1921) \[[[Lezione 3 FdM.pdf#page=1|Dispensa p. 1]]].

> [!danger] Definizione 1.1: Coppia Ordinata (Kuratowski)
> Siano $x$ e $y$ insiemi. Si definisce **coppia ordinata** avente come prima coordinata $x$ e come seconda coordinata $y$ l'insieme:
> $$(x, y) := \{\{x\}, \{x, y\}\}$$

La validità e l'esistenza formale di tale oggetto nella teoria ZF poggia esclusivamente su applicazioni ripetute dell'assioma della coppia non ordinata:
1. Dato $x$, l'assioma della coppia garantisce l'esistenza del singoletto $\{x\} = \{x, x\}$;
2. Dati $x$ e $y$, l'assioma della coppia garantisce l'esistenza della coppia non ordinata $\{x, y\}$;
3. Dati gli insiemi $\{x\}$ e $\{x, y\}$, una terza applicazione dell'assioma della coppia garantisce l'esistenza dell'insieme delle due parti: $\{\{x\}, \{x, y\}\}$.

L'asimmetria strutturale della definizione è evidente: l'elemento $x$ compare in entrambi i sottoinsiemi (sia nel singoletto $\{x\}$ sia nella coppia $\{x, y\}$), mentre $y$ compare esclusivamente nella coppia $\{x, y\}$. La presenza del singoletto $\{x\}$ serve proprio come "ancora" identificativa per isolare in modo univoco la prima coordinata rispetto alla seconda.

Nel caso particolare in cui le due coordinate coincidano ($x = y$), la definizione restituisce:
$$(x, x) = \{\{x\}, \{x, x\}\} = \{\{x\}, \{x\}\} = \{\{x\}\}$$
La coppia ordinata di elementi uguali $(x, x)$ è dunque un singoletto contenente un singoletto, e possiede un unico elemento: $\{x\}$.

> [!tip]- Flashcard: Definizione di Coppia Ordinata di Kuratowski
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Come viene definita costruttivamente la coppia ordinata $(x, y)$ secondo Kazimierz Kuratowski nella teoria assiomatica degli insiemi ZF?
Back: La coppia ordinata con prima coordinata $x$ e seconda coordinata $y$ è definita come:
$$(x, y) := \{\{x\}, \{x, y\}\}$$
È un insieme costituito da due elementi (il singoletto della prima coordinata $\{x\}$ e la coppia non ordinata $\{x, y\}$), la cui esistenza deriva da applicazioni successive dell'assioma della coppia.
Tags: education/university education/math tech/logic
<!--ID: 1790873652719-->
END> %%

### Proprietà Caratteristica della Coppia Ordinata

Affinché la definizione di Kuratowski sia matematicamente soddisfacente, essa deve garantire la proprietà fondamentale delle coppie ordinate: due coppie sono uguali se e solo se coincidono ordinatamente le rispettive coordinate \[[[Lezione 3 FdM.pdf#page=1|Dispensa p. 1]]].

> [!summary] Proposizione 1.3: Proprietà Caratteristica della Coppia Ordinata
> Siano $x, y, a, b$ insiemi. Allora:
> $$(x, y) = (a, b) \iff x = a \land y = b$$

> [!info] Dimostrazione Formale
> - **Implicazione $(\impliedby)$:** Se $x = a$ e $y = b$, allora banalmente $\{x\} = \{a\}$ e $\{x, y\} = \{a, b\}$, da cui $\{\{x\}, \{x, y\}\} = \{\{a\}, \{a, b\}\}$, ossia $(x, y) = (a, b)$.
> 
> - **Implicazione $(\implies)$:** Supponiamo per ipotesi $(x, y) = (a, b)$, cioè:
>   $$\{\{x\}, \{x, y\}\} = \{\{a\}, \{a, b\}\}$$
>   Distinguiamo due casi mutuamente esclusivi in base alla natura di $x$ e $y$:
>   - **Caso 1: $x = y$.**
>     In tal caso $(x, y) = \{\{x\}\}$, un insieme che possiede un solo elemento. Poiché per ipotesi $(a, b) = (x, y)$, anche $(a, b) = \{\{a\}, \{a, b\}\}$ deve possedere un solo elemento. Per l'assioma di estensionalità deve risultare $\{a\} = \{a, b\} = \{x\}$.
>     Dall'uguaglianza $\{a\} = \{x\}$ segue $a = x$. Dall'uguaglianza $\{a, b\} = \{x\}$ segue che ogni elemento di $\{a, b\}$ deve essere uguale a $x$, dunque anche $b = x$.
>     Concludiamo che $a = x$ e $b = x = y$, ossia $x = a$ e $y = b$.
>   - **Caso 2: $x \ne y$.**
>     In tal caso $\{x\} \ne \{x, y\}$, poiché $y \in \{x, y\}$ ma $y \notin \{x\}$. Dunque $(x, y)$ possiede esattamente due elementi distinti: il singoletto $\{x\}$ e la coppia non ordinata $\{x, y\}$.
>     Poiché per ipotesi $(a, b) = (x, y)$, anche $(a, b)$ deve possedere due elementi distinti, il che implica $a \ne b$.
>     Applicando l'assioma di estensionalità tra i due insiemi a due elementi $\{\{x\}, \{x, y\}\}$ e $\{\{a\}, \{a, b\}\}$, l'unico singoletto a sinistra deve coincidere con l'unico singoletto a destra:
>     $$\{x\} = \{a\} \implies x = a$$
>     Di conseguenza, la coppia non ordinata con due elementi a sinistra deve coincidere con la coppia a due elementi a destra:
>     $$\{x, y\} = \{a, b\}$$
>     Poiché sappiamo già che $x = a$, affinché i due insiemi siano identici l'elemento restante deve coincidere: $y = b$.
>     In entrambi i casi si deduce $x = a \land y = b$. $\blacksquare$

> [!tip]- Flashcard: Proprietà Caratteristica della Coppia Ordinata
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: Siano $x, y, a, b$ insiemi. La proprietà caratteristica della coppia ordinata stabilisce che {{c1::$ (x, y) = (a, b) \iff x = a \land y = b $}}.
Extra: Se $x \ne y$, scambiando l'ordine degli elementi si ottiene una coppia distinta: $(x, y) \ne (y, x)$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652721-->
END> %%

### Generalizzazione a Terne e $n$-uple Ordinate

A partire dalla definizione di coppia ordinata, è possibile definire per ricorsione collezioni ordinate con un numero arbitrario di elementi \[[[Lezione 3 FdM.pdf#page=4|Dispensa p. 4]]].

> [!danger] Definizione: Terna Ordinata
> Siano $x, y, z$ insiemi. Si definisce **terna ordinata** formata da $x, y, z$ la coppia ordinata avente come prima coordinata la coppia $(x, y)$ e come seconda coordinata $z$:
> $$(x, y, z) := ((x, y), z)$$

In modo analogo, per qualsiasi $n \ge 3$, la $n$-upla ordinata $(x_1, x_2, \dots, x_n)$ è definita ricorsivamente come la coppia ordinata:
$$(x_1, x_2, \dots, x_n) := ((x_1, x_2, \dots, x_{n-1}), x_n)$$

> [!tip]- Flashcard: Definizione di Terna Ordinata
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Come si definisce formalmente una terna ordinata $(x, y, z)$ nella teoria degli insiemi?
Back: La terna ordinata si definisce ricorsivamente come una coppia ordinata in cui la prima coordinata è a sua volta una coppia ordinata:
$$(x, y, z) := ((x, y), z)$$
Tags: education/university education/math tech/logic
<!--ID: 1790873652722-->
END> %%

---

## 2. Il Prodotto Cartesiano

Dati due insiemi $A$ e $B$, intendiamo collezionare tutte le coppie ordinate aventi la prima coordinata in $A$ e la seconda coordinata in $B$.

Come discusso a lezione dal docente, nella teoria assiomatica ZF non è lecito definire un insieme scrivendo semplicemente $\{(x, y) \mid x \in A \land y \in B\}$ senza specificare il dominio di appartenenza delle coppie, poiché l'[[02 - Teoria degli Insiemi#5. Assioma di Specificazione|assioma di specificazione]] richiede tassativamente un insieme "universo" da cui estrarre gli elementi mediante un predicato logico \[[[Lezione 3 FdM.pdf#page=2|Dispensa p. 2]]].

### Deduzione Rigorosa dell'Universo di Estrazione

Per individuare l'universo appropriato, analizziamo la struttura insiemistica della generica coppia ordinata $(x, y) = \{\{x\}, \{x, y\}\}$ con $x \in A$ e $y \in B$:
1. Per definizione di [[02 - Teoria degli Insiemi#8. Assioma dell'Unione e Unione di Insiemi|unione]]:
   $$x \in A \land y \in B \implies x \in A \cup B \land y \in A \cup B$$
2. Di conseguenza, sia il singoletto $\{x\}$ sia la coppia $\{x, y\}$ sono sottoinsiemi di $A \cup B$:
   $$\{x\} \subset A \cup B \quad \land \quad \{x, y\} \subset A \cup B$$
3. Per la definizione di [[02 - Teoria degli Insiemi#11. Assioma dell'Insieme Potenza (Insieme delle Parti)|insieme delle parti]] $\mathcal{P}(A \cup B)$, essere sottoinsieme equivale ad appartenere all'insieme potenza:
   $$\{x\} \in \mathcal{P}(A \cup B) \quad \land \quad \{x, y\} \in \mathcal{P}(A \cup B)$$
4. Ne consegue che la coppia ordinata $(x, y) = \{\{x\}, \{x, y\}\}$, essendo costituita da elementi di $\mathcal{P}(A \cup B)$, è essa stessa un sottoinsieme dell'insieme delle parti:
   $$(x, y) \subset \mathcal{P}(A \cup B)$$
5. Applicando nuovamente la definizione di insieme delle parti, se $(x, y) \subset \mathcal{P}(A \cup B)$, allora $(x, y)$ è un elemento dell'insieme delle parti dell'insieme delle parti:
   $$(x, y) \in \mathcal{P}(\mathcal{P}(A \cup B))$$

Questo dimostra in modo ineccepibile che tutte le coppie ordinate con prima coordinata in $A$ e seconda coordinata in $B$ appartengono all'universo preesistente $\mathcal{P}(\mathcal{P}(A \cup B))$.

> [!danger] Definizione 1.4: Prodotto Cartesiano
> Siano $A$ e $B$ insiemi. Si definisce **prodotto cartesiano** di $A$ e $B$, e si denota con $A \times B$, l'insieme:
> $$A \times B := \{z \in \mathcal{P}(\mathcal{P}(A \cup B)) \mid (\exists x \in A)(\exists y \in B)(z = (x, y))\}$$

> [!info] Osservazione 1.5: Notazione Semplificata
> Chiarito il rigore assiomatico a monte, per comodità espositiva si adotta il consueto abuso di notazione:
> $$A \times B = \{(x, y) \mid x \in A \land y \in B\}$$

> [!tip]- Flashcard: Universo Assiomatico del Prodotto Cartesiano
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: In quale insieme universo preesistente vivono le coppie ordinate del prodotto cartesiano $A \times B$ secondo l'assioma di specificazione?
Back: Vivono nell'insieme delle parti dell'insieme delle parti dell'unione:
$$(x, y) \in \mathcal{P}(\mathcal{P}(A \cup B))$$
Poiché $x, y \in A \cup B \implies \{x\}, \{x, y\} \in \mathcal{P}(A \cup B) \implies (x, y) \subset \mathcal{P}(A \cup B) \implies (x, y) \in \mathcal{P}(\mathcal{P}(A \cup B))$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652723-->
END> %%

### Rappresentazione Geometrica ed Esempi

Il termine "cartesiano" richiama l'impostazione geometrica introdotta da René Descartes (Cartesio): gli elementi di $A$ sono disposti lungo un asse orizzontale e quelli di $B$ lungo un asse verticale ortogonale. Ogni coppia $(x, y) \in A \times B$ individua un punto sul piano identificato dall'intersezione delle coordinate \[[[Lezione 3 FdM.pdf#page=2|Dispensa p. 2]]].

> [!example] Esempio 1.6: Prodotti Cartesiani Finiti e Infiniti
> 1. **Insiemi finiti:** Siano $A = \{a, b, c\}$ e $B = \{d, e\}$. Allora:
>    $$A \times B = \{(a, d), (a, e), (b, d), (b, e), (c, d), (c, e)\}$$
>    L'insieme consta di $3 \times 2 = 6$ elementi.
> 2. **Intervalli reali continui:** Siano $A = [1, 4]$ e $B = [2, 3]$ due sottoinsiemi di $\mathbb{R}$. Il prodotto cartesiano $A \times B = [1, 4] \times [2, 3]$ rappresenta geometricamente il rettangolo pieno nel piano $\mathbb{R}^2$ avente come base il segmento $[1, 4]$ e come altezza il segmento $[2, 3]$.

### Cardinalità del Prodotto Cartesiano

Nel caso di insiemi finiti di cardinalità $|A| = n$ e $|B| = m$, il numero di elementi del prodotto cartesiano è dato dal principio fondamentale del calcolo combinatorio:
$$|A \times B| = |A| \cdot |B| = n \cdot m$$
Per scegliere una coppia $(x, y)$, vi sono $n$ scelte possibili e indipendenti per la prima coordinata $x \in A$, e per ciascuna di esse vi sono $m$ scelte indipendenti per la seconda coordinata $y \in B$. Trattandosi di scelte tra loro indipendenti, le possibilità complessive si moltiplicano.

> [!tip]- Flashcard: Cardinalità del Prodotto Cartesiano
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: Siano $A$ e $B$ due insiemi finiti di cardinalità $\vert A\vert = n$ e $\vert B\vert = m$. La cardinalità del loro prodotto cartesiano è {{c1::$ \vert A \times B\vert = \vert A\vert \cdot \vert B\vert = n \cdot m $}}.
Extra: Deriva dal principio combinatorio delle estrazioni con ripetizione: $n$ scelte indipendenti per la prima coordinata moltiplicate per $m$ scelte per la seconda.
Tags: education/university education/math tech/logic
<!--ID: 1790873652724-->
END> %%

---

## 3. Relazioni Binarie e Corrispondenze

Il concetto di prodotto cartesiano permette di formalizzare in modo rigoroso qualsiasi legame tra oggetti matematici.

> [!danger] Definizione 1.7: Relazione Binaria, Notazione Infissa e Dominio
> Siano $A$ e $B$ due insiemi. Si definisce **relazione** (o corrispondenza) tra $A$ e $B$ un qualsiasi sottoinsieme del loro prodotto cartesiano:
> $$R \subset A \times B$$
> Se $(x, y) \in R$, si dice che $x$ è in relazione con $y$ secondo $R$, e si scrive:
> $$x \xrightarrow{R} y$$
> Una relazione tra $A$ e se stesso ($R \subset A \times A$) si chiama **relazione (binaria) su $A$**. In tal caso, per denotare che $(x, y) \in R$ si impiega comunemente la **notazione infissa**:
> $$x R y$$
> Si definisce **dominio** della relazione $R$ il sottoinsieme degli elementi di $A$ che ammettono almeno un corrispondente in $B$:
> $$\operatorname{dom}(R) := \{x \in A \mid (\exists y \in B)((x, y) \in R)\}$$

> [!tip]- Flashcard: Definizione di Relazione Binaria e Dominio
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Come si definisce una relazione binaria $R$ tra due insiemi $A$ e $B$ e qual è il suo dominio $\operatorname{dom}(R)$?
Back: Una relazione binaria tra $A$ e $B$ è un qualsiasi sottoinsieme del prodotto cartesiano:
$$R \subset A \times B$$
Il dominio di $R$ è l'insieme degli elementi del primo insieme che sono in relazione con almeno un elemento del secondo:
$$\operatorname{dom}(R) := \{x \in A \mid (\exists y \in B)((x, y) \in R)\}$$
Tags: education/university education/math tech/logic
<!--ID: 1790873652725-->
END> %%

### Esempi Notabili di Relazioni

> [!example] Esempio 1.8: Relazione di Parentela
> Sia $A$ l'insieme di tutti gli esseri umani viventi. Consideriamo la relazione $R \subset A \times A$ definita da:
> $$x R y \iff x \text{ è genitore di } y$$
> Il dominio $\operatorname{dom}(R)$ di questa relazione non coincide con l'intero insieme $A$, poiché vi sono persone viventi che non hanno figli: $\operatorname{dom}(R) \subsetneq A$ \[[[Lezione 3 FdM.pdf#page=3|Dispensa p. 3]]].

> [!example] Esempio 1.9: Grafi Orientati come Relazioni Binarie
> Nella teoria dei grafi e nell'informatica teorica, un <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>grafo orientato</b></font></mark> (o *directed graph*) è una coppia ordinata $G = (V, E)$, dove:
> - $V$ è un insieme non vuoto di elementi detti **vertici** (o nodi);
> - $E \subset V \times V$ è una relazione binaria su $V$, i cui elementi sono detti **archi orientati** (o frecce).
> Quando $(x, y) \in E$, si scrive $x \xrightarrow{E} y$, a indicare che esiste un arco che punta dal vertice $x$ al vertice $y$ \[[[Lezione 3 FdM.pdf#page=3|Dispensa p. 3]]].

> [!tip]- Flashcard: Grafi Orientati come Relazioni Binarie
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Qual è la definizione insiemistica rigorosa di un grafo orientato $G = (V, E)$?
Back: Un grafo orientato è una coppia $G = (V, E)$ in cui $V$ è l'insieme dei vertici e l'insieme degli archi $E$ è una relazione binaria su $V$:
$$E \subset V \times V$$
Ogni arco orientato $(u, v) \in E$ è una coppia ordinata che esprime la relazione $u \xrightarrow{E} v$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652726-->
END> %%

### Conteggio Combinatorio delle Relazioni su Insiemi Finiti

Un quesito fondamentale posto dal docente a lezione riguarda il numero totale di relazioni binarie costruibili su un insieme finito:

> Se un insieme $A$ consta di $n$ elementi, quante relazioni binarie distinte si possono definire su $A$?

1. Il prodotto cartesiano $A \times A$ contiene $n \cdot n = n^2$ coppie ordinate distinte.
2. Poiché una relazione $R$ su $A$ è, per definizione, un *qualunque* sottoinsieme di $A \times A$, l'insieme di tutte le possibili relazioni su $A$ coincide con l'[[02 - Teoria degli Insiemi#11. Assioma dell'Insieme Potenza (Insieme delle Parti)|insieme delle parti]] del prodotto cartesiano: $\mathcal{P}(A \times A)$.
3. La cardinalità cercata è quindi:
   $$|\mathcal{P}(A \times A)| = 2^{|A \times A|} = 2^{n^2}$$

Per esempio, se $|A| = 4$ elementi:
- Il prodotto cartesiano contiene $|A \times A| = 4^2 = 16$ coppie ordinate;
- Il numero di relazioni binarie possibili (ossia il numero di grafi orientati distinti con 4 vertici) è:
  $$2^{16} = 65536$$

> [!info] Perché la base è 2? Corrispondenza con le Funzioni Indicatrici
> Come spiegato con insistenza dal prof. Salzo, la base $2$ non deriva dal fatto che le coppie sono formate da $2$ elementi!
> La base $2$ discende dal fatto che una proposizione logica ammette due soli valori di verità: Vero ($1$) o Falso ($0$).
> Per definire un sottoinsieme $R \subset A \times A$, dobbiamo decidere per ciascuna delle $n^2$ coppie se essa appartiene o meno alla relazione:
> - Scelta 1: la coppia $(x, y) \in R$ (valore $1$ / sì);
> - Scelta 2: la coppia $(x, y) \notin R$ (valore $0$ / no).
> Vi sono dunque 2 scelte indipendenti per ciascuna delle $n^2$ coppie, il che genera $2 \times 2 \times \dots \times 2 = 2^{n^2}$ configurazioni binarie possibili.

> [!tip]- Flashcard: Numero di Relazioni Binarie su un Insieme Finito
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: Sia $A$ un insieme finito con $\vert A\vert = n$ elementi. Il numero totale di relazioni binarie distinte definibili su $A$ è {{c1::$ 2^{n^2} $}}.
Extra: Poiché una relazione è un sottoinsieme di $A \times A$, il loro numero coincide con la cardinalità dell'insieme delle parti $\vert\mathcal{P}(A \times A)\vert = 2^{\vert A\vert^2}$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652727-->
END> %%

---

## 4. Definizione Generale di Funzione

Nella scuola secondaria, una funzione viene spesso presentata con formule del tipo: *"una legge che ad ogni elemento di $A$ fa corrispondere uno e un solo elemento di $B$"*.

Come rimarcato criticamente dal docente, l'espressione "legge" è priva di cittadinanza nella teoria assiomatica degli insiemi: in matematica esistono assiomi, definizioni, insiemi e relazioni, ma il concetto di "legge" non è né primitivo né definito.
Per conferire pieno rigore logico, nella teoria ZF una <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>funzione</b></font></mark> viene definita come una particolare terna ordinata formata da insiemi \[[[Lezione 3 FdM.pdf#page=4|Dispensa p. 4]]].

> [!danger] Definizione 2.1: Funzione (Applicazione) e Relazione Funzionale
> Siano $A$ e $B$ insiemi. Si chiama **funzione** (o **applicazione**) da $A$ a $B$ una terna ordinata:
> $$f = (A, B, R)$$
> dove $R \subset A \times B$ è una **relazione funzionale** tra $A$ e $B$, cioè tale che:
> $$(\forall x \in A)(\exists! y \in B)((x, y) \in R)$$
> Questa condizione di unicità esistenziale equivale al verificarsi simultaneo di due proprietà distinte:
> 1. **Esistenza (o Totalità del Dominio):**
>    $$(\forall x \in A)(\exists y \in B)((x, y) \in R) \iff \operatorname{dom}(R) = A$$
> 2. **Unicità (o Univocità):**
>    $$(\forall x \in A)(\forall y_1, y_2 \in B)(((x, y_1) \in R \land (x, y_2) \in R) \implies y_1 = y_2)$$

Dalla definizione emergono i termini e le notazioni standard:
- L'unico elemento $y \in B$ tale che $(x, y) \in R$ si indica con il simbolo $f(x)$ e si chiama <mark style="background:rgba(181, 113, 255, 0.36)"><font color="#9a54c1"><b>immagine di $x$ mediante $f$</b></font></mark>;
- Se $(x, y) \in R$, si scrive $x \stackrel{f}{\mapsto} y$ oppure $x \mapsto f(x)$;
- La generica funzione da $A$ a $B$ si indica con la notazione compatta:
  $$f: A \to B$$
- L'insieme $A$ si chiama **dominio** (o insieme di partenza) della funzione;
- L'insieme $B$ si chiama **codominio** (o insieme di arrivo) della funzione;
- L'insieme di tutte le funzioni possibili da $A$ a $B$ si denota con:
  $$B^A$$

> [!tip]- Flashcard: Definizione Formale di Funzione come Terna Ordinata
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Qual è la definizione assiomatica rigorosa di una funzione $f$ da $A$ a $B$ nella teoria degli insiemi?
Back: Una funzione è una terna ordinata $f = (A, B, R)$ dove $R \subset A \times B$ è una relazione funzionale che soddisfa:
$$(\forall x \in A)(\exists! y \in B)((x, y) \in R)$$
Cioè: ad ogni elemento del dominio $A$ corrisponde uno ed un solo elemento del codominio $B$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652728-->
END> %%

> [!tip]- Flashcard: Condizioni di Esistenza e Unicità di una Funzione
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: La relazione funzionale $R \subset A \times B$ di una funzione $f = (A, B, R)$ soddisfa due condizioni:
1. Esistenza (totalità): {{c1::$ (\forall x \in A)(\exists y \in B)((x, y) \in R) $}} (ossia $\operatorname{dom}(R) = A$);
2. Unicità (univocità): {{c2::$ (\forall x \in A)(\forall y_1, y_2 \in B)(((x, y_1) \in R \land (x, y_2) \in R) \implies y_1 = y_2) $}}.
Extra: Se da un punto $x$ non parte alcuna freccia (mancata esistenza) o partono due frecce distinte (mancata unicità), $R$ non è una funzione.
Tags: education/university education/math tech/logic
<!--ID: 1790873652729-->
END> %%

### Cardinalità dell'Insieme delle Funzioni $B^A$

Se $A$ e $B$ sono insiemi finiti di cardinalità $|A| = n$ e $|B| = m$, quante funzioni distinte appartengono a $B^A$?
- Per il primo elemento $x_1 \in A$, vi sono $m$ scelte possibili per $f(x_1) \in B$;
- Per il secondo elemento $x_2 \in A$, vi sono $m$ scelte indipendenti per $f(x_2) \in B$;
- Reiterando per tutti gli $n$ elementi di $A$, si ottiene:
  $$|B^A| = |B|^{|A|} = m^n$$

Questo risultato combinatorio giustifica pienamente la notazione esponenziale $B^A$ per l'insieme delle funzioni!

> [!info] Il Caso delle Funzioni Indicatrici
> Se consideriamo come codominio l'insieme binario $B = \{0, 1\}$, l'insieme delle funzioni $\{0, 1\}^A$ ha cardinalità:
> $$|\{0, 1\}^A| = 2^{|A|}$$
> Ogni sottoinsieme $E \subset A$ è univocamente identificato dalla sua <mark style="background:rgba(255, 193, 69, 0.32)"><font color="#cc8800"><b>funzione indicatrice</b></font></mark> (o caratteristica) $\chi_E: A \to \{0, 1\}$:
> $$\chi_E(x) = \begin{cases} 1 & \text{se } x \in E \\ 0 & \text{se } x \notin E \end{cases}$$
> La corrispondenza biunivoca tra $\mathcal{P}(A)$ e $\{0, 1\}^A$ dimostra in modo naturale perché $|\mathcal{P}(A)| = 2^{|A|}$.

> [!tip]- Flashcard: Cardinalità dell'Insieme delle Funzioni
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Qual è la cardinalità dell'insieme delle funzioni $B^A$ tra due insiemi finiti e quale connessione sussiste con l'insieme delle parti?
Back: La cardinalità è $\vert B^A\vert = \vert B\vert^{\vert A\vert} = m^n$, dove $n = \vert A\vert$ e $m = \vert B\vert$.
Nel caso speciale $B = \{0, 1\}$, le funzioni $\{0, 1\}^A$ sono le funzioni indicatrici dei sottoinsiemi di $A$, la cui cardinalità è $2^{\vert A\vert} = \vert\mathcal{P}(A)\vert$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652730-->
END> %%

---

## 5. Grafico di una Funzione

Nella definizione $f = (A, B, R)$, la relazione funzionale $R$ contiene tutte le coppie $(x, f(x))$. Tale relazione coincide con il grafico della funzione \[[[Lezione 3 FdM.pdf#page=5|Dispensa p. 5]]].

> [!info] Osservazione 2.2: Grafico di una Funzione
> Sia $f: A \to B$ una funzione. La sua relazione funzionale $R$ si può riscrivere come:
> $$R = \{z \in A \times B \mid (\exists x \in A)(z = (x, f(x)))\} = \{(x, f(x)) \in A \times B \mid x \in A\}$$
> Tale insieme si chiama **grafico** della funzione $f$ e si denota con $G_f$.

Poiché la relazione funzionale $R = G_f$ è univocamente determinata dai valori $f(x)$ assunti da $f$ su $A$, per assegnare una funzione è sufficiente specificare il dominio $A$, il codominio $B$ e la legge che associa ad ogni $x \in A$ il valore $f(x)$.

### Criterio Geometrico della Retta Verticale

Quando $A, B \subset \mathbb{R}$, il grafico $G_f$ è un sottoinsieme del piano cartesiano $\mathbb{R}^2$.
La condizione di funzionalità si traduce nel noto **test della retta verticale**:
- Un sottoinsieme $G \subset A \times \mathbb{R}$ è il grafico di una funzione $f: A \to \mathbb{R}$ se e solo se **ogni retta verticale $x = x_0$ con $x_0 \in A$ interseca $G$ in uno ed un solo punto**.
- Se per un certo $x_0 \in A$ la retta verticale non incontra la curva, cade la condizione di esistenza ($\operatorname{dom}(f) \ne A$);
- Se una retta verticale interseca la curva in due o più punti distinti (come nel caso della circonferenza $x^2 + y^2 = r^2$), cade la condizione di unicità e la curva non rappresenta una funzione.

> [!tip]- Flashcard: Grafico di una Funzione e Test della Retta Verticale
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Come si definisce formalmente il grafico $G_f$ di una funzione $f: A \to B$ e qual è il significato geometrico del test della retta verticale?
Back: Il grafico è il sottoinsieme del prodotto cartesiano formato dalle coppie $(x, f(x))$:
$$G_f := \{(x, f(x)) \in A \times B \mid x \in A\}$$
Geometricamente, ogni retta verticale $x = x_0$ (con $x_0 \in A$) deve intersecare il grafico in esattamente un punto: l'intersezione garantisce l'esistenza di $f(x_0)$, l'unicità del punto garantisce l'univocità del valore.
Tags: education/university education/math tech/logic
<!--ID: 1790873652731-->
END> %%

---

## 6. Funzioni Notevoli e Dominio Massimale

> [!example] Esempio 2.3: Funzione Identità e Iniezione Canonica
> 1. **Funzione Identità:** Sia $A$ un insieme. La funzione $i_A: A \to A$ definita ponendo per ogni $x \in A$:
>    $$i_A(x) = x$$
>    si chiama **funzione identità** di $A$. Formalmente si definisce come la terna $i_A = (A, A, \Delta_A)$, dove $\Delta_A$ è la diagonale di $A \times A$:
>    $$\Delta_A := \{(x, x) \in A \times A \mid x \in A\}$$
> 2. **Iniezione (o Immersione) Canonica:** Sia $A$ un insieme e sia $X \subset A$ un suo sottoinsieme. La funzione $j_X: X \to A$ definita da:
>    $$(\forall x \in X) \, j_X(x) = x$$
>    si chiama **iniezione canonica** (o immersione) di $X$ in $A$. Formalmente essa è la terna $j_X = (X, A, R)$, dove $R = \{(x, x) \in X \times A \mid x \in X\}$ \[[[Lezione 3 FdM.pdf#page=6|Dispensa p. 6]]].

> [!info] Osservazione 2.4: Dominio Naturale (o Massimale)
> Spesso nell'analisi reale una funzione viene introdotta fornendo unicamente la sua espressione analitica $f(x)$ (es. $f(x) = \sqrt{x^2 - 1}$), omettendo il dominio.
> In tali circostanze si sottintende convenzionalmente che il dominio sia il **dominio naturale** (o massimale), ossia il più grande sottoinsieme di $\mathbb{R}$ per il quale l'operazione ha senso matematico.

> [!tip]- Flashcard: Funzione Identità e Iniezione Canonica
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Qual è la differenza formale tra la funzione identità $i_A$ e l'iniezione canonica $j_X$ di un sottoinsieme $X \subset A$?
Back: Entrambe associano ogni elemento a se stesso ($x \mapsto x$), ma differiscono per dominio e codominio:
- L'identità ha dominio e codominio coincidenti: $i_A: A \to A$;
- L'iniezione canonica ha come dominio il sottoinsieme $X$ e come codominio l'insieme contenitore $A$: $j_X: X \to A$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652732-->
END> %%

---

## 7. Immagine Diretta e Controimmagine

Data una funzione $f: A \to B$, è possibile trasformare non solo singoli elementi, ma interi sottoinsiemi mediante due operazioni duali \[[[Lezione 3 FdM.pdf#page=6|Dispensa p. 6]]].

> [!danger] Definizione 2.5: Immagine Diretta e Controimmagine
> Sia $f: A \to B$ una funzione. Siano $X \subset A$ e $Y \subset B$.
> 1. Si definisce **immagine (diretta)** di $X$ mediante $f$ il sottoinsieme di $B$:
>    $$f(X) := \{y \in B \mid (\exists x \in X)(f(x) = y)\} = \{f(x) \in B \mid x \in X\}$$
>    In particolare, l'insieme $f(A) \subset B$ si chiama **immagine della funzione $f$** (denotata anche con $\operatorname{Im}(f)$).
> 2. Si definisce **controimmagine** (o **immagine inversa**, o **preimmagine**) di $Y$ mediante $f$ il sottoinsieme di $A$:
>    $$f^{-1}(Y) := \{x \in A \mid f(x) \in Y\}$$

> [!warning] Avvertenza Notazionale Critica
> La scrittura $f^{-1}(Y)$ denota la controimmagine di un *sottoinsieme* del codominio ed è **sempre ben definita per qualunque funzione $f$**.
> Essa non richiede affatto che la funzione $f$ sia invertibile o biiettiva. La funzione inversa $f^{-1}$ (come operazione puntuale tra elementi) verrà introdotta solo per funzioni biiettive, mentre la controimmagine insiemistica $f^{-1}(Y)$ esiste incondizionatamente.

> [!tip]- Flashcard: Immagine Diretta e Controimmagine
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: Data una funzione $f: A \to B$, se $X \subset A$ e $Y \subset B$:
- L'immagine diretta di $X$ è {{c1::$ f(X) := \{y \in B \mid (\exists x \in X)(f(x) = y)\} $}};
- La controimmagine di $Y$ è {{c2::$ f^{-1}(Y) := \{x \in A \mid f(x) \in Y\} $}}.
Extra: $f(X)$ è un sottoinsieme del codominio $B$, mentre $f^{-1}(Y)$ è un sottoinsieme del dominio $A$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652733-->
END> %%

> [!example] Esempio 2.6: Calcolo di Immagine e Controimmagine
> Siano $A = \{1, 2, 3\}$ e $B = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$.
> Sia $f: A \to B$ la funzione definita da $f(x) = x^2 + 1$.
> - Calcoliamo i valori puntuali: $f(1) = 2$, $f(2) = 5$, $f(3) = 10$.
> - Se $X = \{1, 2\}$, l'immagine diretta è:
>   $$f(X) = \{f(1), f(2)\} = \{2, 5\}$$
> - Se $Y = \{5, 6, 7, 8, 9, 10\}$, la controimmagine è l'insieme degli $x \in A$ tali che $f(x) \in Y$:
>   $$f^{-1}(Y) = \{2, 3\}$$
>   (poiché $f(2) = 5 \in Y$ e $f(3) = 10 \in Y$, mentre $f(1) = 2 \notin Y$).

> [!tip]- Flashcard: Esempio di Controimmagine
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Se $f: \{1, 2, 3\} \to \{1, \dots, 10\}$ è definita da $f(x) = x^2 + 1$, quali sono $f(\{1, 2\})$ e $f^{-1}(\{5, 6, 7, 8, 9, 10\})$?
Back: - L'immagine diretta è $f(\{1, 2\}) = \{f(1), f(2)\} = \{2, 5\}$;
- La controimmagine è $f^{-1}(\{5, 6, 7, 8, 9, 10\}) = \{2, 3\}$, poiché $f(2) = 5 \in Y$ e $f(3) = 10 \in Y$, mentre $f(1) = 2 \notin Y$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652734-->
END> %%

---

## 8. Proprietà Algebriche di Immagini e Controimmagini

L'interazione tra immagini, controimmagini e le operazioni booleane di unione e intersezione rivela un'asimmetria profonda tra il comportamento in avanti e all'indietro \[[[Lezione 3 FdM.pdf#page=7|Dispensa p. 7]]].

> [!summary] Proposizione 2.7: Proprietà Fondamentali di Immagini e Controimmagini
> Siano $f: A \to B$ una funzione, $X, X_1, X_2 \subset A$ e $Y, Y_1, Y_2 \subset B$. Allora valgono le seguenti proprietà:
> 1. **Monotonia:**
>    - $X_1 \subset X_2 \implies f(X_1) \subset f(X_2)$
>    - $Y_1 \subset Y_2 \implies f^{-1}(Y_1) \subset f^{-1}(Y_2)$
> 2. **Conservazione dell'Unione:**
>    - $f(X_1 \cup X_2) = f(X_1) \cup f(X_2)$
>    - $f^{-1}(Y_1 \cup Y_2) = f^{-1}(Y_1) \cup f^{-1}(Y_2)$
> 3. **Comportamento rispetto all'Intersezione (Asimmetria):**
>    - $f(X_1 \cap X_2) \subset f(X_1) \cap f(X_2)$ (inclusione in generale stretta!)
>    - $f^{-1}(Y_1 \cap Y_2) = f^{-1}(Y_1) \cap f^{-1}(Y_2)$ (uguaglianza esatta!)
> 4. **Composizione di Immagine e Controimmagine:**
>    - $X \subset f^{-1}(f(X))$
>    - $f(f^{-1}(Y)) \subset Y$

> [!tip]- Flashcard: Proprietà di Conservazione di Immagini e Controimmagini
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: Siano $f: A \to B$, $X_1, X_2 \subset A$ e $Y_1, Y_2 \subset B$.
- Rispetto all'unione: {{c1::$ f(X_1 \cup X_2) = f(X_1) \cup f(X_2) $}} e {{c1::$ f^{-1}(Y_1 \cup Y_2) = f^{-1}(Y_1) \cup f^{-1}(Y_2) $}};
- Rispetto all'intersezione: {{c2::$ f(X_1 \cap X_2) \subset f(X_1) \cap f(X_2) $}} mentre {{c2::$ f^{-1}(Y_1 \cap Y_2) = f^{-1}(Y_1) \cap f^{-1}(Y_2) $}}.
Extra: La controimmagine preserva perfettamente sia l'unione che l'intersezione, mentre l'immagine diretta preserva l'unione ma per l'intersezione garantisce solo l'inclusione.
Tags: education/university education/math tech/logic
<!--ID: 1790873652735-->
END> %%

### Analisi dell'Asimmetria dell'Intersezione e Controesempio

La ragione per cui l'immagine diretta non conserva in generale l'uguaglianza sull'intersezione risiede nella possibile non-iniettività della funzione.

> [!example] Controesempio: Mancata Uguaglianza per $f(X_1 \cap X_2)$
> Consideriamo la funzione $f: \mathbb{R} \to \mathbb{R}$ definita da $f(x) = x^2$.
> Siano $X_1 = [-2, 0]$ e $X_2 = [0, 2]$:
> - L'intersezione dei domini è il singoletto $X_1 \cap X_2 = \{0\}$, la cui immagine è:
>   $$f(X_1 \cap X_2) = f(\{0\}) = \{0\}$$
> - Calcoliamo separatamente le immagini:
>   $$f(X_1) = f([-2, 0]) = [0, 4], \quad f(X_2) = f([0, 2]) = [0, 4]$$
> - L'intersezione delle immagini è:
>   $$f(X_1) \cap f(X_2) = [0, 4] \cap [0, 4] = [0, 4]$$
> Poiché $\{0\} \subsetneq [0, 4]$, risulta chiaramente:
> $$f(X_1 \cap X_2) \subsetneq f(X_1) \cap f(X_2)$$

L'uguaglianza $f(X_1 \cap X_2) = f(X_1) \cap f(X_2)$ vale per ogni coppia di sottoinsiemi se e solo se la funzione $f$ è iniettiva.

Al contrario, la controimmagine preserva perfettamente l'intersezione grazie alla rigorosa equivalenza logica dei predicati:
$$x \in f^{-1}(Y_1 \cap Y_2) \iff f(x) \in (Y_1 \cap Y_2) \iff (f(x) \in Y_1 \land f(x) \in Y_2) \iff (x \in f^{-1}(Y_1) \land x \in f^{-1}(Y_2)) \iff x \in f^{-1}(Y_1) \cap f^{-1}(Y_2)$$

> [!tip]- Flashcard: Asimmetria dell'Intersezione nell'Immagine Diretta
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Perché per l'immagine diretta vale solo $f(X_1 \cap X_2) \subset f(X_1) \cap f(X_2)$ e non l'uguaglianza? Fornire un controesempio.
Back: L'uguaglianza può fallire se la funzione fa collidere elementi distinti di $X_1 \setminus X_2$ e $X_2 \setminus X_1$ nello stesso valore.
Esempio: $f(x) = x^2$ con $X_1 = \{-1\}$ e $X_2 = \{1\}$.
$X_1 \cap X_2 = \emptyset \implies f(X_1 \cap X_2) = \emptyset$.
Ma $f(X_1) = \{1\}$ e $f(X_2) = \{1\} \implies f(X_1) \cap f(X_2) = \{1\} \ne \emptyset$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652736-->
END> %%

### Analisi delle Composizioni $f^{-1}(f(X))$ e $f(f^{-1}(Y))$

1. **Proprietà $X \subset f^{-1}(f(X))$:**
   Se $x \in X$, allora per definizione $f(x) \in f(X)$. Ma se $f(x) \in f(X)$, per definizione di controimmagine $x \in f^{-1}(f(X))$.
   L'inclusione può essere stretta se vi sono elementi fuori da $X$ che hanno la stessa immagine di elementi di $X$ (funzione non iniettiva). Vale l'uguaglianza per ogni $X$ se e solo se $f$ è iniettiva.

2. **Proprietà $f(f^{-1}(Y)) \subset Y$:**
   Se $y \in f(f^{-1}(Y))$, esiste $x \in f^{-1}(Y)$ tale che $y = f(x)$. Ma per definizione di controimmagine, $x \in f^{-1}(Y)$ significa $f(x) \in Y$, da cui $y \in Y$.
   L'inclusione può essere stretta se vi sono elementi in $Y$ che non vengono raggiunti dalla funzione (funzione non suriettiva). Vale l'uguaglianza per ogni $Y$ se e solo se $f$ è suriettiva; in generale vale l'identità:
   $$f(f^{-1}(Y)) = Y \cap f(A)$$

> [!tip]- Flashcard: Inclusioni di Immagine e Controimmagine Composte
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: Siano $f: A \to B$, $X \subset A$ e $Y \subset B$. Valgono sempre le inclusioni:
- {{c1::$ X \subset f^{-1}(f(X)) $}} (con uguaglianza se e solo se $f$ è iniettiva);
- {{c2::$ f(f^{-1}(Y)) \subset Y $}} (con uguaglianza se e solo se $f$ è suriettiva, valendo in generale $f(f^{-1}(Y)) = Y \cap f(A)$).
Tags: education/university education/math tech/logic
<!--ID: 1790873652737-->
END> %%

---

## 9. Restrizione di una Funzione

Spesso è necessario limitare l'azione di una funzione a una porzione del suo dominio originale \[[[Lezione 3 FdM.pdf#page=7|Dispensa p. 7]]].

> [!danger] Definizione 2.8: Restrizione di una Funzione
> Sia $f: A \to B$ una funzione e sia $X \subset A$. Si chiama **restrizione** di $f$ a $X$, e si denota con $f|_X$, la funzione:
> $$f|_X: X \to B \quad \text{tale che} \quad (\forall x \in X) \, f|_X(x) = f(x)$$
> In termini formali, se $f = (A, B, R)$, la restrizione è la terna ordinata $f|_X = (X, B, R|_X)$, dove:
> $$R|_X := \{(x, y) \in R \mid x \in X\} = R \cap (X \times B)$$

La restrizione possiede la medesima legge e lo stesso codominio della funzione originaria, ma agisce su un dominio più piccolo.

> [!tip]- Flashcard: Definizione di Restrizione di una Funzione
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Basic
Front: Come si definisce formalmente la restrizione $f\vert_X$ di una funzione $f: A \to B$ a un sottoinsieme $X \subset A$?
Back: La restrizione è la funzione $f\vert_X: X \to B$ che agisce solo sugli elementi di $X$ mantenendo inalterata la legge:
$$(\forall x \in X) \, f\vert_X(x) = f(x)$$
In termini di relazione funzionale: $R\vert_X = \{(x, y) \in R \mid x \in X\} = R \cap (X \times B)$.
Tags: education/university education/math tech/logic
<!--ID: 1790873652738-->
END> %%

---

## 10. Famiglie di Elementi e Famiglie di Parti

Nella pratica matematica avanzata e nell'analisi, le successioni numeriche, le collezioni di insiemi e le serie sono formalizzate come particolari funzioni il cui dominio funge da insieme di indici \[[[Lezione 3 FdM.pdf#page=7|Dispensa p. 7]]].

> [!danger] Definizione 2.9: Famiglia di Elementi
> Siano $I$ e $A$ due insiemi. Una funzione $a: I \to A$ si chiama **famiglia di elementi di $A$ indicizzata da $I$**.
> In tale contesto:
> - L'immagine dell'indice $i \in I$ mediante $a$ si denota con $a_i$ anziché $a(i)$;
> - La funzione stessa si denota con il simbolo $(a_i)_{i \in I}$;
> - Il dominio $I$ si chiama **insieme degli indici** della famiglia.

Se $I = \mathbb{N}$, la famiglia $(a_n)_{n \in \mathbb{N}}$ prende il nome di **successione** di elementi di $A$.

### Famiglie di Parti e Operazioni Generalizzate

Quando gli elementi della famiglia sono a loro volta insiemi (cioè sottoinsiemi di un dato insieme $A$), la funzione assume valori nell'insieme delle parti \[[[Lezione 3 FdM.pdf#page=7|Dispensa p. 7]]].

> [!danger] Definizione 2.10: Famiglia di Parti, Unione e Intersezione Generalizzata
> Siano $I$ e $A$ due insiemi. Una funzione $F: I \to \mathcal{P}(A)$ si chiama **famiglia di parti di $A$** e si denota con $(F_i)_{i \in I}$.
> Si definiscono l'**unione** e l'**intersezione** della famiglia $(F_i)_{i \in I}$ rispettivamente come:
> $$\bigcup_{i \in I} F_i := \{x \in A \mid (\exists i \in I)(x \in F_i)\}$$
> $$\bigcap_{i \in I} F_i := \{x \in A \mid (\forall i \in I)(x \in F_i)\}$$

Le nozioni di unione e intersezione per famiglie arbitrarie estendono le operazioni binarie a collezioni con un numero infinito di insiemi, costituendo il pilastro su cui poggeranno la topologia di $\mathbb{R}$, la teoria della misura e l'analisi infinitesimale.

> [!tip]- Flashcard: Famiglie di Parti e Operazioni Generalizzate
%%
TARGET DECK: University::Fondamenti di Matematica (Analisi 1)::03 - Coppie Ordinate, Relazioni e Funzioni
START
Cloze
Text: Data una famiglia di parti $(F_i)_{i \in I}$ con $F_i \subset A$:
- L'unione della famiglia è {{c1::$ \bigcup_{i \in I} F_i := \{x \in A \mid (\exists i \in I)(x \in F_i)\} $}};
- L'intersezione della famiglia è {{c2::$ \bigcap_{i \in I} F_i := \{x \in A \mid (\forall i \in I)(x \in F_i)\} $}}.
Extra: Un elemento appartiene all'unione se appartiene ad almeno un insieme della famiglia; appartiene all'intersezione se appartiene a tutti gli insiemi della famiglia.
Tags: education/university education/math tech/logic
<!--ID: 1790873652739-->
END> %%

---
---SUMMARY---
Coppie ordinate di Kuratowski, prodotto cartesiano assiomatico, relazioni binarie e grafi, funzioni come terne, immagini dirette, controimmagini e famiglie.
