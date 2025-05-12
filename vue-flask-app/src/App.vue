<template>
  <div class="container">
    <h1>用户管理</h1>
    <UserList />
  </div>
</template>

<script setup>
import UserList from './components/UserList.vue'
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
  font-family: sans-serif;
}
</style>
