<template>
  <div class="header-search" @click.stop="onShowClick" :class="{ show: isShow }">
    <svg-icon
      class-name="search-icon"
      icon="search"
    />
    <el-select
      ref="headerSearchSelectRef"
      class="header-search-select"
      v-model="search"
      filterable
      default-first-option
      remote
      placeholder="Search"
      :remote-method="querySearch"
      @change="onSelectChange"
    >
      <el-option
        v-for="option in 5"
        :key="option"
        :label="option"
        :value="option"
      ></el-option>
    </el-select>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { filterRouters, generateMenus } from '@/utils/route'
import { useRouter } from 'vue-router'
import Fuse from 'fuse.js'
// import { generateRoutes } from './FuseData'
// import { watchSwitchLang } from '@/utils/i18n'

// 检索数据源
const router = useRouter()
const searchPool = computed(() => {
  const filterRoutes = filterRouters(router.getRoutes())
  return generateMenus(filterRoutes)
})
console.log(searchPool.value)

/**
 * 搜索库相关
 */
let fuse
const initFuse = (searchPool) => {
  fuse = new Fuse(searchPool, {
    // 是否按优先级进行排序
    shouldSort: true,
    // 匹配长度超过这个值的才会被认为是匹配的
    minMatchCharLength: 1,
    // 将被搜索的键列表。 这支持嵌套路径、加权搜索、在字符串和对象数组中搜索。
    // name：搜索的键
    // weight：对应的权重
    keys: [
      {
        name: 'title',
        weight: 0.7
      },
      {
        name: 'path',
        weight: 0.3
      }
    ]
  })
}
console.log(fuse)

initFuse(searchPool.value)
// 控制 search 显示
const isShow = ref(false)
// el-select 实例
const onShowClick = () => {
  console.info("onShowClick")
  isShow.value = !isShow.value
}
  // headerSearchSelectRef.value.focus()
// const headerSearchSelectRef = ref(null)

/**
 * 关闭 search 的处理事件
 */
// const onClose = () => {
//   headerSearchSelectRef.value.blur()
//   isShow.value = false
//   searchOptions.value = []
// }
/**
 * 监听 search 打开，处理 close 事件
 */
// watch(isShow, (val) => {
//   if (val) {
//     document.body.addEventListener('click', onClose)
//   } else {
//     document.body.removeEventListener('click', onClose)
//   }
// })

// search 相关
const search = ref('')
// 搜索方法
const querySearch = () => {
  console.log('querySearch')
}
// 搜索结果
// const searchOptions = ref([])
// 搜索方法
// const querySearch = (query) => {
//   if (query !== '') {
//     searchOptions.value = fuse.search(query)
//   } else {
//     searchOptions.value = []
//   }
// }
// 选中回调
const onSelectChange = () => {
  console.log('onSelectChange')
  // router.push(val.path)
}

// 处理国际化
// watchSwitchLang(() => {
//   searchPool = computed(() => {
//     const filterRoutes = filterRouters(router.getRoutes())
//     return generateRoutes(filterRoutes)
//   })
//   initFuse(searchPool.value)
// })
</script>

<style lang="scss" scoped>
.header-search {
  font-size: 0 !important;
  ::v-deep .search-icon {
    cursor: pointer;
    font-size: 18px;
    vertical-align: middle;
  }
  .header-search-select {
    font-size: 18px;
    transition: width 0.2s;
    width: 0;
    overflow: hidden;
    background: transparent;
    border-radius: 0;
    display: inline-block;
    vertical-align: middle;

    :deep .el-input__inner {
      border-radius: 0;
      border: 0;
      padding-left: 0;
      padding-right: 0;
      box-shadow: none !important;
      border-bottom: 1px solid #d9d9d9;
      vertical-align: middle;
    }
  }
  &.show {
    .header-search-select {
      width: 210px;
      margin-left: 10px;
    }
  }
}
</style>
