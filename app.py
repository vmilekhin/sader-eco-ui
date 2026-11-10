import streamlit as st
import hashlib

st.set_page_config(page_title="Экологический контроль", layout="wide")

st.title("🛡️ Панель оператора: Экологический контроль")
st.markdown("Проверка событий и доказательных материалов")

# --- ИМИТАЦИЯ ДАННЫХ (Позже это будет приходить из БД) ---
# В реальности эти данные будет отдавать FastAPI (5 группа)
mock_event = {
    "event_id": "evt-1001",
    "cam_id": "CAM-01",
    "datetime": "2026-11-10 08:15:00",
    "duration_sec": 125,
    "ml_confidence": 0.92,
    "model_version": "v2.1-eco",
    "status": "PENDING",
    "video_url": "https://www.w3schools.com/html/mov_bbb.mp4", # Тестовое видео
    "audio_url": "https://www.w3schools.com/html/horse.mp3",  # Тестовое аудио
    "db_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" # Фейковый хеш из БД
}

# --- БОКОВАЯ ПАНЕЛЬ: Выбор события ---
st.sidebar.header("Список событий")
st.sidebar.info(f"Текущее событие: {mock_event['event_id']}\n\nКамера: {mock_event['cam_id']}")
st.sidebar.button("Обновить список (скоро)")

# --- ОСНОВНОЙ ЭКРАН: Карточка события ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📹 Доказательные материалы (Видео / Аудио)")
    
    # Видеоплеер
    st.video(mock_event["video_url"], format="video/mp4")
    
    # Аудиоплеер
    st.audio(mock_event["audio_url"], format="audio/mp3")

with col2:
    st.subheader("ℹ️ Данные события")
    st.write(f"**Дата и время:** {mock_event['datetime']}")
    st.write(f"**Длительность работы двигателя:** {mock_event['duration_sec']} сек.")
    st.write(f"**Уверенность ML:** {mock_event['ml_confidence'] * 100:.1f}% (Модель: {mock_event['model_version']})")
    
    st.divider()
    
    # --- БЛОК БЕЗОПАСНОСТИ (Твоя фишка) ---
    st.subheader("🔒 Проверка целостности")
    st.write("Хеш-сумма из базы данных (SHA-256):")
    st.code(mock_event["db_hash"], language="text")
    
    # Имитация проверки хеша
    # В реальности: мы берем файл с диска, считаем его хеш и сравниваем с БД.
    if st.button("Проверить целостность файла"):
        # (Тут будет реальная функция скачивания и хеширования)
        computed_hash = mock_event["db_hash"] # Имитируем, что хеши совпали
        if computed_hash == mock_event["db_hash"]:
            st.success("✅ Целостность подтверждена. Файл не был изменен.")
        else:
            st.error("🚨 ВНИМАНИЕ! Хеши не совпадают. Файл мог быть подменен!")

    st.divider()

    # --- БЛОК ВЕРИФИКАЦИИ ОПЕРАТОРОМ ---
    st.subheader("✍️ Решение оператора")
    st.warning("Вы просмотрели материалы? Подтвердите или отклоните нарушение.")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("✅ Подтвердить", type="primary", use_container_width=True):
            st.balloons()
            st.success("Событие подтверждено. Пакет материалов сформирован.")
            # Тут будет отправка PUT-запроса в API (5 группа)
    with col_btn2:
        if st.button("❌ Отклонить", use_container_width=True):
            st.error("Событие отклонено. Материалы помечены как ложное срабатывание.")
            # Тут будет отправка PUT-запроса в API
