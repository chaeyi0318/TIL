## Template Syntax
- DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용

### Template Syntax 종류
- Text Interpolation
  ```html
    <p>Message: {{ msg }}</p>
  ```
  - 데이터 바인딩의 가장 기본적인 형태
  - 이중 중괄호 구문(콧수염 구문)을 사용
  - 콧수염 구문을 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
  - msg 속성이 변경될 때마다 업데이트 됨

- Raw HTML
  ```html
  <div v-html="raw-html"></div>

  const rawHtml = ref('<span style="color:red">This is should be red.</span>')
  ```
  - 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야 함

- Attribute Bindings
  ```html
  <div v-bind:id="dynamicId"></div>

  const dynamicId = ref('my-id')
  ```
  - 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
  - HTML을 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
  - 바인딩 값이 null이나 undefind인 경우 렌더링 요소에서 제거됨

- JavaScript Expressions
  ```html
  {{ number + 1 }}
  {{ ok ? 'YES' : 'NO' }}
  {{ message.split('').reverse.join('') }}

  <div v-bind:id="`list-${id}`"></div>
  ```
  - vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
  - vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
    1. 콧수염 구문 내부
    2. 모든 derective의 속성 값("v-"로 시작하는 특수 속성)
  - Expressions 주의사항
    - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
      - 표현식은 값으로 평가할 수 있는 코드 조각(return 뒤에 사용할 수 있는 코드여야 함)
    - 작동하지 않는 경우
      ```html
      <!-- 표현식이 아닌 선언식 -->
      {{ const number = 1 }}

      <!-- 제어문은 삼항 표현식을 사용해야 함 -->
      {{ if (ok) { return message } }}
      ```


## Directive - 'v-' 접두사가 있는 특수 속성
### 특징
- Directive의 속성 값은 단일 JavaScript 표현식이어야 함
- 표현식 값이 변경 될 때 DOM에 반응적으로 업데이트를 적용


### Directive - "Arguments"
- 일부 directive는 뒤에 콜론으로 표시되는 인자를 사용할 수 있음

### Directive - "Modifiers"
- . 으로 표시되는 특수 접미사로 directive가 특별한 방식으로 바인딩되어야 함을 나타냄


## Dynamically data Binding
### v- bind : 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩
- v-bind  사용처
1. Attribute Bindings (속성 바인딩)
  - HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함
  ![alt text](image.png)
  ![alt text](image-1.png)
  
  ### Dynamic attribute name (동적 인자 이름)
  - 대괄호로 감싸서 directive argument에 JavaScript 표현식을 사용할 수 있음
  - 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨

2. Class and Style Bindings (클래스와 스타일 바인딩)
- 클래스와 스타일은 모둔 HTML 속성이므로 다른 속성과 마찬가지로 v-bind를 사용하여 동적으로 문자열 값을 할당할 수 있음
- Vue는 class 및 style 속성 값을 v-bind로 사용할 때 객체 또는 배열을 활용하여 작성할 수 있도록 함


### Class and Style Bidings가 가능한 경우
1. Binding HTML Classes
  - Binding to Objects
  - Binding to Arrays
2. Binding Inline Style
  - Binding to Objects
  -. Binding to Arrays