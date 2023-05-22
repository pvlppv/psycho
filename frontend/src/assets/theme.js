import { ref } from 'vue';

const darkTheme = ref(JSON.parse(localStorage.getItem('darkTheme')));

const root = document.documentElement;
const blackColor = getComputedStyle(root).getPropertyValue("--black-color");
const whiteColor = getComputedStyle(root).getPropertyValue("--white-color");
const blackshadowColor = getComputedStyle(root).getPropertyValue("--shadow-black-color");
const whiteshadowColor = getComputedStyle(root).getPropertyValue("--shadow-white-color");

const setTheme = () => {
  root.style.setProperty("--black-color", darkTheme.value ? blackColor : whiteColor);
  root.style.setProperty("--white-color", darkTheme.value ? whiteColor : blackColor);
  root.style.setProperty("--shadow-black-color", darkTheme.value ? blackshadowColor : whiteshadowColor);
  root.style.setProperty("--shadow-white-color", darkTheme.value ? whiteshadowColor : blackshadowColor);
};

const toggleTheme = () => {
  darkTheme.value = !darkTheme.value;
  setTheme();
  localStorage.setItem("darkTheme", darkTheme.value);
};

setTheme();

export default {
  darkTheme,
  setTheme,
  toggleTheme
};