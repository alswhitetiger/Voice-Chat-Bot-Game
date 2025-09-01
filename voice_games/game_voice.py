import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
from playsound import playsound

load_dotenv()
client = OpenAI()
recognizer = sr.Recognizer()

conversation_history = [
    {
        "role": "system",
        "content": "당신은 호그와트의 교장 알버스 덤블도어입니다. 사용자는 신입생입니다. 주변 상황을 생생하게 묘사하고, 항상 사용자에게 다음에 무엇을 할 것인지 물어보세요. 대답은 간결하게 1~3 문장으로 유지하세요."
    }
]

def listen_and_recognize():
    with sr.Microphone() as source:
        print("\n🎧 행동을 말씀하세요...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language='ko-KR')
        except (sr.UnknownValueError, sr.RequestError):
            return "음성을 인식하지 못했습니다."

def generate_and_speak(text):
    print(f"\n🎤 덤블도어 교수:\n{text}\n")
    with client.audio.speech.with_streaming_response.create(
        model='tts-1', voice='nova', input=text
    ) as response:
        response.stream_to_file("response.mp3")
    playsound("response.mp3")

initial_message = "오랜만이다, 새로운 마법사여. 이곳 호그와트에 온 것을 진심으로 환영한다. 이제 너의 모험이 시작될 것이다. 첫 번째로 어떤 수업에 참여하고 싶으냐?"
conversation_history.append({"role": "assistant", "content": initial_message})
generate_and_speak(initial_message)

while True:
    action = listen_and_recognize()
    print(f"👤 나:\n{action}\n")

    if "종료" in action or "그만" in action:
        generate_and_speak("다음 모험에서 다시 만나도록 하지.")
        break
    
    conversation_history.append({"role": "user", "content": action})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        temperature=0.8,
    )
    ai_response = response.choices[0].message.content
    
    conversation_history.append({"role": "assistant", "content": ai_response})
    generate_and_speak(ai_response)