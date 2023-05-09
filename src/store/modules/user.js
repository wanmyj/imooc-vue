import { login, getUserInfo } from '@/api/sys'
import md5 from 'md5'
import { setItem, getItem } from '@/utils/storage'
import { TOKEN } from '@/constant'
import router from '@/router'

export default {
  // true -> 单独模块
  namespaced: true,
  state: () => ({
    token: getItem(TOKEN) || ''
  }),
  mutations: {
    setToken (state, token) {
      state.token = token
      setItem(TOKEN, token)
    }
  },
  actions: {
    /**
     * 登录请求动作
     */
    login (context, userInfo) {
      const { username, password } = userInfo
      return new Promise((resolve, reject) => {
        login({
          username,
          password: md5(password)
        })
          .then((data) => {
            console.log(data.token)
            this.commit('user/setToken', data.token)
            // 登录后操作
            // 跳转
            router.push('/')
            resolve()
          })
          .catch((err) => {
            reject(err)
          })
      })
    }
  }
}
