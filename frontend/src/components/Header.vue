<script setup>
import theme from '@/assets/theme.js'; 
import { ElNotification } from 'element-plus'

// Notification
const notification = () => {
  ElNotification({
    title: 'Временно не доступно.',
    customClass: 'main-notification',
    type: 'info',
  })
}
</script>

<template>
  <div class="main-title">
    <div class="badge">
        <span class="badge-value">Alpha</span>
        <h1 class="main-title2">Thoughty</h1>
    </div>
    <p class="main-description">- бесконечная лента анонимных сообщений, где каждый может излить свою душу</p>
    <div class="main-settings">
        <el-tooltip effect="customized" content="О приложении" placement="bottom" :enterable="false" :hide-after="0" :offset="15">
            <i class="main-settings-one bx bx-info-circle" @click="notification"></i>
        </el-tooltip>
        <el-tooltip effect="customized" content="Тема" placement="bottom" :enterable="false" :hide-after="0" :offset="15">
            <i class="main-settings-one bx" :class="{ 'bxs-moon': theme.darkTheme.value, 'bxs-sun': !theme.darkTheme.value }" @click="theme.toggleTheme"></i>
        </el-tooltip>
        <el-tooltip effect="customized" content="Язык" placement="bottom" :enterable="false" :hide-after="0" :offset="15">
            <i class="main-settings-one bx bx-world" @click="notification"></i>
        </el-tooltip>
    </div> 
  </div>
</template>

<style scoped>
.badge {
    position: relative;
    display: inline-block;
}

.badge-value {
    position: absolute;
    top: -10px;
    right: -30px;
    padding: 4px 8px;
    background-color: var(--white-color);
    color: var(--black-color);
    font-size: 0.8rem;
    border-radius: 1rem;
}

.main-title2 {
    margin: 0;
    padding: 0;
    font-size: 24px;
}

.main-title {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}
.main-title2 {
    color: var(--white-color);
    font-size: 4rem;
    text-shadow: 0px 0px 25px var(--shadow-white-color), 0px 15px 25px var(--shadow-white-color);
}
.main-description {
    color: var(--white-color);
    font-size: 1rem;
    font-weight: var(--fw-semi-bold);
    text-shadow: 0px 0px 25px var(--shadow-white-color), 0px 15px 25px var(--shadow-white-color);
}
.main-settings {
    display: flex;
    color: var(--white-color);
    font-size: 1.2rem;
    gap: 1rem;
}
.main-settings-one {
    color: var(--white-color);
    cursor: pointer;
}
</style>
