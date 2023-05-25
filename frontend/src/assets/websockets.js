const locale = document.documentElement.lang;
const ws = new WebSocket(`ws://localhost:8000/${locale}/ws`);

export default ws;
