<script setup>
import { ref, unref, onMounted, onUnmounted, computed, defineComponent } from 'vue'
import ws from '@/assets/websockets.js'
import getMessages from '@/assets/getMessages.js' 
import TextClamp from 'vue3-text-clamp';
import dayjs from 'dayjs'
import { ClickOutside as vClickOutside } from 'element-plus'
import postReport from '@/assets/postReport'
import { ElNotification } from 'element-plus'

// Websockets
ws.onmessage = (event) => {
    console.log(event)
    const newMessage = {
        id: messages.value.length,
        message_text: event.data,
    };
    messages.value.unshift(newMessage)
}

// Infinite Scrolling
const limit = 20;
const messages = ref([]);
const loading = ref(false)
const noMore = ref(false)
const disabled = computed(() => loading.value || noMore.value)

messages.value = await getMessages(limit, 0);

const getMessagesOnScroll = async () => {
    try {
        loading.value = true
        // await new Promise(resolve => setTimeout (resolve, 3000));
        const newMessages = await getMessages(limit, messages.value.length);
        loading.value = false
        if (newMessages.length === 0) {
            noMore.value = true;
            return;
        }
        messages.value.push(...newMessages);
    } catch (error) {
        console.log(error)
    }
}

// Messages Tools
const tools = ref(null)
const toolOpacity = ref([])

const showTools = (index) => {
  toolOpacity.value[index] = 1
}
const hideTools = (index) => {
  toolOpacity.value[index] = 0
}

const formatDate = (dateString) => {
    const date = dayjs(dateString)
    const now = dayjs()

    const diffYears = now.diff(date, 'year')
    const diffMonths = now.diff(date, 'month')
    const diffWeeks = now.diff(date, 'week')
    const diffDays = now.diff(date, 'day')
    const diffHours = now.diff(date, 'hour')
    const diffMinutes = now.diff(date, 'minute')

    if (diffYears > 0) {
        return `${diffYears}г`
    } else if (diffMonths > 0) {
        return `${diffMonths}м`
    } else if (diffWeeks > 0) {
        return `${diffWeeks}н`
    } else if (diffDays > 0) {
        return `${diffDays}д`
    } else if (diffHours > 0) {
        return `${diffHours}ч`
    } else if (diffMinutes > 0) {
        return `${diffMinutes}мин`
    } else {
        return "Только что"
    }
}

// Share
const notificationReply = () => {
  ElNotification({
    title: 'Ссылка скопирована.',
    message: 'Ссылка скопирована.',
    customClass: 'main-feed-message-tools-tool-notification',
  })
}

// Report
const notificationReport = () => {
  ElNotification({
    title: 'Жалоба отправлена',
    message: 'Жалоба отправлена.',
    customClass: 'main-feed-message-tools-tool-notification',
  })
}

</script>

<template>
    <div class="main-feed-1">
        <DynamicScroller class="main-feed" :items="messages" :min-item-size="94.59" v-infinite-scroll="getMessagesOnScroll" :infinite-scroll-disabled="disabled" :infinite-scroll-delay="200" :infinite-scroll-distance="1000" :infinite-scroll-immediate="false">
            <template v-slot="{ item, index, active }">
                <DynamicScrollerItem class="main-feed-message" :item="item" :active="active" :size-dependencies="[item.message_text]" :data-index="index" @mouseover="showTools(index)" @mouseout="hideTools(index)">
                    <i class='main-feed-message-pic bx bxs-user'></i> 
                    <div class="main-feed-message-text">
                        <div class="main-feed-message-text-1">
                            <div class="main-feed-message-text-1-username">Аноним</div>
                            <div class="main-feed-message-text-1-time">{{ formatDate(item.created_at) }}</div>
                        </div>
                        <text-clamp class="main-feed-message-text-2" :text="item.message_text" :max-lines='5'>
                            <template #after="{ expand, collapse, toggle, clamped, expanded }">
                                <button class="main-feed-message-text-2-button" v-if="clamped" @click="expand">ещё</button>
                            </template>
                        </text-clamp>
                        <div class="main-feed-message-text-3">
                            <p class="main-feed-message-text-3-one">Ответить</p>
                            <i class='main-feed-message-text-3-dots bx bx-dots-horizontal-rounded'></i>
                            <p class="main-feed-message-text-3-one">0 ответов</p>
                        </div>
                    </div>
                    <div class="main-feed-message-tools" ref="tools" :style="{ opacity: toolOpacity[index] }">
                        <el-tooltip effect="customized" content="Открыть" placement="bottom" transition="none" :enterable="false" :hide-after="0" :offset="15">
                            <router-link :to="{ name: 'Message', params: { message_id: item.id } }" class="main-feed-message-tools-tool"><i class='bx bx-expand'></i></router-link>
                        </el-tooltip>
                        <el-tooltip effect="customized" content="Поделиться" placement="bottom" transition="none" :enterable="false" :hide-after="0" :offset="15">
                            <i class='main-feed-message-tools-tool bx bx-share' @click="notificationReply"></i>
                        </el-tooltip>
                        <el-tooltip effect="customized" content="Пожаловаться" placement="bottom" transition="none" :enterable="false" :hide-after="0" :offset="15">
                            <i class='main-feed-message-tools-tool bx bx-error' @click="notificationReport"></i>
                        </el-tooltip>
                    </div>
                </DynamicScrollerItem>
            </template>
        </DynamicScroller>
        <!-- <div v-if="loading" class="main-feed-loading"><div class="main-feed-loading-spinner"><div></div><div></div><div></div><div></div><div></div></div></div> -->
    </div>
