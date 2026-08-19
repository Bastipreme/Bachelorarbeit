# Vergleich eines dedizierten Reflexionsbots und eines generischen KI-Systems zur Unterstützung von Lernprozessen im Software-Prozessmanagement

Bachelorarbeit, Software Engineering, Hochschule Heilbronn (HHN), 2026.

**[Arbeit lesen (PDF, 97 Seiten)](Thesis/main.pdf)**

## Worum es geht

Studierende nutzen generative KI längst auch für Aufgaben, die eine eigene Begründung verlangen. Diese Arbeit fragt, ob ein KI-System, das gezielt für Reflexion statt für schnelle Antworten gebaut ist, daran etwas ändert. Dazu wurde ein **Reflexionsbot** entwickelt, der keine Lösungen ausgibt, sondern sokratisch nachfragt und die Tiefe seiner Rückfragen an die Qualität der studentischen Antwort anpasst.

Erprobt wurde er in einem Mini-Experiment in der Lehrveranstaltung „Grundlagen des Software Engineering 1“. Eine Gruppe bearbeitete zwei Prozessszenarien mit dem Reflexionsbot, eine Vergleichsgruppe mit einem frei gewählten Consumer-System (ChatGPT, Gemini oder Claude). Die Szenarien sind bewusst **Dilemmata ohne eindeutig richtige Lösung**: ein reguliertes ML-Projekt (*SmartDose*) und ein verteiltes Team (*LearnLoop*).

Ausgewertet wurde in einem konvergenten Mixed-Methods-Design: 31 Bearbeitungen und die zugehörigen Chatverläufe wurden qualitativ nach dem Reflexionsstufenmodell von Hatton und Smith kodiert, ergänzt um **Autorenschaft als eigene Dimension**, und mit einem Prä-Post-Survey (n=22 bzw. n=20) zusammengeführt.

Der zentrale Befund fällt vorsichtiger aus als die Ausgangserwartung: Das Systemdesign schlägt sich im **Nutzungsverhalten** nieder, nicht in den **Lernmaßen**.

## Ergebnisse

### Autorenschaft der Bearbeitungen

| Autorenschaft | Team AI (n=15) | Reflexionsbot (n=16) |
|---|---|---|
| studentisch | 3 | 8 |
| unklar | 4 | 1 |
| KI-generiert | 8 | 7 |
| **nicht eindeutig studentisch** | **12 (80 %)** | **8 (50 %)** |

Der Abstand von 80 % zu 50 % ist die auffälligste Zahl der Arbeit — und die am stärksten einzuschränkende. Team AI war durch die Teilaufgabe „AI Analysis“ **verpflichtet**, die eigenen Entscheidungen in ein generisches System einzugeben; ein Teil der KI-Artefakte ist damit durch die Aufgabenstellung selbst angelegt. Hinzu kommt, dass der Reflexionsbot einen Chatexport bereitstellte, während die Vergleichsgruppe manuell sichern musste — und das Vorliegen eines Chatlogs geht als Indikator in die Kodierung ein. Betrachtet man nur die **gesichert** KI-generierten Fälle, schrumpft der Unterschied auf 8 von 15 gegenüber 7 von 16.

### Reflexionstiefe (nur studentisch verfasste Bearbeitungen)

| Stufe | Team AI (n=3) | Reflexionsbot (n=8) |
|---|---|---|
| 0 — keine Reflexion, Verweigerung | 1 | 4 |
| 1 — deskriptives Schreiben | 0 | 3 |
| 2 — deskriptive Reflexion | 2 | 0 |
| 3 — dialogische Reflexion | 0 | 1 |
| 4 — kritische Reflexion | 0 | 0 |
| **Mittelwert** | **1,33** | **0,75** |

Auf dem Konstrukt, das der Reflexionsbot gezielt fördern soll, liegt die Vergleichsgruppe deskriptiv **höher**. Bei drei gegenüber acht auswertbaren Fällen trägt das keine Richtungsaussage — ein einzelner Fall verschiebt den Mittelwert um mehr als 0,3 Stufen, und die drei Team-AI-Fälle sind der Rest einer Gruppe, aus der 80 % ausgeschieden sind. Festzuhalten bleibt: Ein Vorteil des Reflexionsbots zeigt sich hier nicht.

### Wissenstest und Selbsteinschätzung

Der objektive Wissenstest (0–6 Punkte) lässt **keine Aussage** zu. Beide Gruppen liegen bereits im Prä-Test bei rund 5,5 von 6 Punkten, ein Deckeneffekt verhindert die Abbildung von Zuwächsen. Die Reflexionsbot-Gruppe fällt von 5,56 auf 4,44 (n=9), die Generic-AI-Gruppe bleibt bei 5,43 (n=7); etwa die Hälfte des Rückgangs entfällt auf einen einzelnen Fall.

Im Survey ergibt sich ein gegenläufiges Bild:

