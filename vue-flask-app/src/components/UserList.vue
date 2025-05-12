<template>
  <div>
    <div v-for="user in users" :key="user.id" class="user-card">
      <strong>{{ user.name }}</strong> — {{ user.email }}
      <!-- 删除按钮，点击时调用 deleteUser 函数 -->
      <button @click="deleteUser(user)">删除</button>
    </div>

    <h2>添加新用户</h2>
    <form @submit.prevent="addUser">
      <input v-model="form.name" placeholder="姓名" required />
      <input v-model="form.email" placeholder="邮箱" required />
      <button type="submit">添加</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const users = ref([])
const form = ref({ name: '', email: '' })

const fetchUsers = async () => {
  const res = await axios.get('/api/users')
  users.value = res.data
}

const addUser = async () => {
  try {
    await axios.post('/api/users', form.value)
    form.value = { name: '', email: '' }
    await fetchUsers()
  } catch (e) {
    alert('添加失败: ' + e.message)
  }
}

// 删除用户函数，根据用户名或邮箱删除
const deleteUser = async (user) => {
  const userInfo = user.name || user.email
  const deleteType = user.name ? 'name' : 'email'
  try {
    await axios.delete(`/api/users?${deleteType}=${userInfo}`)
    alert('用户删除成功')
    await fetchUsers()
  } catch (e) {
    alert('删除失败: ' + e.message)
  }
}

onMounted(fetchUsers)
</script>

<style scoped>
.user-card {
  border-bottom: 1px solid #ddd;
  margin-bottom: 10px;
  padding-bottom: 10px;
}

input {
  margin: 5px;
  padding: 5px;
}

button {
  padding: 6px 12px;
  margin-top: 5px;
  cursor: pointer;
}
</style>
