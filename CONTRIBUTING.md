# Contributing to NeoToasterFirmware

감사합니다! 프로젝트에 기여해 주셔서 감사합니다. 아래 절차를 따라 주세요.

## 브랜치 전략
- 기능/개선: `feature/<short-description>`
- 버그 수정: `fix/<short-description>`
- 문서: `docs/<short-description>`

PR은 기본적으로 `main`(또는 기본 브랜치)로 병합 요청합니다. 하나의 PR은 하나의 목적만 가지도록 해주세요.

## 커밋 메시지
- 요약은 짧고 영어/한국어 가능 (권장: 영어). 형식 예: `feat: add new config option` 또는 `fix: correct timing bug`

## PR 템플릿
PR에는 다음 항목을 포함해 주세요:
- 변경 요약
- 관련 이슈(#number)
- 테스트 방법(로컬에서 빌드/동작 확인 방법)
- 영향 범위(보드, 기능)

## 코드 스타일과 검사
- C++ 코딩 스타일은 기존 파일 스타일을 따릅니다.
- 변경 후 `platformio run -e esp32dev`로 빌드 확인을 권장합니다.

## 테스트
- 하드웨어 의존 코드의 경우 가능한 한 추상화된 모듈 단위로 유닛 테스트를 추가해 주세요.

## 연락 및 리뷰
- 주요 변경은 PR에서 리뷰어(maintainer)를 지정해 주세요.
# Contributing

작은 변경이나 버그 리포트, 문서 개선 모두 환영합니다.

간단한 개발/기여 흐름

1. 저장소 포크/클론
2. 새 브랜치 생성: `git checkout -b fix/your-change`
3. 브랜치 이름 규칙

- 형식: `type/scope-or-short-desc`
- 허용되는 타입: `feat`, `fix`, `chore`, `docs`, `ci`, `refactor`, `test`, `perf`, `hotfix`, `release`
- 예시: `feat/ui-add-settings`, `fix/rtc-bug`, `chore/pinned-deps`, `docs/update-readme`
- 권장 정규식: `^(feat|fix|chore|docs|ci|refactor|test|perf|hotfix|release)\/[a-z0-9._-]+(?:-[a-z0-9._-]+)*$`

브랜치 이름은 위 규칙을 따르세요. 이 규칙은 PR 생성 시 자동으로 검사됩니다(규칙 미준수 시 체크 실패).
3. 변경 및 로컬 빌드(아래 참고)
4. 테스트 후 PR 생성

빌드 및 플래시 (빠른 예)

- PlatformIO 설치: `python -m pip install --upgrade pip` 그리고 `pip install -U platformio`
- 빌드:
  - `platformio run -e esp32dev`
  - `platformio run -e adafruit_matrixportal_esp32s3`
- 플래시:
  - `platformio run -e esp32dev -t upload` (장치 연결 필요)

파일시스템(FFat/SD) 업로드

프로젝트는 런타임에 `FFat` 또는 SD 카드를 사용합니다. 파일을 장치에 올리려면:

- SD 사용: `data/` 디렉터리의 내용을 SD 카드에 복사
- FFat 사용(지원하는 경우): PlatformIO의 `uploadfs` 타겟 사용 (`platformio run -e <env> -t uploadfs`) 또는 외부 도구로 FFat 이미지 생성 후 업로드

외부 라이브러리 추가시

1. `platformio.ini`의 `lib_deps`에 항목 추가
2. `scripts/check_third_party_licenses.py` 실행하여 라이선스 수집
3. `THIRD_PARTY_LICENSES.md` 업데이트

코드 스타일

- C++ 코드는 기존 스타일을 따릅니다 (헤더/소스 분리, 네임스페이스 `toaster` 등).

이슈/PR 템플릿

간단한 설명, 재현 방법, 기대 동작을 포함해 주세요.
