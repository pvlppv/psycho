<script setup>
</script>

<template>
  <main>
    <section class="main">
        <router-view />
    </section>
  </main>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');
:root {
    --app-height: 100%;

    --black-color: #000000;
    --white-color: #ffffff;
    --shadow-white-color: rgba(255, 255, 255, 0.15);
    --shadow-black-color: rgba(0, 0, 0, 0.15);

    --fw-regular: 400;
    --fw-medium: 500;
    --fw-semi-bold: 600;
    --fw-bold: 700;
    --fw-extra-bold: 800;
}
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
::selection {
    color: var(--black-color);
    background: var(--white-color);
}
::-moz-selection { /* for Firefox */
    color: var(--black-color);
    background: var(--white-color);
}
html {
    scroll-behavior: smooth;
}
body {
    font-family: "Montserrat", sans-serif;
}
main {
    position: relative;
    overflow: hidden;
}
ul {
    list-style: none;
}
a {
    text-decoration: none;
}
img {
    max-width: 100%;
    height: auto;
}
body {
    background: var(--black-color);
}
section {
    width: 100vw;
    height: 100vh;
    /* height: var(--app-height); */
}
.main {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
}
</style>
