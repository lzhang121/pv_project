<template>
  <div class="container">
    <div class="user_container">
      <h1>用户管理</h1>
      <UserList />
    </div>
    <div class="solar_container">
      <h1>近7日太阳辐射强度</h1>
      <SolarChart />
    </div>
  </div>
</template>

<script setup>
import UserList from './components/UserList.vue'
import SolarChart from './components/SolarChart.vue'
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
  font-family: sans-serif;
}
</style>
