import streamlit as st
import hashlib
import bcrypt
import time

st.set_page_config(page_title="Hash Sandbox 🔐", page_icon="🔐", layout="centered")

st.title("🧩 Hash Sandbox — песочница хеш-функций")
st.write("Изучите, как работают алгоритмы хеширования: MD5, SHA, bcrypt и др.")

# Ввод данных
text = st.text_input("Введите строку для хеширования:", placeholder="Например: password123")

algorithm = st.selectbox(
    "Выберите алгоритм:",
    ["MD5", "SHA-1", "SHA-256", "SHA-512", "bcrypt"]
)

if st.button("Вычислить хеш"):
    if not text:
        st.warning("Введите строку для хеширования!")
    else:
        start_time = time.time()
        
        if algorithm == "MD5":
            result = hashlib.md5(text.encode()).hexdigest()
        elif algorithm == "SHA-1":
            result = hashlib.sha1(text.encode()).hexdigest()
        elif algorithm == "SHA-256":
            result = hashlib.sha256(text.encode()).hexdigest()
        elif algorithm == "SHA-512":
            result = hashlib.sha512(text.encode()).hexdigest()
        elif algorithm == "bcrypt":
            salt = bcrypt.gensalt()
            result = bcrypt.hashpw(text.encode(), salt).decode()

        elapsed = time.time() - start_time

        st.success("✅ Хеш успешно вычислен!")
        st.code(result, language="text")

        st.write(f"⏱️ Время вычисления: {elapsed:.6f} сек")
        st.write(f"🔢 Длина хеша: {len(result)} символов")

        # Пояснение
        st.info({
            "MD5": "Устаревший алгоритм, не рекомендуется для безопасных систем.",
            "SHA-1": "Также устарел, возможны коллизии.",
            "SHA-256": "Современный надёжный стандарт (используется в блокчейнах).",
            "SHA-512": "Длинный хеш, высокая стойкость, применяется в криптографии.",
            "bcrypt": "Медленный адаптивный алгоритм, используется для хранения паролей."
        }[algorithm])

# Дополнительная функция сравнения хешей
st.divider()
st.subheader("🔍 Проверка совпадения хешей")

hash1 = st.text_input("Хеш #1:")
hash2 = st.text_input("Хеш #2:")

if st.button("Сравнить"):
    if hash1 and hash2:
        if hash1.strip() == hash2.strip():
            st.success("✅ Хеши совпадают!")
        else:
            st.error("❌ Хеши различаются.")
    else:
        st.warning("Введите оба хеша для сравнения.")
