<script setup>
</script>

<template>
    <div class="main-about">
        <h1 class="main-about-h1">О приложении</h1>
        <!-- <p class="main-about-p"><b>Thoughty App</b> - это площадка, где каждый может поделиться чем-то сокровенным, излить душу, получить фидбек.</p> -->
        <div class="main-about-features">
            <div class="main-about-features-one">
                <div class="main-about-features-one-h1">
                    <i class='main-about-features-one-h1-icon bx bx-mask'></i>
                    <h1 class="main-about-features-one-h1-h1">Полная анонимность</h1>
                </div>
                <p class="main-about-features-one-p">Никакой регистрации и сбора личных данных</p>
            </div>
            <div class="main-about-features-one">
                <div class="main-about-features-one-h1">
                    <i class='main-about-features-one-h1-icon bx bx-world'></i>
                    <h1 class="main-about-features-one-h1-h1">Языковые лобби</h1>
                </div>
                <p class="main-about-features-one-p">Приложение предназначено для всех языков. По мере развития приложения будут добавляться и другие языковые лобби</p>
            </div>
            <div class="main-about-features-one">
                <div class="main-about-features-one-h1">
                    <i class='main-about-features-one-h1-icon bx bx-chat'></i>
                    <h1 class="main-about-features-one-h1-h1">Фидбек</h1>
                </div>
                <p class="main-about-features-one-p">Ответы на ваши сообщения</p>
            </div>
        </div>
        <div class="main-about-buttons">
            <a href="https://telegram.org" target="_blank"><button class="main-about-buttons-contact">Написать нам</button></a>
            <a href="https://pay.cloudtips.ru/p/c0aa205a" target="_blank"><button class="main-about-buttons-support">Поддержать проект</button></a>    
        </div>
        <div class="main-about-footer">
            <div class="main-about-footer-socials">
                <a href="https://telegram.org" class="main-about-footer-socials-a" target="_blank"><i class='main-about-footer-socials-a-i bx bxl-telegram'></i></a>
            </div>
            <div class="main-about-footer-politics">
                <a class="main-about-footer-politics-one" href="" target="_blank">Условия</a>
                <a class="main-about-footer-politics-one" href="" target="_blank">Конфидециальность</a>
            </div>  
            <p class="main-about-footer-copyright">&copy; 2023 Thoughty App - All Rights Reserved.</p>  
        </div>
    </div>
</template>

<style scoped>
.main-about {
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
    text-align: center;
    gap: 4rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
    padding: 2rem 10rem;
    z-index: 1;
    top: 12.6rem;
}
.main-about-h1 {
    font-size: 1.5rem;
    color: var(--white-color);
}
.main-about-p {
    color: var(--white-color);
}
.main-about-features {
    color: var(--white-color);
    display: flex;
    flex-direction: column;
    gap: 2rem;
}
.main-about-features-one {
    display: grid;
    grid-template-columns: repeat(2, 13rem);
    gap: 2rem;
    align-items: center;
}
.main-about-features-one-h1 {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}
.main-about-features-one-h1-icon {
    font-size: 2.5rem;
}
.main-about-features-one-h1-h1 {
    font-size: 1rem;
    text-align: start;
}
.main-about-features-one-p {
    font-size: 0.8rem;
    text-align: start;
}
.main-about-buttons {
    display: flex;
    gap: 2rem;
}
.main-about-buttons-contact,
.main-about-buttons-support {
    border: 1px solid var(--white-color);
    border-radius: 5px;
    background: var(--black-color);
    color: var(--white-color);
    width: 10rem;
    padding: 1rem;
    cursor: pointer;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
.main-about-footer-socials {
    display: flex;
    gap: 1.5rem;
}
.main-about-footer-socials-a-i {
    color: var(--white-color);
    font-size: 1.5rem;
}
.main-about-footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}
.main-about-footer-politics {
    display: flex;
    gap: 0.5rem;
}
.main-about-footer-politics-one {
    color: var(--white-color);
    text-decoration: underline;
    font-size: 0.8rem;
}
.main-about-footer-copyright {
    color: var(--white-color);
    font-size: 0.8rem;
}
</style>