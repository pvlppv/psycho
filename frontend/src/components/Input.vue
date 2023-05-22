<script setup>
import { ref } from 'vue'
import ws from '@/assets/websockets.js'

const message = ref()

const sendMessage = (event) => {
    ws.send(message.value)
    message.value = ''
    event.preventDefault()
}

</script>

<template>
  <form class="main-feed-send">
    <div style="position: relative; height: 54px; width: 720px;">
      <div style="position: absolute; height: 54px; width: 720px; display: flex; align-items: flex-end;">
        <el-input v-model="message" @keydown.enter.exact.prevent="sendMessage" class="main-feed-send-input" type="textarea" resize="none" :autosize="{minRows: 2, maxRows: 10}" show-word-limit minlength="100" maxlength="30000"/>
      </div>
    </div>
  </form>
</template>

<style scoped>
.main-feed-send {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: 2rem;
}
.main-feed-send-input {
    width: 45rem;
    border: 1px solid var(--white-color);
    border-radius: 0.4rem;
    color: var(--white-color);
    resize: both;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
.main-feed-send-button {
    border: 1px solid var(--white-color);
    border-radius: 0.4rem;
    background: var(--black-color);
    color: var(--white-color);
    width: 7rem;
    padding: 1rem;
    cursor: pointer;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
.el-textarea {
  --el-input-text-color: var(--white-color);
  --el-input-border-color: none;
  --el-input-bg-color: var(--black-color);
  --el-input-placeholder-color: var(--white-color);
  --el-input-hover-border-color: none;
  --el-input-focus-border-color: none;
  --el-fill-color-blank: var(--black-color);
  --el-color-info: var(--white-color);
  --el-border-radius-base: 0.4rem;
}
</style>