</template>

<style>
.main-feed-1 {
    position: relative;
    width: 60rem;
    height: 30rem;
    border: 1px solid var(--white-color);
    border-radius: 0.7rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    overflow: auto;
}
.main-feed {
    height: 100%;
    padding: 1rem 2rem;
}
.main-feed-message {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    padding: 1rem 0rem;
}
.main-feed-message-pic {
    margin-top: 0.4rem;
    font-size: 1.5rem;
    color: var(--white-color);
}
.main-feed-message-text {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
    color: var(--white-color);
    font-size: 0.8rem;
}
.main-feed-message-text-1 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.main-feed-message-text-1-username {
    font-weight: var(--fw-semi-bold);
}
.main-feed-message-text-1-time {
    font-size: 0.7rem;
    opacity: 0.5;
}
.main-feed-message-text-2-button {
    cursor: pointer;
    border: none;
    background: none;
    color: var(--white-color);
    opacity: 0.5;
    font-size: 0.8rem;
    margin-left: 0.2rem;
}
.main-feed-message-text-3 {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    color: var(--white-color);
    margin-top: 0.5rem;
    opacity: 0.5;
}
.main-feed-message-text-3-one {
    cursor: pointer;
    font-size: 0.7rem;
}
.main-feed-message-text-3-one:hover {
    text-decoration: underline;
}
.main-feed-message-text-3-dots {
    font-size: 0.8rem;
}
.main-feed-message-tools {
    position: absolute;
    right: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.8rem;
    color: var(--white-color);
    background: var(--black-color);
    opacity: 0;
}
.main-feed-message-tools-tool {
    color: var(--white-color);
    cursor: pointer;
}
.main-feed-loading {
    width: 50px;
    height: 50px;
    display: inline-block;
    overflow: hidden;
    background: var(--black-color);
}
.main-feed-loading-spinner {
    width: 100%;
    height: 100%;
    position: relative;
    transform: translateZ(0) scale(0.5);
    backface-visibility: hidden;
    transform-origin: 0 0;
}
.main-feed-loading-spinner div {
    position: absolute;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    transform: translate(42px,42px) scale(1);
    background: var(--white-color);
    animation: main-feed-loading-spinner 3.3333333333333335s infinite cubic-bezier(0,0.5,0.5,1);
}
.main-feed-loading-spinner div:nth-child(1) {
    background: var(--white-color);
    transform: translate(76px,42px) scale(1);
    animation: main-feed-loading-spinner-r 0.8333333333333334s infinite cubic-bezier(0,0.5,0.5,1), main-feed-loading-spinner-c 3.3333333333333335s infinite step-start;
}.main-feed-loading-spinner div:nth-child(2) {
    animation-delay: -0.8333333333333334s;
    background: var(--white-color);
}.main-feed-loading-spinner div:nth-child(3) {
    animation-delay: -1.6666666666666667s;
    background: var(--white-color);
}.main-feed-loading-spinner div:nth-child(4) {
    animation-delay: -2.5s;
    background: var(--white-color);
}.main-feed-loading-spinner div:nth-child(5) {
    animation-delay: -3.3333333333333335s;
    background: var(--white-color);
}
.main-feed-loading-spinner div { box-sizing: content-box; }
@keyframes main-feed-loading-spinner {
    0% { transform: translate(8px,42px) scale(0); }
    25% { transform: translate(8px,42px) scale(0); }
    50% { transform: translate(8px,42px) scale(1); }
    75% { transform: translate(42px,42px) scale(1); }
    100% { transform: translate(76px,42px) scale(1); }
}
@keyframes main-feed-loading-spinner-r {
    0% { transform: translate(76px,42px) scale(1); }
    100% { transform: translate(76px,42px) scale(0); }
}
.el-popper.is-customized {
    color: var(--black-color);
    background: var(--white-color);
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
.el-popper.is-customized .el-popper__arrow::before {
    background: var(--white-color);
}
.main-feed-message-tools-tool-notification {
    background: var(--black-color);
    color: var(--white-color);
    border-radius: 5rem;
}
</style>
