<script setup>
</script>

<template>
    <div class="main-lang">
        <h1 class="main-lang-h1">Язык</h1>
        <div class="main-lang-div">
            <img class="main-lang-div-one" src="@/assets/en.png" alt="">
            <img class="main-lang-div-one" src="@/assets/ru.png" alt="">
        </div>
    </div>
</template>

<style scoped>
.main-lang {
    position: absolute;
    background: var(--black-color);
    width: 60rem;
    height: 30rem;
    overflow: auto;
    border: 1px solid var(--white-color);
    border-radius: 0.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    padding: 2rem 2rem;
    z-index: 1;
    top: 12.6rem;
}
.main-lang-h1 {
    color: var(--white-color);
}
.main-lang-div {
    display: flex;
    gap: 2rem;
}
.main-lang-div-one {
    width: 3rem;
    border: 1px solid var(--white-color);
    border-radius: 0.375rem;
    cursor: pointer;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
</style>