## 객체
### Object - 키로 구분된 데이터 집합을 저장하는 자료형
### 객체 구조
- 중괄호를 이용해 작성
- 중괄호 안에는 key : value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
- key는 문자형만 허용
- value는 모든 자료형 허용

```javascript
const user = {
  name: 'Alice',
  'key with space': true,
  greeting: function() {
    return 'hello'
  }
}

// 속성 참조
console.log(user.name)    // Alice
console.log(user['key with space'])   // true

// 추가
user.address = 'korea'

// 수정
user.name = 'Bella'

// 삭제
delete user.name
```


### in 연산자
```javascript
console.log('greeting' in user)   // true
console.log('country' in user)    // false
```


### Method - 객체 속성에 정의된 함수
- object.method() 방식으로 호출
- 메서드는 객체를 '행동'할 수 있게 함
- 'this' 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음


### this - 함수나 메서드를 호출한 객체를 가리키는 키워드
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
```javascript
const person = {
  name: 'Alice',
  greeting: function () {
    return `Hello my name is ${this.name}`
  }
}

console.log(person.greeting())    // Hello my name is Alice
```
### **JavaScript에서 this는 함수를 "호출하는 방법"에 따라 가리키는 대상이 다름**
- 단순 호출 : 전역 객체
```javascript
const myFunc = function () {
  return this
}

console.log(myFunc())   // window
```

- 메서드 호출 : 메서드를 호출한 객체
```javascript
const myObj = {
  data: 1,
  myFunc: function() {
    return this
  }
}

console.log(myObj.myFunc())   //myObj
```


### 중첩된 함수에서의 this 문제점과 해결책
```javascript
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number)) {
      console.log(this)   // window
    }
  }
}

console.log(myObj2.myFunc())
```
> forEach의 인자로 작성된 함수는 일반적인 함수 호출이기 때문에 this가 전역 객체를 가리킴

```javascript
const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(number) => {
      console.log(this)   // myObj3
    }
  }
}

console.log(myObj3.myFunc())
```
> 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수(myFunc)에서 this의 값을 가져옴


### JavaScript 'this' 정리
- javascript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- javascript에서 this는 함수가 "호출되는 방식"에 따라 결정되는 현재 객체를 나타냄
- Python의 self와 Java의 this가 선언 시 이미 값이 정해지는 것에 비해 javascript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨 (동적 할당)
- this가 미리 정해지지 않고 호출 방식에 의해 결정되는 것은
  - 장점 : 함수를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
  - 단점 : 이런 유연함이 실수로 이어질 수 있다는 것


## 추가 객체 문법
### 단축 속성
- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음

```javascript
const name = 'Alice'
const age = 30

const user = {
  name,
  age,
}
```


### 단축 메서드
- 메서드 선언 시 function 키워드 생략 가능
```javascript

const myObj = {
  myFunc() {
    return 'hello'
  }
}
```


### 계산된 속성
- 키가 대괄호로 둘러싸여 있는 속성
- 고정된 값이 아닌 변수 값을 사용할 수 있음

```javascript
const product = prompt('물건 이름 입력')
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,
  [prefix + suffix]: 'value',
}
```


### 구조 분해 할당
- 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법

```javascript
const userInfo = {
  firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'
}

const { firstName, userId, email } = userInfo

console.log(firstName, userId, email)
```


### Object with '전개 구문'
- 객체 복사
  - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

```javascript
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}

console.log(newObj)   // {a: 1, b: 2, c: 3, d: 4, e: 5}
```


### 유용한 객체 메서드
```javascript
const profile = {
  name: 'Alice',
  age: 30,
}

console.log(Object.keys(profile))   // ['name', 'age']
console.log(Object.values(profile))   // ['Alice', 30]
```


### Optional chaining('?.')
- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환

```javascript
const user = {
  name: 'Alice',
  greeting: function () {
    return 'hello'
  }
}

console.log(user.address.street)    // Uncaught TypeError
console.log(user.address?.street)   // undefined

console.log(user.nonMethod())     // Uncaught TypeError
console.log(user.nonMethod?.())   // undefined
```

> 만약 Optional chaining을 사용하지 않는다면 '&&' 연산자를 사용해야 함

```javascript
const user = {
  name: 'Alice',
  greeting: function() {
    return 'hello'
  }
}

console.log(user.address && user.address.street)    // undefined
```


#### Optional chaining 장점
- 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음
- 어떤 속성이 필요한지에 대한 보증이 확실하지 않은 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음


#### Optional chaining 주의사항
1. 존재하지 않아도 괜찮은 대상에만 사용해야 함(남용 X)
  - 왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용
  - 중첩 객체를 에러 없이 접근하는 것이 사용 목적이기 때문

  ```javascript
  user?.address?.street     // Bad
  user.address?.street      // Good
  ```

2. Optional chaining 아의 변수는 반드시 선언되어 있어야 함
```javascript
console.log(myObj?.address)   // X
```


#### Optional chaining 정리
1. obj?.prop : obj가 존재하면 obj.prop을 반환하고, 그렇지 않으면 undefined를 반환
2. obj?.[prop] : obj가 존재하면 obj[prop]을 반환하고, 그렇지 않으면 undefined를 반환
3. obj?.method() : obj가 존재하면 obj.method()를 호출하고, 그렇지 않으면 undefined를 반환


## JSON
- JavaScript Object Notation
- key - value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 **"문자열"**
- JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함


### Object <-> JSON 변환
```JavaScript
const jsonObj = {
  coffee: 'Americano',
  icecream: 'Cookie and cream',
}

// Object -> JSON
const objToJson = JSON.stringify(jsonObj)

console.log(objToJson)
console.log(typeof objToJson)   // String

const jsonToObj = JSON.parse(objToJson)

console.log(jsonToObj)
console.log(typeof jsonToObj)   // object
```


## 클래스
- 객체를 생성하기 위한 템플릿 : 객체의 속성, 메서드를 정의하는 청사진 역할


### 클래스 기본 문법
1. class 키워드
2. 클래스 이름
3. 생성자 메서드 : constructor()


### 클래스 특징
- ES6에서 도입
- 생성자 함수를 사용하여 객체를 생성하는 이전의 방식을 객체 지향적으로 표현하고자 만들어짐
- 그래서 클래스는 내부적으로 생성자 함수를 기반으로 동작함

```JavaScript
// 생성자 함수
function Member(name, age) {
  this.name = name
  this.age = age
  this.sayHi = function () {
    console.log(`Hi I am ${this.name}`)
  }
}

// 클래스
class Member {
  constructor(name, age) {
    this.name = name
    this.age = age
  }

  sayHi() {
    cosole.log(`Hi I am ${this.name}`)
  }
}
```


### new 연산자 : 클래스나 생성자 함수를 사용하여 새로운 객체를 생성
```JavaScript
const instance = new ClassName(arg1, arg2)
```
- 특징
  - 클래스의 constructor()는 new 연산자에 의해 자동으로 호출되며 특별한 절차 없이 객체를 초기화 할 수 있음
  - new 없이 클래스를 호출하면 TypeError 발생