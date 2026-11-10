import streamlit as st

st.set_page_config(page_title="Экологический контроль", layout="wide")

st.title("🛡️ Панель оператора: Экологический контроль")
st.markdown("Проверка событий и доказательных материалов")

# --- ИМИТАЦИЯ БАЗЫ ДАННЫХ (Список событий) ---
# Позже это будет приходить из API от 5-й группы
MOCK_EVENTS = {
    "evt-1001": {
        "datetime": "2026-11-10 08:15:00", "duration_sec": 125, "ml_confidence": 0.92,
        "model_version": "v2.1-eco", "cam_id": "CAM-01", "status": "PENDING",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "audio_url": "https://www.w3schools.com/html/horse.mp3",
        "db_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    "evt-1002": {
        "datetime": "2026-11-10 09:30:00", "duration_sec": 45, "ml_confidence": 0.78,
        "model_version": "v2.1-eco", "cam_id": "CAM-02", "status": "PENDING",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "audio_url": "https://www.w3schools.com/html/horse.mp3",
        "db_hash": "a1b2c3d44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b8"
    }
}

# --- БОКОВАЯ ПАНЕЛЬ ---
st.sidebar.header("Список событий")
selected_event_id = st.sidebar.radio(
    "Выберите событие для проверки:",
    options=list(MOCK_EVENTS.keys()),
    format_func=lambda x: f"{x} ({MOCK_EVENTS[x]['datetime']})"
)

mock_event = MOCK_EVENTS[selected_event_id]
st.sidebar.info(f"Камера: {mock_event['cam_id']}\n\nСтатус: {mock_event['status']}")

# --- ОСНОВНОЙ ЭКРАН ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"📹 Доказательные материалы: {selected_event_id}")
    
    # Видеоплеер
    st.video(mock_event["video_url"], format="video/mp4")
    
    # Аудиоплеер
    st.audio(mock_event["audio_url"], format="audio/mp3")

with col2:
    st.subheader("ℹ️ Данные события")
    st.write(f"**Дата и время:** {mock_event['datetime']}")
    st.write(f"**Длительность:** {mock_event['duration_sec']} сек.")
    st.write(f"**Уверенность ML:** {mock_event['ml_confidence'] * 100:.1f}% (Модель: {mock_event['model_version']})")
    
    st.divider()
    
    # --- БЛОК БЕЗОПАСНОСТИ ---
    st.subheader("🔒 Проверка целостности")
    st.write("Хеш-сумма из базы данных (SHA-256):")
    st.code(mock_event["db_hash"], language="text")
    
    if st.button("Проверить целостность файла", use_container_width=True):
        # Имитация
        computed_hash = mock_event["db_hash"]
        if computed_hash == mock_event["db_hash"]:
            st.success("✅ Целостность подтверждена.")
        else:
            st.error("🚨 ВНИМАНИЕ! Файл подменен!")

    st.divider()

    # --- БЛОК ВЕРИФИКАЦИИ ---
    st.subheader("✍️ Решение оператора")
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("✅ Подтвердить", type="primary", use_container_width=True):
            st.balloons()
            st.success("Событие подтверждено.")
    with col_btn2:
        if st.button("❌ Отклонить", use_container_width=True):
            st.error("Событие отклонено.")
