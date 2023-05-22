import { createStore } from 'vuex'
import user from './modules/user'
import getters from './getters'
import app from './modules/app'

export default createStore({
  getters,
  modules: {
    app,
    user
  }
})
