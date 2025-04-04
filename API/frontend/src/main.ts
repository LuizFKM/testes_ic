

import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import { createPinia } from 'pinia'
const app = createApp(App)

const pinia = createPinia()
app.use(pinia);
app.mount('#app')
