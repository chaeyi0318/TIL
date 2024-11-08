<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg"
      @update-name="updateName"
    />
    
    <!-- <button @click="$emit('someEvent')">클릭!</button> -->
    <button @click="buttonClick">클릭!</button>
    <button @click="emitArgs">추가 인자 전달!</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';

// 내려 받은 props를 선언
// 문자열 배열을 사용한 선언
// defineProps(['myMsg'])

// 객체를  사용한 선언
defineProps({
  myMsg: String,
  dynamicProps: String
})

// props 데이터를 활용해야하는 경우
// const props = defineProps({ myMsg: String })
// console.log(props)
// console.log(props.myMsg)

// emit 이벤트 선언 (배열방식, 객체방식)
// 배열 방식
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function() {
  emit('someEvent')
}

const emitArgs = function() {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function() {
  emit('updateName')
}
</script>

<style scoped>

</style>