| Item (1–5) | Reflexionsbot | Generic AI |
|---|---|---|
| Kompetenzentwicklung | 3,10 | 2,80 |
| war hilfreicher als erwartet | 3,40 | 2,20 |
| würde ich erneut nutzen | 2,50 | 3,20 |
| hätte das andere System bevorzugt | 3,30 | 2,20 |

Der Reflexionsbot wird günstiger bewertet und zugleich seltener wieder gewählt. Beim selbsteingeschätzten Verständnis für Begründen und Abwägen bleibt er stabil, während die Vergleichsgruppe sinkt.

### Was daraus folgt

Nicht das Werkzeug entscheidet, sondern ob sich jemand darauf einlässt. Ein erheblicher Teil der Reflexionsbot-Gruppe wich den Rückfragen aus oder versuchte gezielt, das System zu einer Direktantwort zu bewegen — in drei dokumentierten Fällen mit Erfolg. Gutes Design schafft die Gelegenheit zur Reflexion, es erzwingt sie nicht.

Kapitel 5 berichtet alle Messwerte, Kapitel 6 interpretiert sie, benennt die Grenzen und leitet in Abschnitt 6.4 sechs Handlungsempfehlungen für die Lehre ab.

## Repository-Struktur

```
├── Thesis/                    LaTeX-Quellen und main.pdf
│   ├── main.tex               Einstiegspunkt
│   ├── einleitung.tex … anhang.tex
│   ├── Literatur.bib          IEEE, 64 Einträge
│   └── img/
├── Chatbot/                   Implementierung des Reflexionsbots
│   ├── Chatbot.py             Streamlit-App, Systemnachricht, Sitzungsverwaltung
│   ├── Dockerfile             Container, über den die App in der Übung lief
│   ├── docker-compose.yml
│   └── requirements.txt       streamlit 1.57.0, openai 2.36.0
└── Experiment/                Erhebungsmaterialien
    ├── Scenario 1|2 for Team-AI / Team-Reflexionsbot
    ├── Pre-Survey_English.txt, Post-Survey_English.txt
    └── create_google_form.gs, create_post_google_form.gs
```

Die Systemnachricht des Bots ist vollständig in Anhang A.7 der Arbeit abgedruckt, die Szenarien in Anhang A.4, die Fragebögen in Anhang A.5.

## Rohdaten

**Die Rohdaten des Mini-Experiments sind nicht Teil dieses Repositorys.** Die eingereichten Bearbeitungen, die Chatverläufe und die beiden Survey-Exporte enthalten pseudonymisierte, aber nicht anonymisierte Angaben von 22 Teilnehmenden aus einer einzelnen Übungsgruppe. Bei dieser Gruppengröße lässt sich eine Re-Identifikation über die Merkmalskombination nicht ausschließen, und die Einwilligung deckte die Teilnahme an der Übung ab, keine Veröffentlichung.

Sie liegen ausschließlich dem digitalen Anhang der eingereichten Fassung bei. Die vollständige Kodierung aller 31 Fälle ist in Anhang A.2 der Arbeit nachvollziehbar dokumentiert, die deskriptive Statistik aller Fragebogenitems in Anhang A.6.

## Nachvollziehen

Die Arbeit kompiliert mit `texlive-full` und `latexmk`, ohne Python:

```bash
cd Thesis && latexmk -pdf main.tex
```

Der Reflexionsbot braucht einen OpenAI-API-Schlüssel. Er wird über `st.secrets` gelesen, die Datei `.streamlit/secrets.toml` ist bewusst nicht im Repository:

```bash
cd Chatbot
mkdir -p .streamlit
echo 'OPENAI_API_KEY = "sk-..."' > .streamlit/secrets.toml
pip install -r requirements.txt
streamlit run Chatbot.py
```

Alternativ über Docker, hier wird der Schlüssel als Umgebungsvariable übergeben:

```bash
cd Chatbot
OPENAI_API_KEY=sk-... docker compose up --build   # http://localhost:8501
```

Eingesetztes Modell war `gpt-4o-mini`. Die virtuelle Umgebung (`.venv`) ist nicht eingecheckt.

## Rechte

Dieses Repository ist zur Nachvollziehbarkeit der Bachelorarbeit veröffentlicht, nicht als lizenzierte Software. Das Urheberrecht an Code, Text und Abbildungen liegt beim Autor; für eine Nutzung darüber hinaus bitte vorher Kontakt aufnehmen.

Ausgenommen ist das Logo der Hochschule Heilbronn (`Thesis/img/Logo_HHN.png`) als Material Dritter.

Zitiervorschlag:

> S. Schuster, „Vergleich eines dedizierten Reflexionsbots und eines generischen KI-Systems zur Unterstützung von Lernprozessen im Software-Prozessmanagement“, Bachelorarbeit, Hochschule Heilbronn, 2026.
