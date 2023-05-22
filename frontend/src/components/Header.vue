<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import theme from '@/assets/theme.js'; 

const aboutLink = computed(() => {
  const route = useRoute();
  return route.path === '/' ? { name: 'About' } : { name: 'Main' };
});
const langLink = computed(() => {
  const route = useRoute();
  return route.path === '/' ? { name: 'Lang' } : { name: 'Main' };
});

</script>

<template>
  <div class="main-title">
    <h1 class="main-title2">Thoughty</h1>
    <p class="main-description">- бесконечная лента анонимных сообщений, где каждый может излить свою душу</p>
    <div class="main-settings">
        <el-tooltip effect="customized" content="О приложении" placement="bottom" transition="none" :enterable="false" :hide-after="0" :offset="15">
            <router-link :to="aboutLink"><i class="main-settings-one bx bx-info-circle"></i></router-link>
        </el-tooltip>
        <el-tooltip effect="customized" content="Тема" placement="bottom" transition="none" :enterable="false" :hide-after="0" :offset="15">
            <i class="main-settings-one bx" :class="{ 'bxs-moon': theme.darkTheme.value, 'bxs-sun': !theme.darkTheme.value }" @click="theme.toggleTheme"></i>
        </el-tooltip>
        <el-tooltip effect="customized" content="Язык" placement="bottom" transition="none" :enterable="false" :hide-after="0" :offset="15">
            <router-link :to="langLink"><i class="main-settings-one bx bx-world"></i></router-link>
        </el-tooltip>
    </div> 
  </div>
</template>

<style scoped>
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
.main-settings-about-window {
    position: absolute;
    top: 57.3%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: var(--black-color);
    z-index: 1;
    width: 50rem;
    height: 30rem;
    border: 1px solid var(--white-color);
    border-radius: 0.375rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    padding: 2rem 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2rem;
}
.main-settings-about-window-text {
    font-size: 0.8rem;
}
.main-settings-about-window-socials {
    display: flex;
    gap: 1.5rem;
    font-size: 1.5rem;
}
.main-settings-about-window-socials-social {
    color: var(--white-color);
}
.main-settings-about-window-support {
    display: flex;
    gap: 2rem;
}
.main-settings-about-window-support-text,
.main-settings-about-window-support-support {
    border: 1px solid var(--white-color);
    border-radius: 0.375rem;
    background: var(--black-color);
    color: var(--white-color);
    width: 10rem;
    padding: 1rem;
    cursor: pointer;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    font-size: 0.8rem;
}
.main-settings-about-window-footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.3rem;
}
.main-settings-about-window-politics {
    display: flex;
    gap: 0.4rem;
    font-size: 0.6rem;
}
.main-settings-about-window-politics-terms,
.main-settings-about-window-politics-privacy {
    color: var(--white-color);
    text-decoration: underline;
}
.main-settings-about-window-copyright {
    color: var(--white-color);
    font-size: 0.7rem;
    margin-top: auto;
}
.main-settings-theme {
    cursor: pointer;
}
.main-settings-lang {
    cursor: pointer;
}
.main-settings-lang-window {
    position: absolute;
    top: 57.3%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: var(--black-color);
    z-index: 1;
    width: 50rem;
    height: 30rem;
    border: 1px solid var(--white-color);
    border-radius: 0.375rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    padding: 2rem 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2rem;
}
.main-settings-lang-window-lang {
    display: flex;
    gap: 2rem;
}
.main-settings-lang-window-lang-en,
.main-settings-lang-window-lang-ru {
    width: 2rem;
    border: 1px solid var(--white-color);
    border-radius: 10%;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    cursor: pointer;
}
.main-settings-user-popup-background {
    position: absolute;
    background: var(--white-color);
    opacity: 0.7;
    width: 100%;
    height: 100%;
    z-index: 1;
    display: none;
}
.main-settings-user-popup {
    position: fixed;
    top: 57.3%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: var(--black-color);
    z-index: 2;
    width: 50rem;
    height: 30rem;
    border: 1px solid var(--white-color);
    border-radius: 0.375rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    padding: 2rem 2rem;
    display: none;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
    overflow-y: scroll;
    font-size: 0.8rem;
}
.main-settings-user-popup-accept {
    border: 1px solid var(--white-color);
    border-radius: 0.375rem;
    background: var(--black-color);
    color: var(--white-color);
    width: 12rem;
    padding: 1rem;
    cursor: pointer;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
</style>
