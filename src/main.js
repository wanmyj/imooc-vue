import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import i18n from './i18n'
import installElementPlus from './plugins/element'

// import scss
import './styles/index.scss'
// 导入 svgIcon
import installIcons from '@/icons'
// 
import './permission'

const app = createApp(App)
installElementPlus(app)
installIcons(app)
app
  .use(store)
  .use(router)
  .use(i18n)
  .mount('#app')
