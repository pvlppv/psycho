const locale = document.documentElement.lang;
const ws = new WebSocket(`ws://thoughty-app.com/${locale}/ws`);

export default ws;
