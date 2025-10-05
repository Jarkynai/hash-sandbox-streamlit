import streamlit as st
from utils.crypto_utils import compute_hash, available_algorithms, compare_hashes, benchmark_algorithms
import pandas as pd
import time

st.set_page_config(page_title="Hash Sandbox 🔐", page_icon="🔐", layout="centered")


st.title("🧩 Hash Sandbox — песочница хеш-функций")
st.write("Интерактивный инструмент для изучения хеш-функций: MD5, SHA, bcrypt и др.")

# Боковая панель с настройками
st.sidebar.header("Настройки")
algorithm = st.sidebar.selectbox("Алгоритм", available_algorithms())
show_time = st.sidebar.checkbox("Показывать время вычисления", value=True)
show_length = st.sidebar.checkbox("Показывать длину хеша", value=True)


# Основная область — ввод
text = st.text_area("Введите строку для хеширования:", height=120)
add_salt = st.checkbox("Добавить salt (для bcrypt и демонстрации)")
salt_text = st.text_input("Salt (опционально):", value="") if add_salt else ""


if st.button("Вычислить хеш"):
if not text:
st.warning("Введите строку для хеширования!")
else:
start = time.time()
result = compute_hash(text, algorithm, salt=salt_text)
elapsed = time.time() - start


st.success("✅ Хеш вычислен")
st.code(result)


if show_time:
st.write(f"⏱ Время: {elapsed:.6f} с")
if show_length:
st.write(f"🔢 Длина: {len(result)} символов")


# Сравнение двух хешей
st.markdown("---")
st.subheader("🔍 Сравнить хеши")
h1 = st.text_input("Хеш #1")
h2 = st.text_input("Хеш #2")
if st.button("Сравнить хеши"):
ok = compare_hashes(h1, h2)
if ok:
st.success("Хеши совпадают")
else:
st.error("Хеши различаются")


# Бенчмарк алгоритмов
st.markdown("---")
st.subheader("📊 Бенчмарк алгоритмов")
if st.button("Запустить бенчмарк"):
sample = text if text else "password123"
df = benchmark_algorithms(sample)
st.dataframe(df)
st.bar_chart(df.set_index('algorithm')['time'])


# Дополнительно: справка
st.markdown("---")
st.subheader("ℹ️ О алгоритмах")
st.write("MD5 и SHA-1 считаются устаревшими для криптографической защиты, bcrypt предназначен для безопасного хранения паролей и т.д.")