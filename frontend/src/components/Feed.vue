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
    const message = JSON.parse(event.data);
    if (message.event === 'error') {
        ElNotification({
            title: 'Ошибка',
            message: message.data,
            customClass: 'main-notification',
            type: 'error',
        });
    } else {
        const newMessage = {
            id: messages.value.length,
            message_text: message.data.message_text,
        };
        messages.value.unshift(newMessage)
    }
};

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
                            <p class="main-feed-message-text-3-one" @click="notification">Ответить</p>
                            <div class="main-feed-message-text-3-one-divider"></div>
                            <p class="main-feed-message-text-3-one" @click="notification">0 ответов</p>
                        </div>
                    </div>
                    <div class="main-feed-message-tools" ref="tools" :style="{ opacity: toolOpacity[index] }">
                        <el-tooltip effect="customized" content="Открыть" placement="bottom" :enterable="false" :hide-after="0" :offset="15">
                            <!-- <router-link :to="{ name: 'Message', params: { message_id: item.id } }" class="main-feed-message-tools-tool"><i class='bx bx-expand'></i></router-link> -->
                            <i class='main-feed-message-tools-tool bx bx-expand' @click="notification"></i>
                        </el-tooltip>
                        <el-tooltip effect="customized" content="Поделиться" placement="bottom" :enterable="false" :hide-after="0" :offset="15">
                            <i class='main-feed-message-tools-tool bx bx-share' @click="notification"></i>
                        </el-tooltip>
                        <el-tooltip effect="customized" content="Пожаловаться" placement="bottom" :enterable="false" :hide-after="0" :offset="15">
                            <i class='main-feed-message-tools-tool bx bx-error' @click="notification"></i>
                        </el-tooltip>
                    </div>
                </DynamicScrollerItem>
            </template>
        </DynamicScroller>
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
    gap: 0.5rem;
    color: var(--white-color);
    margin-top: 0.5rem;
    opacity: 0.5;
}
.main-feed-message-text-3-one {
    cursor: pointer;
    font-size: 0.7rem;
    text-decoration: none;
    transition: text-decoration 0.3s; 
    position: relative;
}
.main-feed-message-text-3-one::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -2px;
    width: 100%;
    height: 1px; 
    background: var(--white-color); 
    transform: scaleX(0);
    transform-origin: center; 
    transition: transform 0.2s;
}

.main-feed-message-text-3-one:hover::after {
    transform: scaleX(1);
}
.main-feed-message-text-3-one-divider {
    content: "";
    background: var(--white-color);
    color: var(--white-color);
    width: 1px;
    height: 12px;
    margin: 0px 10px;
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
    transition: opacity 0.3s;
}
.main-feed-message-tools-tool {
    color: var(--white-color);
    cursor: pointer;
}
.el-popper.is-customized {
    color: var(--black-color);
    background: var(--white-color);
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
.el-popper.is-customized .el-popper__arrow::before {
    background: var(--white-color);
}

.main-notification {
    background: var(--black-color) !important;
    --el-notification-width: 300px !important;
    --el-notification-padding: 14px 26px 14px 13px !important;
    --el-notification-radius: 0.5rem !important;
    --el-notification-shadow: var(--el-box-shadow-light) !important;
    --el-notification-border-color: var(--white-color) !important;
    --el-notification-icon-size: 24px !important;
    --el-notification-close-font-size: var(--el-message-close-size, 16px) !important;
    --el-notification-group-margin-left: 13px !important;
    --el-notification-group-margin-right: 8px !important;
    --el-notification-content-font-size: var(--el-font-size-base) !important;
    --el-notification-content-color: var(--white-color) !important;
    --el-notification-title-font-size: 0.9rem !important;
    --el-notification-title-color: var(--white-color) !important;
    --el-notification-close-color: var(--white-color) !important;
    --el-notification-close-hover-color: var(--white-color) !important;
    box-shadow: 0px 0px 10px var(--shadow-white-color), 0px 5px 10px var(--shadow-white-color) !important;
}
</style>
