<template>
  <!-- 一级 menu 菜单 -->
  <el-menu
    :collapse="!$store.getters.sidebarOpened"
    :default-active="activeMenu"
    :unique-opened="true"
    :background-color="$store.getters.cssVar.menuBg"
    :text-color="$store.getters.cssVar.menuText"
    :active-text-color="$store.getters.cssVar.menuActiveText"
    router
  >
    <sidebar-item 
      v-for="item in routes" 
      :key="item.path" 
      :route="item"
    ></sidebar-item>
  </el-menu>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { filterRouters, generateMenus } from '@/utils/route'
import SidebarItem from './SidebarItem.vue'
// import SidebarItem from './SidebarItem.vue'

const router = useRouter()
console.log(router.getRoutes())
const routes = computed(() => {
  const fRoutes = filterRouters(router.getRoutes())
  return generateMenus(fRoutes)
})
console.log(JSON.stringify(routes.value))

// // 计算高亮 menu 的方法
const route = useRoute()
const activeMenu = computed(() => {
  const { path } = route
  return path
})
</script>
