# NeoToasterFirmware - Architecture Overview

이 문서는 프로젝트의 주요 모듈, 책임, 데이터 흐름의 개요를 제공합니다. 초안이며 필요시 상세를 확장합니다.

## 개요
- 빌드 시스템: `platformio.ini` (env: `esp32dev`, `adafruit_matrixportal_esp32s3`)
- 진입점: `src/main.cpp` → `Protogen.begin()` / `Protogen.loop()`

## 주요 모듈
- `src/`
  - `protogen.*`: 애플리케이션 초기화, 메인 루프, 중앙 오케스트레이션
  - `config/`: 설정 파싱 및 관리 (`config.yaml` 기반)
  - `effects/`: 시각효과 모듈(각 효과별 분리)
  - `hal/`: 하드웨어 추상화 계층 (display, controller, sensor)
  - `huds/`: HUD 및 UI 컴포넌트

- `lib/`
  - 유틸리티(이미지 처리, 자산 로더, dither 등)

## 데이터 흐름(간단)
1. 초기화: 설정 파일 로드 → 하드웨어 초기화
2. 입력(센서/원격) 수신 → 이벤트 큐에 전달
3. 렌더: 현재 상태에 맞는 `effects`/`huds`가 그리기 명령을 생성
4. HAL: 디스플레이 드라이버로 픽셀 전송

## 테스트 전략(권장)
- 비즈니스 로직(이미지 처리, 스크립트 파서 등)은 유닛 테스트로 검증
- HAL은 인터페이스로 분리해 모의(Mock)로 테스트

## 확장 포인트
- 새로운 보드: `platformio.ini`에 env 추가 + 보드별 `hal/` 드라이버
- 새로운 이펙트: `effects/`에 모듈 추가
