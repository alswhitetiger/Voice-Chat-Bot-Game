# AI 인터랙티브 오디오 스토리 게임: 호그와트 마법 모험
이 프로젝트는 OpenAI의 강력한 AI 모델들을 활용하여 사용자와 실시간으로 음성 대화를 나누며 이야기를 만들어나가는 **'인터랙티브 오디오 스토리 게임'**입니다. AI가 호그와트의 교장 '알버스 덤블도어'가 되어 게임 마스터(GM) 역할을 수행하며, 사용자는 목소리나 텍스트로 자신의 행동을 말하며 몰입감 높은 모험을 진행할 수 있습니다.

이 프로젝트는 개발 과정과 최종 결과물을 모두 포함하고 있으며, 사용 환경에 따라 선택할 수 있도록 **Jupyter Notebook**, **터미널 앱**, **웹 앱(Streamlit)** 세 가지 형태로 제공됩니다.

# 📝 파일 구성
| 파일명 | 설명 |
| :--- | :--- |
| **`game_voice.ipynb`** | **(개발 및 테스트용)** Jupyter Notebook 환경에서 음성 게임의 핵심 기능을 단계별로 개발하고 테스트한 파일입니다. 코드 셀을 하나씩 실행하며 각 기능(STT, Chat Completion, TTS)이 어떻게 동작하는지 확인할 수 있습니다. |
| **`game_voice.py`** | **(터미널 실행용)** 완성된 음성 게임을 컴퓨터의 터미널(명령창)에서 바로 실행할 수 있는 파이썬 스크립트입니다. 별도의 UI 없이 간단하게 음성 대화 기능에만 집중하고 싶을 때 사용합니다. |
| **`voice_game_streamlit.py`** | **(웹 실행용)** Streamlit을 사용하여 웹 브라우저에서 실행되는 최종 버전의 게임입니다. 호그와트 배경화면, 실시간 채팅 UI, 음성 녹음 버튼 등 시각적인 요소를 더해 사용 편의성과 몰입감을 극대화했습니다. |
# ✨ 주요 기능
**실시간 음성 대화:** 사용자의 음성을 인식(STT)하고, AI의 답변을 음성으로 합성(TTS)하여 실제 대화처럼 게임을 즐길 수 있습니다.

**문맥 기억:** 이전 대화 내용을 모두 기억하여 연속성 있는 스토리 진행이 가능합니다.

**페르소나 적용:** AI에게 '덤블도어 교수'라는 명확한 역할을 부여하여 게임의 몰입감을 높였습니다.

**다양한 실행 환경:** 개발 과정 확인부터 간단한 터미널 실행, 화려한 웹 UI 실행까지 모두 가능합니다.

**하이브리드 입력:** Streamlit 버전에서는 음성 입력과 텍스트 입력을 모두 지원하여 편의성을 높였습니다.

# 🛠️ 기술 스택 및 API 비용
이 프로젝트는 다음과 같은 기술들을 사용하며, OpenAI API 사용에 따른 비용이 발생합니다.

* **AI Models:**

  * ```gpt-4o-mini```: 메인 대화 및 스토리 생성을 담당합니다. 비용은 **입력/출력 토큰 양**에 따라 결정됩니다.

  * ```tts-1```: AI의 답변을 음성으로 합성합니다. 비용은 변환할 **텍스트의 글자 수**에 따라 결정됩니다.

  * **Google Web Speech API:** 사용자 음성을 텍스트로 변환합니다. ```speech_recognition``` 라이브러리를 통해 무료로 사용되므로 **OpenAI 비용은 발생하지 않습니다.**

* **Core Libraries:**

  *  ```openai```: OpenAI API 사용

  *  ```speech_recognition```: 마이크를 통한 음성 입력 및 텍스트 변환

  *  ```streamlit```: 웹 애플리케이션 UI 구현

  *  ```streamlit-mic-recorder```: Streamlit 환경에서 마이크 녹음

  *  ```pydub```: 오디오 파일 형식 변환

  *  ```playsound```: (터미널 버전) 음성 파일 재생

  *  ```python-dotenv```: API 키 관리

*  **예상 비용**: 10분간 게임을 즐길 경우, Chat Completion과 TTS 비용을 합쳐 약 **$0.38 (약 530원)** 정도의 저렴한 비용이 예상됩니다.

# 🚀 설치 및 실행 방법
**1. 프로젝트 준비**
먼저, 프로젝트를 진행할 폴더를 만들고, 제공된 모든 ```.py``` 및 ```.ipynb``` 파일을 해당 폴더에 넣습니다.

**2. API 키 설정**
프로젝트 폴더 안에 ```.env``` 라는 이름의 파일을 만들고, 그 안에 자신의 OpenAI API 키를 아래와 같이 입력하고 저장해주세요.

```OPENAI_API_KEY="sk-..."```

**3. 라이브러리 설치**
터미널(명령 프롬프트 또는 VS Code 터미널)에 아래 명령어를 입력하여 이 프로젝트에 필요한 모든 라이브러리를 설치합니다.

```Bash
pip install jupyterlab streamlit openai python-dotenv speechrecognition streamlit-mic-recorder pydub playsound pyaudio
```

**4. 게임 실행**
# 🎮 터미널 버전 실행
간단하게 음성 대화만 즐기고 싶을 때 사용합니다.

```Bash
python game_voice.py
```
**# game_voice.py 파일이 있는 폴더에서 실행**

# ✨ Streamlit 웹 버전 실행
호그와트 배경이 있는 웹 UI로 게임을 즐기고 싶을 때 사용합니다.

``` Bash
streamlit run voice_game_streamlit.py
```
**# voice_game_streamlit.py 파일이 있는 폴더에서 실행**

실행 후 터미널에 나타나는 URL 주소를 웹 브라우저에 열면 게임을 시작할 수 있습니다.

---

# 실행 페이지!!
**streamlit의 시연페이지**

<img width="724" height="620" alt="image" src="https://github.com/user-attachments/assets/7dde21cc-f56a-4371-888a-ee5edda2fa88" />
<img width="728" height="718" alt="image" src="https://github.com/user-attachments/assets/de127397-e67c-46be-aab5-65018f873528" />

---

**py의 터미널 시연 페이지**

<img width="1303" height="832" alt="image" src="https://github.com/user-attachments/assets/f7fc0d0c-7527-4271-85f7-885fea91b049" />
<img width="1290" height="864" alt="image" src="https://github.com/user-attachments/assets/e0325512-723b-430b-8d27-ddc934000791" />
<img width="1300" height="633" alt="image" src="https://github.com/user-attachments/assets/e04d9347-dc3b-47a4-bdd5-d465b27ddd4a" />

---

**ipynb의 시연페이지**

<img width="1341" height="614" alt="image" src="https://github.com/user-attachments/assets/9059dd3c-a45d-45d4-a125-16f456a494e0" />
<img width="1375" height="620" alt="image" src="https://github.com/user-attachments/assets/8ecae48a-610d-4e9d-9365-c1264e7c6d90" />

---

# 아쉬운 점
**음성 인식으로 하는 것이어서, 녹음한 것을 텍스트로 변환하는 것에 대해 자꾸 오타가 나기도 해서 그런 점들을 수정하여 좀 더 완벽하게 만들어 보고 싶다.**
