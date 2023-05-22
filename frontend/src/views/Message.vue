<script setup>
import Header from '@/components/Header.vue'
import Message from '@/components/Message.vue'
import { ref, onMounted } from 'vue';

const showMessage = ref(false);

onMounted(async () => {
    await new Promise((resolve) => setTimeout(resolve, 1000)); 
    showMessage.value = true;
});

</script>

<template>
    <div class="main-2">
        <Header />
        <Suspense>
            <template #default>
                <Message v-if="showMessage"/>
                <p v-else>Loading...</p>
            </template>
            <template #fallback>
                <p>Loading...</p>
            </template>
        </Suspense>
    </div>
</template>

<style scoped>
.main-2 {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
}
</style>