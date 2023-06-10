<template>
  <el-dropdown
    trigger="click"
    class="international"
    @command="handleSetLanguage"
  >
    <div>
      <el-tooltip content="国际化" :effect="effect">
        <svg-icon icon="language" />
      </el-tooltip>
    </div>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item :disabled="language === 'zh'" command="zh">
          中文
        </el-dropdown-item>
        <el-dropdown-item :disabled="language === 'en'" command="en">
          English
        </el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script setup>
// Must be called at the top of a `setup` function；导入i18n报错
// import { useI18n } from 'vue-i18n';
// const { t } = useI18n();
// 改成
// import i18n from '@/i18n';
// const { t } = i18n.global;

import i18n from '@/i18n'
// import { useI18n } from 'vue-i18n'
import { computed, defineProps } from 'vue'
import { useStore } from 'vuex'
import { ElMessage } from 'element-plus'

defineProps({
  effect: {
    type: String,
    default: 'dark',
    validator: function (value) {
      // 这个值必须匹配下列字符串中的一个
      return ['dark', 'light'].indexOf(value) !== -1
    }
  }
})

const store = useStore()
const language = computed(() => store.getters.language)

// const { locale } = useI18n()
const { locale } = i18n.global

// 切换语言的方法
const handleSetLanguage = (lang) => {
  // 切换i18n的locale
  locale.value = lang
  // i18n.global.locale.value = lang
  // console.log(t)
  // 修改vuex保存的language
  store.commit('app/setLanguage', lang)
  // 提示
  ElMessage.success("更新成功")
}
</script>
