<template>
  <div>
    <div class="app-main">
      <router-view></router-view>
    </div>
  </div>
</template>
<script setup>  
import {} from 'vue'
</script>

<style lang="scss" scoped>
.app-main {
  min-height: calc(100vh - 50px - 43px);
  width: 100%;
  position: relative;
  overflow: hidden;
  padding: 104px 20px 20px 20px;
  box-sizing: border-box;
}
</style>
