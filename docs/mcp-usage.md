# MCP 사용 안내

---
title: MCP 사용 안내
summary: MCP(에이전트 기반 GitHub 작업) 사용법과 권한 및 안전 수칙을 정리합니다.
last_modified: 2026-04-12
---

## 개요
MCP(Copilot의 GitHub MCP 액션)는 원격 GitHub 저장소에 대해 안전하게 파일/브랜치/PR 작업을 자동화하는 도구입니다. 이 문서는 로컬 git 명령 대신 MCP 관련 액션을 사용할 때의 권한, 안전 수칙, 주요 사용 예시를 정리합니다.

## 주요 기능(에이전트 함수)
- `mcp_io_github_git_create_branch`: 원격에 새 브랜치 생성
- `mcp_io_github_git_create_or_update_file`: 원격 파일 생성/업데이트(커밋 포함)
- `mcp_io_github_git_create_pull_request`: 브랜치 기반 PR 생성
- `mcp_io_github_git_push_files`: 여러 파일을 한 번에 커밋+푸시
- `mcp_io_github_git_get_commit`, `get_latest_release` 등 조회용 함수

(참고: 저장소 내에 동일한 이름의 도구가 제공되는 경우 이를 사용하면 프로그래매틱 작업을 안전하게 수행할 수 있습니다.)

## 권한 및 토큰
- 대부분 작업은 저장소에 대한 쓰기 권한이 필요합니다. `GITHUB_TOKEN`으로 가능한 작업과 조직 정책에 따라 제한이 있을 수 있습니다.
- 포크에서 자동 PR 생성/파일 푸시가 실패하면 개인 액세스 토큰(PAT)을 `secrets`로 추가하고 워크플로우(또는 에이전트 호출)에 해당 시크릿을 참조하세요.
- 최소 권한 원칙 적용: 필요한 최소한의 권한만 부여하세요(`contents: write`, `pull-requests: write` 등).

## 안전 수칙
1. 중요한 변경(코드 삭제, 브랜치 제거)은 자동화 전에 백업 또는 별도 브랜치 생성 후 진행하세요.
2. 파일 삭제나 브랜치 제거는 되돌릴 수 있으니 명확히 확인 후 실행하세요. (MCP에 브랜치 삭제 전용 함수가 없는 경우 GitHub API 호출 또는 `git push --delete` 사용 필요)
3. 자동화 작업은 로그와 커밋 메시지를 남기고 라벨을 붙여 쉽게 추적 가능하게 하세요.

## 예시
- 새 브랜치 생성
  - 도구: `mcp_io_github_git_create_branch`
  - 용도: 자동 포맷/패치 적용용 브랜치 생성

- 파일 여러 개를 커밋해서 푸시
  - 도구: `mcp_io_github_git_push_files`
  - 용도: 자동 생성한 포맷 결과나 문서 업데이트를 한 번에 업로드

- PR 생성
  - 도구: `mcp_io_github_git_create_pull_request`
  - 용도: 자동 브랜치에서 PR을 열어 리뷰 후 병합

- 브랜치 삭제
  - 현재 제공되는 MCP 도구 중에는 브랜치 삭제 전용 함수가 명시적으로 없을 수 있습니다. 브랜치 삭제는 다음 중 하나로 수행하세요:
    - 로컬에서 `git push origin --delete <branch>` 실행
    - GitHub REST API `DELETE /repos/{owner}/{repo}/git/refs/heads/{branch}` 호출

## 테스트 & 롤백
- 변경 전: `git checkout -b backup/<timestamp>`로 백업 브랜치 생성
- 자동화 실행 후: 생성된 PR/커밋을 검토
- 롤백: 잘못된 파일 변경은 PR을 닫거나 `git revert`/원격 브랜치 복원으로 되돌립니다.

## 권장 흐름
1. 에이전트로 변경사항을 `create_or_update_file` 또는 `push_files`로 커밋할 때는 새 브랜치 사용
2. `create_pull_request`로 PR 생성 후 수동 리뷰 및 병합
3. 필요 시 병합 완료 후 원격 브랜치 정리(수동 또는 승인된 자동화)

원하시면 이 문서를 더 확장해 `예제 호출 코드`(정확한 페이로드/매개변수 예시)를 추가하거나, 제가 MCP 도구를 사용해 특정 작업을 자동으로 수행하도록 도와드리겠습니다.

## Change History

- 2026-04-12: 문서 헤더 표준화 및 변경 이력 추가 (자동)
