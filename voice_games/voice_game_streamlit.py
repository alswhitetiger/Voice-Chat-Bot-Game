import streamlit as st
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
from streamlit_mic_recorder import mic_recorder
import io
from pydub import AudioSegment

# --- 초기 설정 ---
load_dotenv()
st.set_page_config(page_title="호그와트 마법 모험", layout="centered")
client = OpenAI()
recognizer = sr.Recognizer()

# --- 세션 상태 초기화 ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "당신은 호그와트의 교장 알버스 덤블도어입니다. 사용자는 신입생입니다. 주변 상황을 생생하게 묘사하고, 항상 사용자에게 다음에 무엇을 할 것인지 물어보세요. 대답은 간결하게 1~3 문장으로 유지하세요."},
        {"role": "assistant", "content": "오랜만이다, 새로운 마법사여. 이곳 호그와트에 온 것을 진심으로 환영한다. 이제 너의 모험이 시작될 것이다. 첫 번째로 어떤 수업에 참여하고 싶으냐?"}
    ]
if "last_audio_id" not in st.session_state:
    st.session_state.last_audio_id = None

# --- 배경 및 UI 스타일 ---
HOGWARTS_BACKGROUND_URL = "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fwallpapers.com%2Fimages%2Fhd%2Fthe-magical-world-of-hogwarts-castle-at-twilight-qddsrb40uub1v5jo.jpg&type=sc960_832"
st.markdown(f"""
<style>
.stApp {{
    background-image: url("{HOGWARTS_BACKGROUND_URL}");
    background-size: cover; background-position: center; background-attachment: fixed;
}}
.stChatMessage {{
    background-color: rgba(255, 255, 255, 0.7); border-radius: 10px;
}}
h1 {{
    color: #FFFFFF; text-shadow: 2px 2px 4px #000000;
}}
</style>
""", unsafe_allow_html=True)
st.title("🧙‍♂️ 호그와트 마법 모험")

# --- 사이드바 메뉴 ---
with st.sidebar:
    st.header("게임 메뉴")
    if st.button("대화 초기화"):
        st.session_state.clear()
        st.rerun()

    with st.expander("전체 대화 내용 보기"):
        st.write(st.session_state.get("messages", "아직 대화가 없습니다."))

# --- 핵심 함수 ---
def text_to_speech(text):
    response = client.audio.speech.create(model='tts-1', voice='nova', input=text)
    return response.read()

def handle_response(user_text):
    st.session_state.messages.append({"role": "user", "content": user_text})
    
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    ai_response = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    
    st.session_state.audio_to_play = text_to_speech(ai_response)

# --- 채팅 UI 표시 ---
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# --- 음성 및 텍스트 입력 처리 ---
st.sidebar.divider()
st.sidebar.subheader("마법 주문 외우기 (음성)")
audio_info = mic_recorder(start_prompt="🎤 녹음 시작", stop_prompt="🛑 녹음 중지", key='recorder')

if audio_info and audio_info['id'] != st.session_state.last_audio_id:
    st.session_state.last_audio_id = audio_info['id']
    audio_bytes = audio_info['bytes']
    
    try:
        sound = AudioSegment.from_file(io.BytesIO(audio_bytes))
        wav_io = io.BytesIO()
        sound.export(wav_io, format="wav")
        wav_io.seek(0)

        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)
        user_text = recognizer.recognize_google(audio_data, language='ko-KR')
        
        handle_response(user_text)
        st.rerun()
        
    except (sr.UnknownValueError, sr.RequestError):
        st.warning("음성을 인식하지 못했습니다. 다시 시도해주세요.")
    except Exception:
        st.error("오디오 파일을 처리하는 중 오류가 발생했습니다.")

if user_text_input := st.chat_input("마법 주문을 입력하세요..."):
    handle_response(user_text_input)
    st.rerun()

# --- 오디오 재생 및 게임 시작 음성 ---
if "audio_to_play" in st.session_state:
    st.audio(st.session_state.pop("audio_to_play"), autoplay=True)

if "start_audio_played" not in st.session_state:
    initial_message = st.session_state.messages[1]["content"]
    st.session_state.audio_to_play = text_to_speech(initial_message)
    st.session_state.start_audio_played = True
    st.rerun()