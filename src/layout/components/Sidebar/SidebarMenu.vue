<template>
  <!-- 一级 menu 菜单 -->
  <el-menu
    :unique-opened="true"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    router
  >
    <!-- 子集 menu -->
    <el-submenu index="1">
      <template #title>
        <i class="el-icon-location"></i>
        <span>导航①</span>
      </template>
      <el-menu-item index="1-1">选项1</el-menu-item>
      <el-menu-item index="1-2">选项2</el-menu-item>
    </el-submenu>
    <!-- 具体菜单 -->
    <el-menu-item index="2">
      <i class="el-icon-location"></i>
      <template #title>
        导航si  
      </template>
    </el-menu-item>
  </el-menu>
</template>

<script setup>
import {} from 'vue'
// import { computed } from 'vue'
// import { useRouter, useRoute } from 'vue-router'
// import { filterRouters, generateMenus } from '@/utils/route'
// import SidebarItem from './SidebarItem.vue'

// const router = useRouter()
// const routes = computed(() => {
//   const filterRoutes = filterRouters(router.getRoutes())
//   return generateMenus(filterRoutes)
// })
// // console.log(JSON.stringify(routes.value))

// // 计算高亮 menu 的方法
// const route = useRoute()
// const activeMenu = computed(() => {
//   const { path } = route
//   return path
// })
</script>
