<script setup>
import { ref } from 'vue';
import theme from '@/assets/theme.js';

const skeletonOpacity = ref(theme.darkTheme.value ? 0.2 : 1);

</script>

<template>
    <el-skeleton animated style="display: flex; align-items: center; justify-content: center;">
        <template #template>
            <div class="main-feed-skeleton">
                <div class="main-feed-2-skeleton" id="el-skeleton" :style="{opacity: skeletonOpacity}">
                    <div v-for="i in 4" :key="i" class="main-feed-message-skeleton">
                        <el-skeleton-item class='main-feed-message-pic-skeleton' variant="circle" />                     
                        <div class="main-feed-message-text-skeleton">
                            <div class="main-feed-message-text-1-skeleton">
                                <el-skeleton-item class="main-feed-message-text-1-username-skeleton" variant="text" />
                                <el-skeleton-item class="main-feed-message-text-1-time-skeleton" variant="text" />
                            </div>
                            <el-skeleton-item class="main-feed-message-text-2-skeleton" variant="text" />
                            <el-skeleton-item class="main-feed-message-text-2-skeleton-2" variant="text" />
                            <el-skeleton-item class="main-feed-message-text-2-skeleton-3" variant="text" />
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </el-skeleton>
</template>

<style scoped>
.main-feed-skeleton {
    width: 60rem;
    height: 30rem;
    overflow-y: scroll;
    border: 1px solid var(--white-color);
    border-radius: 0.7rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    padding: 2rem 2rem;
}
.main-feed-2-skeleton {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}
.main-feed-message-skeleton {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
}
.main-feed-message-pic-skeleton {
    width: 1.5rem;
    height: 1.5rem;
    margin-top: 0.4rem;
    color: var(--white-color);
}
.main-feed-message-text-skeleton {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    color: var(--white-color);
    font-size: 0.8rem;
}
.main-feed-message-text-1-skeleton {
    display: flex;
    align-items: center;
    gap: 0.8rem;
}
.main-feed-message-text-1-username-skeleton {
    width: 4rem;
    height: 0.5rem;
}
.main-feed-message-text-1-time-skeleton {
    opacity: 0.5;
    width: 3rem;
    height: 0.5rem;
}
.main-feed-message-text-2-skeleton {
    width: 53rem;
    height: 0.5rem;
}
.main-feed-message-text-2-skeleton-2 {
    width: 53rem;
    height: 0.5rem;
}
.main-feed-message-text-2-skeleton-3 {
    width: 40rem;
    height: 0.5rem;
}
</style>