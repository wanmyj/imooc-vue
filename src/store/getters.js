// import { MAIN_COLOR } from '@/constant'
// import { getItem } from '@/utils/storage'
// import { generateColors } from '@/utils/theme'
import variables from '@/styles/variables.module.scss'
const getters = {
  token: state => state.user.token,
  /**
   * @returns true 表示已存在用户信息
   */
  hasUserInfo: (state) => {
    return JSON.stringify(state.user.userInfo) !== '{}'
  },
  userInfo: (state) => state.user.userInfo, 
  sidebarOpened: (state) => state.app.sidebarOpened,
  language: (state) => state.app.language,
  cssVar: (state) => variables
  //   return {
  //     ...state.theme.variables,
  //     ...generateColors(getItem(MAIN_COLOR))
  //   }
  // },
  // mainColor: (state) => state.theme.mainColor,
  // tagsViewList: (state) => state.app.tagsViewList
}
export default getters
