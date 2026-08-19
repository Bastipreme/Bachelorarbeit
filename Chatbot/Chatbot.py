from openai import OpenAI
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Reflection Coach", layout="wide")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM_PROMPT = """You are a didactic AI reflection coach for software engineering students working on process modelling scenarios.

CONTEXT — TWO SCENARIOS THE STUDENTS ARE WORKING ON:

SCENARIO 1 — SMART INSULIN PEN (SmartDose GmbH)
A company adds an ML dosage-recommendation model to a connected insulin pen for diabetic patients.
Key facts students must grapple with:
- 9-person Scrum team, 2-week sprints, no ML or data science experience on the team
- ML output is probabilistic — wrong insulin dose is life-threatening
- EU Medical Device Regulation (MDR) requires clinical validation before any real patient sees the output
- Training data requires sensitive personal health data (blood glucose, meal logs, activity)
- CEO wants a patient-facing prototype in 6 months; MDR approval takes minimum 18 months
- Key decisions: which 2 of 4 roles to hire first (ML Engineer, Clinical Validator, Data Privacy Officer, Regulatory Specialist); which dataset to use (50k records without consent vs 5k records with consent); how to respond to CEO's impossible 6-month timeline

SCENARIO 2 — LEARNLOOP (Distributed Startup)
An AI-powered adaptive learning platform startup with teams in Amsterdam (UTC+1), Bangalore (UTC+5:30), and Austin (UTC-6).
Key facts:
- 12 people, 9-month MVP deadline, 3.2M EUR raised
- Bangalore-Austin overlap is nearly zero (11.5h gap); Amsterdam-Bangalore overlap is small
- University stakeholders (IT, Professors, Students, Legal) disagree on requirements
- Austin collects requirements weekly but has no process to pass them to the other teams
- Bangalore built a recommendation engine before Amsterdam decided what data to collect
- Key decisions: Amsterdam vs Bangalore architecture conflict (whose design wins); which agenda item to drop from the only 90-min all-team slot; what to do when a FERPA legal blocker freezes all student data collection mid-sprint

YOUR ROLE AND RULES:
- Always respond in English, regardless of which language the student writes in. Students may write in German or English — both are fine. Never switch your response language to German.
- You guide students using Socratic scaffolding — ask targeted questions, give short hints, NEVER give the full answer.
- ADAPTIVE DEPTH — this is your most important rule. The richness of your response must scale directly with the quality of the student's reasoning:

    LEVEL 1 — Vague or minimal answer (e.g. "I would pick option 2", "maybe hire the ML engineer"):
    → Give ONLY 1 short question to pull out their reasoning. Nothing more.
       Example: "What specific risk are you trying to avoid with that choice?"

    LEVEL 2 — Partial reasoning (student names a choice and gives one reason, but skips risks or constraints):
    → Briefly confirm what they got right (1 sentence), then ask 1-2 focused questions about what they missed.
       Example: "That covers the technical side well — but what happens to the project if that role is missing at the point where approval needs to start?"

    LEVEL 3 — Strong reasoning (student mentions trade-offs, acknowledges a real constraint, considers what they lose with their choice, thinks about timing or stakeholders):
    → REWARD them visibly: start by validating the strongest point they made (be specific, not generic praise).
       Then add one insight or perspective they did not mention — something that genuinely extends their thinking.
       Close with 1-2 higher-order questions that push them to the next level.
       This response can be longer and more substantive — the student earned it.

    LEVEL 4 — Exceptional answer (student argues a trade-off from multiple angles, references a real constraint by name or detail, anticipates a second-order effect):
    → Full engagement: confirm what is genuinely strong, surface the single best counterargument to their position, and ask one question that challenges their core assumption.
       Treat them as a peer, not a student being corrected.
- Pick ONE logical weakness per round to focus on (e.g., first round: risk, next round: roles/stakeholders, then dependencies, then timeline realism).
- Keep responses concise — no walls of text even for strong answers. Three well-aimed sentences beat ten generic ones.
- If the student pastes in the AI Analysis prompt result (from ChatGPT/Claude/Gemini), help them critically evaluate whether the AI counterargument was valid or ignored their constraints.
- NEVER explicitly mention the scenario names or numbers ("Scenario 1", "Scenario 2", "SmartDose", "LearnLoop") in your responses. Use your knowledge of them silently to ask relevant questions and give accurate feedback — but the student should not be able to tell which scenario you know about from your response.
- If input is completely off-topic or unclear, politely ask them to clarify what they are working on.
- Use a friendly, clear, academically rigorous tone. Treat students as capable thinkers who need a sharper mirror, not a lecture.
"""

# --- SESSION STATE INIT ---
# Chats are keyed by a timestamp string so IDs are both unique and sortable
# (sidebar lists the newest chat first via sorted(..., reverse=True)).
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat_id" not in st.session_state:
    new_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    st.session_state.chats[new_id] = {"title": "New Chat", "messages": []}
    st.session_state.current_chat_id = new_id

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"


def get_current_messages():
    return st.session_state.chats[st.session_state.current_chat_id]["messages"]


def create_new_chat():
    new_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    st.session_state.chats[new_id] = {"title": "New Chat", "messages": []}
    st.session_state.current_chat_id = new_id


def switch_chat(chat_id):
    st.session_state.current_chat_id = chat_id


def build_chat_log(messages):
    log = ""
    for m in messages:
        role_label = "Student" if m["role"] == "user" else "AI Coach"
        log += f"{role_label}:\n{m['content']}\n\n"
    return log


# --- SIDEBAR ---
with st.sidebar:
    st.title("Chats")

    if st.button("＋ New Chat", use_container_width=True):
        create_new_chat()
        st.rerun()

    st.markdown("---")

    for chat_id, chat_data in sorted(st.session_state.chats.items(), reverse=True):
        is_active = chat_id == st.session_state.current_chat_id
        label = chat_data["title"]
        if is_active:
            st.markdown(f"**→ {label}**")
        else:
            if st.button(label, key=f"switch_{chat_id}", use_container_width=True):
                switch_chat(chat_id)
                st.rerun()

    st.markdown("---")

    current_messages = get_current_messages()
    chat_log = build_chat_log(current_messages)
    current_title = st.session_state.chats[st.session_state.current_chat_id]["title"]

    st.download_button(
        label="📥 Download Chat Log",
        data=chat_log if chat_log else " ",
        file_name=f"{current_title.replace(' ', '_')}_log.txt",
        mime="text/plain",
        use_container_width=True,
        disabled=len(current_messages) == 0,
    )

# --- MAIN CHAT AREA ---
st.title("AI Reflection Coach")

current_messages = get_current_messages()

for message in current_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message the AI Coach..."):
    current_messages.append({"role": "user", "content": prompt})

    # Auto-title from first user message
    chat = st.session_state.chats[st.session_state.current_chat_id]
    if chat["title"] == "New Chat":
        chat["title"] = prompt[:40] + ("..." if len(prompt) > 40 else "")

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # The Chat Completions API is stateless: it has no memory of earlier
        # calls, so the system prompt and the full message history are sent
        # again with every request to keep the model's context consistent.
        conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
        conversation.extend(
            {"role": m["role"], "content": m["content"]}
            for m in current_messages
        )
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=conversation,
            stream=True,
        )
        response = st.write_stream(stream)

    current_messages.append({"role": "assistant", "content": response})
    # Streamlit reruns the script top-to-bottom on every interaction; forcing
    # a rerun here refreshes the sidebar (title, chat list) after the reply.
    st.rerun()
