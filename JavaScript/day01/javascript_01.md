## javascript 변수 선언 키워드
### let
- 블록 스코프를 갖는 지역 변수를 선언
- **재할당 가능**
- **재선언 불가능**

```javascript
// 재할당
let num = 10
num = 20

// 재선언
let num = 10
let num = 20
```

### const
- 블록 스코프를 갖는 지역 변수를 선언
- **재할당 불가능**
- **재선언 불가능**
- 선언 시 반드시 초기값 설정 필요

```javascript
const num = 10
num = 10  // 재할당 불가능

const num = 10
const num = 20  // 재선언 불가능

const num   // 초기값 필요
```

### 변수명 작성 규칙
- 반드시 문자, 달러, 밑줄로 시작
- 대소문자 구분
- 예약어 사용 불가
- 카멜 케이스(camelCase) : 변수, 객체, 함수에 사용
- 파스칼 케이스(PascalCase) : 클래스, 생성자에서 사용
- 대문자 스네이크 케이스(SNAKE_CASE) : 상수에 사용

### 어떤 변수 선언 키워드를 사용해야 할까?
- const를 기본으로 사용
- 필요한 경우에만 let으로 전환
  - 재할당이 필요한 경우
  - let을 사용하는 것은 해당 변수가 의도적으로 변경될 수 있음을 명확히 나타냄
  - 코드의 유연성을 확보하면서도 const의 장점을 최대한 활용할 수 있음

### const를 기본으로 사용해야 하는 이유
- 코드의 의도 명확화
  - 해당 변수가 재할당되지 않을 것임을 명확히 표현
  - 개발자들에게 변수의 용도와 동작을 더 쉽게 이해할 수 있게 해줌

- 버그 예방
  - 의도치 않은 변수 값 변경으로 인한 버그를 예방
  - 큰 규모의 프로젝트나 팀 작업에서 중요

## DOM
- 웹 페이지(Document)를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공 -> 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함

### DOM API
- 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작 할 수 있도록 페이지 요소들을 객체 형태로 제공하며 이에 따른 메서드 또한 제공

### document 객체
- 웹 페이지를 나타내는 DOM 트리의 최상위 객체

### DOM tree
- html 태그를 나타내는 elements의 node는 문서의 구조를 결정
- 이들은 다시 자식 node를 가질 수 있음 (ex. document.title)

## DOM 선택
### DOM 조작 시 기억해야 할 것
- 웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기
- 조작 순서
  1. 조작하고자 하는 요소를 선택(또는 탐색)
  2. 선택된 요소의 콘텐츠 또는 속성을 조작

### 선택 메서드
- document.querySelector(selector) : 요소 한 개 선택 / 제공한 선택자를 만족하는 첫번째 element 객체를 반환(없다면 null)
- documnet.querySelectorAll(selector) : 요소 여러 개 선택 / 제공한 선택자와 일치하는 여러 element를 선택(제공한 선택자를 만족하는 NodeList를 반환)

## DOM 조작 - 속성 조작
### 1. 클래스 속성 조작 : 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
- element.classList.add() : 지정한 클래스 값을 추가
- element.classList.remove() : 지정한 클래스 값을 제거
- element.classList.toggle() : 클래스가 존재한다면 제거하고 false를 반환(존재하지 않으면 클래스를 추가하고 true를 반환)

### 2. 일반 속성 조작
- element.getAttribute() : 해당 요소에 지정된 값을 반환(조회)
- element.setAttribute(name. vlaue) : 지정된 요소의 속성 값을 설정 / 속성이 이미 있으면 기존 값을 생신 (그렇지 않으면 지정된 이름과 값으로 새 속성이 추가)
- element.removeAttribute() : 요소에서 지정된 이름을 가진 속성 제거

### DOM 요소 조작 메서드
- document.createElement(tagName) - 생성: 작성한 tagName의 HTML 요소를 생성하여 반환
- Node.appendChild() - 추가
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 추가된 Node 객체를 반환
- Node.removeChild() - 삭제
  - DOM에서 자식 Node를 제거
  - 제거된 Node를 반환