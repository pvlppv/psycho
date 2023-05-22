// App
import { createApp } from 'vue'
import App from '@/App.vue'

// Components
import Header from '@/components/Header.vue';
import Feed from '@/components/Feed.vue';
import Input from '@/components/Input.vue';

// Element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// Router 
import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/Main.vue'

const AboutWindow = () => import('@/components/AboutWindow.vue')
const LangWindow = () => import('@/components/LangWindow.vue')
const Message = async () => import('@/views/Message.vue')

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/', 
            name: 'Main',
            component: Main,
            children: [
                {path: '/about', name: 'About', component: AboutWindow},   
                {path: '/lang', name: 'Lang', component: LangWindow},             
            ],
        },    
        {
            path: '/messages/:message_id', 
            name: 'Message',
            component: Message,
            props: true,
        }
    ]
})

// Virtual Scroll
import VueVirtualScroller from 'vue-virtual-scroller'
import 'vue-virtual-scroller/dist/vue-virtual-scroller.css'

const app = createApp(App);

app.use(ElementPlus);
app.use(router);
app.use(VueVirtualScroller);

app.component('Header', Header);
app.component('Feed', Feed);
app.component('Input', Input);

app.mount('#app');

