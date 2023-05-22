<script setup>
import { ref } from 'vue'
import getMessage from '@/assets/getMessage.js'
import { useRoute } from 'vue-router';

const route = useRoute();

const message = ref(null)

message.value = await getMessage(route.params.message_id);

</script>

<template>
    <div v-for="msg in message" class="main-message">
        <div class="main-message-one">
            <p class="main-message-one-h1">Лобби:</p>
            <router-link :to="{ name: 'Main' }" class="main-message-lobby-name">{{ msg.lobby_name }}</router-link>
        </div>
        <div class="main-message-one">
            <p class="main-message-one-h1">Дата создания:</p>
            <p>{{ msg.created_at }}</p>
        </div>
        <div class="main-message-one">
            <p class="main-message-one-h1">Сообщение:</p>
            <p>{{ msg.message_text }}</p>
        </div>
    </div>
</template>

<style scoped>
.main-message {
    width: 60rem;
    height: 30rem;
    border: 1px solid var(--white-color);
    border-radius: 0.7rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    overflow: auto;
    color: var(--white-color);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 2rem;
    padding: 2rem 2rem;
}
.main-message-one {
    display: flex;
    gap: 0.5rem;
}
.main-message-one-h1 {
    font-weight: var(--fw-semi-bold);
}
.main-message-lobby-name {
    text-decoration: underline;
    color: var(--white-color);
}
</style>