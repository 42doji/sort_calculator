### Git: git add와 git commit의 차이

**git add**는 커밋할 변경 사항을 선별해 준비하는 단계 
**git commit**은 준비된 변경 사항을 하나의 버전으로 기록함. 

---

### 

* **워킹 디렉터리 (Working Directory)**: 파일을 수정, 생성, 삭제하는 작업 공간.
* **준비 영역 (Staging Area 또는 Index)**: 다음 커밋에 포함될 변경 사항이 대기하는 공간.
* **로컬 저장소 (Local Repository)**: 프로젝트의 모든 버전(커밋) 이력이 저장되는 곳.

---

#### `git add`

`git add`는 워킹 디렉터리의 변경 사항 중에서, 특정 파일을 선별하여 스테이지로 옮김.

#### `git commit`

`git commit`은 스테이지에 있는 변경 사항을 버전으로 만들어 기록한다.
