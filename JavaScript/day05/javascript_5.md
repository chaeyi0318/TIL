## 배열
### Array : 순서가 있는 데이터 집합을 저장하는 자료구조
- 대괄호를 이용해 작성
- 요소의 자료형은 제약 없음
- length 속성을 사용해 배열에 담긴 요소 개수 확인 가능

#### 주요 메서드
- push / pop : 배열의 **끝에** 요소를 추가 / 제거
- unshift / shift : 배열의 **앞에** 요소를 추가 / 제거


## Array Helper Method - 배열 조작을 보다 쉽게 수행할 수 있는 특벽한 메서드 모음
### Array Helper Method
- ES6에 도입
- 배열의 각 요소를 순회하며 각 요소에 대해 함수(**콜백함수**)를 호출
- 대표 메서드 : forEach(), map(), filter(), every(), som(), reduce() 등
- 메서드 호출 시 인자로 함수(**콜백함수**)를 받는 것이 특징


### 콜백 함수 (Callback function)
- 다른 함수에 인자로 전달되는 함수
  - 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
```javascript
const numbers = [1, 2, 3]

numbers.forEach(function (num) {
  console.log(num ** 2)    // 1 4 9
})

const callBackFunction = funtion (num) {
  console.log(num ** 2)   // 1 4 9
}

numbers.forEach(callBackFunction)
```


### 주요 Array Helper Methods
- forEach
  - 배열 내의 모든 요소 각각에 대해 함수를 호출
  - 반환 값 없음

- map
  - 배열 내의 모든 요소 각각에 대해 함수를 호출
  - 함수 호출 결과를 모아 새로운 배열을 반환


### forEach() : 배열의 각 요소를 반복하며 모든 요소에 대해 함수를 호출
- 구조
![alt text](image.png)
- 콜백함수는 3가지 매개변수로 구성
  1. item : 처리할 배열의 요소
  2. index : 처리할 배열 요소의 인덱스 (선택 인자)
  3. array : forEach를 호출한 배열 (선택 인자)
- 반환 값 : undefined

```javascript
const names = ['Alice', 'Bella', 'Cathy']

// 일반 함수
names.forEach(function (name) {
  console.log(name)
})

// 화살표 함수
names.forEach((name) => {
  console.log(name)
})
```


### map() : 배열의 모든 요소에 대해 함수를 호출하고, 반환된 호출 결과 값을 모아 새로운 배열을 반환
- 구조
![alt text](image-1.png)
- forEach의 매개변수와 동일
- 반환 값
  - 배열의 각 요소에 대해 실행한 "callback의 결과를 모든 새로운 배열"
  - forEach 동작 원리와 같지만 forEach와 달리 **새로운 배열**을 반환함

```javascript
const persons = [
  { name: 'Alice', age: 20 },
  { name: 'Bella', age: 21 }
]

let result1 = []

for (const person of persons) {
  result1.push(person.name)
}   // ['Alice', 'Bella']

const result = persons.map(function (person) {
  return person.name
})    // ['Alice', 'Bella']
```


## 배열 순회 종합
- for loop
  - 배열의 인덱스를 이용하여 각 요소에 접근
  - break, continue 사용 가능
- for...of
  - 배열 요소에 바로 접근 가능
  - break, continue 사용 가능
- forEach() : **사용권장**
  - 간결하고 가독성이 높은
  - callback 함수를 이용하여 각 요소를 조작하기 용이
  - break, continue 사용 불가


### 기타 Array Helper Methods
- filter : 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- find : 콜백 함수의 반환 값이 참이면 해당 요소를 반환
- some : 배열의 요소 중 적어도 하나라도 콜백 함수를 통과하면 true를 반환하며 즉시 배열 순회 중지, 반면에 모두 통과하지 못하면 false를 반환
- every : 배열의 모든 요소가 콜백 함수를 통과하면 true를 반환, 반면에 하나라도 통과하지 못하면 즉시 false를 반환하고 배열 순회 중지


## 배열 with '전개 구문'
- 배열 복사
```javascript
let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발']

console.log(lyrics)   // ['머리', '어깨', '무릎', '발']
```


## 콜백 함수의 이점
### 콜백 함수 구조를 사용하는 이유
1. 함수의 재사용성 측면
  - 함수를 호출하는 코드에서 콜백 함수의 동작을 자유롭게 변경할 수 있음
  - 예를 들어, map 함수는 콜백 함수를 인자로 받아 배열의 각 요소를 순회하며 콜백 함수를 실행
  - 이때, 콜백 함수는 각 요소를 변환ㅎ하는 로직을 담당하므로, map 함수를 호출하는 코드는 간결하고 가독성이 높아짐
2. 비동기적 처리 측면
  - setTimeout 함수는 콜백 함수를 인자로 받아 일정 시간이 지난 후에 실행됨
  - 이때, setTimeout 함수는 비동기적으로 콜백 함수를 실행하므로, 다른 코드의 실행을 방해하지 않음


## forEach에서 break 하는 대안
- some과 every의 특징을 활용해 break를 사용하는 것처럼 활용 가능
```javascript
// some
const array = [1, 2, 3, 4, 5]

const isEvenNumber = array.some(function (element) {
  return element % 2 == 0
})
console.log(isEvenNumber)   // true

// every
const array = [1, 2, 3, 4, 5]

const isAllEvenNumber = array.every(function (element) {
  return element % 2 == 0
})

console.log(isAllEvenNumber)    // false
```


## 배열은 객체다
- 배열도 키와 속성을 담고 있는 참조 타입의 객체
- 배열의 요소를 대괄호 접근법을 사용해 접근하는 건 객체 문법과 같음
- 숫자형 키를 사용함으로써 배열은 객체 기본 기능 이외에도 "순서가 있는 컬렉션"을 제어하게 해주는 특별한 메서드를 제공하는 것
- 배열은 인덱스를 키로 가지며 length 속성을 갖는 특수한 객체