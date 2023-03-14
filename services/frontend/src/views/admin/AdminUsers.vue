<template>
  <div class="admin_user_list">
    <h1>회원 조회</h1>
      <table v-for="user in users" :key="user.name">
        <tr>
          <th>아이디</th>
          <th>이름</th>
          <th>가입일</th>
          <th>수정일</th>
        </tr>
        <tr>
          <td>{{ user.admin_id }}</td>
          <td>{{ user.name }}</td>
          <td>{{ user.created_at }}</td>
          <td>{{ user.updated_at }}</td>
        </tr>
      </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      users: []
    }
  },
  mounted() {
    this.getUsers()
  },
  methods: {
    getUsers() {
      axios.get('http://localhost:8000/admins/show')
        .then(response => {
          this.users = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
</style>
