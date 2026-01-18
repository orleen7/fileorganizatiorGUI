# 📂 Academic Admin Automation (학사 행정 파일 자동 분류기)

> **"From Chaos to Structure"** > 규칙성 없는 비정형 파일명(Unstructured Filenames)을 정규표현식과 인코딩 정규화 기술로 자동 분류하는 Python 솔루션입니다.

<br>

## 📌 Background & Motivation
대학 학사 행정 업무 중, 수백 명의 학생들이 제출하는 파일명이 통일되지 않아 분류에 막대한 리소스가 낭비되는 문제를 해결하기 위해 개발되었습니다.
특히 **macOS(NFD)와 Windows(NFC) 간의 자소 분리 현상**으로 인해 파일 검색과 정렬이 마비되는 기술적 문제를 **Unicode Normalization**으로 해결하여, OS에 구애받지 않는 자동화 파이프라인을 구축했습니다.

### 📉 Before (The Pain Point)
- **비효율:** 500+개의 파일을 수작업으로 분류하는 데 매주 **18시간 소요**.
- **인코딩 오류:** 맥북 유저가 제출한 파일의 자음/모음이 분리되어 검색 불가능.
- **Human Error:** 육안 분류로 인한 누락 및 오분류 빈번 발생.

### 📈 After (The Solution)
- **자동화:** 정규표현식(Regex)을 통한 메타데이터 추출로 **분류 시간 99% 단축 (10초 이내)**.
- **호환성:** `unicodedata` 라이브러리를 활용해 **OS 간 인코딩 충돌 완전 해결**.
- **접근성:** CLI에 익숙하지 않은 동료를 위해 **`Tkinter` 기반 GUI** 제공.

<br>

## 🛠 Key Features
1. **Cross-Platform Compatibility (자소 분리 해결)**
   - macOS의 NFD(Normalization Form Decomposition) 방식을 Windows 표준인 NFC(Composition)로 자동 변환.
   - OS가 섞인 환경에서도 깨짐 없는 파일명 처리 보장.

2. **Regex Parsing Engine (정규표현식 파싱)**
   - 불규칙한 파일명에서 `학번(8~10자리)`, `주차(Week)`, `이름` 등 핵심 정보를 패턴 매칭으로 추출.
   - 띄어쓰기, 특수문자 등 노이즈(Noise) 데이터 자동 제거.

3. **User-Friendly GUI**
   - Python 설치 여부와 관계없이 직관적으로 사용할 수 있는 파일 선택/분류 인터페이스 제공.
   - 작업 진행 상황(Progress) 및 결과(성공/실패 수치) 시각화.

4. **Exception Handling (예외 격리)**
   - 식별 불가능한 파일은 별도 폴더(`_Unclassified`)로 자동 격리하여 데이터 유실 방지.

<br>

## 💻 Tech Stack
| Category | Technology |
| --- | --- |
| **Language** | Python 3.10+ |
| **GUI** | Tkinter (Standard Lib) |
| **Core Logic** | `re` (Regex), `unicodedata`, `shutil`, `os` |
| **Version Control** | Git / GitHub |

<br>

## 🚀 Getting Started

### Prerequisites
- Python 3.x 이상이 설치되어 있어야 합니다. (별도 라이브러리 설치 불필요)

### Installation & Run
```bash
# 1. 저장소 클론 (Clone this repository)
git clone https://github.com/orleen7/fileorganizatiorGUI

# 2. 프로젝트 폴더로 이동
cd academic-admin-automation

# 3. 프로그램 실행
python main.py

📁 Project Structure
.
├── main.py             # Main execution script (GUI + Logic)
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules (Mac/Python cache)
└── assets/             # (Optional) Screenshot images

📝 License
This project is licensed under the MIT License.


