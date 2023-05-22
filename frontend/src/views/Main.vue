<script setup>
import { ref, onMounted, computed } from 'vue'
import FeedSkeleton from '@/components/FeedSkeleton.vue'

const showFeed = ref(false);

onMounted(async () => {
    await new Promise((resolve) => setTimeout(resolve, 1000));
    showFeed.value = true;
});
</script>

<template>
    <Header />
    <Suspense>
      <template #default>
        <Feed v-if="showFeed" />
        <FeedSkeleton v-else/>
      </template>
      <template #fallback>
        <FeedSkeleton />
      </template>
    </Suspense>
    <Input />
    <router-view />
</template>

<style scoped>
</style>
