FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Chatbot.py .

EXPOSE 8501

# Write secrets.toml from env var at runtime so the key is never baked into the image
CMD sh -c 'mkdir -p .streamlit && \
    echo "OPENAI_API_KEY = \"${OPENAI_API_KEY}\"" > .streamlit/secrets.toml && \
    streamlit run Chatbot.py \
      --server.port=8501 \
      --server.address=0.0.0.0 \
      --server.headless=true'
