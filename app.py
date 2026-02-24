import streamlit as st
import google.generativeai as genai

# 1. 網頁的基本設定
st.set_page_config(page_title="我的專屬翻譯機", page_icon="🌍")
st.title("🌍 Gemini 智慧翻譯機")

# 2. 讓使用者輸入 API Key 的安全密碼框
api_key = st.text_input("請輸入您的 Gemini API Key (系統不會儲存):", type="password")

# 3. 畫面排版：分成左右兩半
col1, col2 = st.columns(2)
with col1:
    st.subheader("原文")
    source_text = st.text_area("請在此輸入要翻譯的文字：", height=200)

with col2:
    st.subheader("翻譯結果")
    result_placeholder = st.empty() # 準備一個空位來放翻譯結果

# 4. 翻譯按鈕與核心功能
if st.button("🚀 開始翻譯"):
    if not api_key:
        st.warning("請先輸入上方 API Key 喔！")
    elif not source_text:
        st.warning("請輸入要翻譯的文字！")
    else:
        try:
            # 設定剛剛成功過關的 Gemini 2.5 Flash 模型
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # 設計 Prompt
            prompt = f"""
            You are a professional translator. 
            Translate the following text into Traditional Chinese.
            Output ONLY the translated text without any explanations.
            
            Text to translate: "{source_text}"
            """
            
            # 顯示「翻譯中」的動畫，並呼叫 Gemini
            with st.spinner('AI 正在努力翻譯中...'):
                response = model.generate_content(prompt)
                result_placeholder.success(response.text)
                
        except Exception as e:
            st.error(f"哎呀，發生錯誤了：{e}")
