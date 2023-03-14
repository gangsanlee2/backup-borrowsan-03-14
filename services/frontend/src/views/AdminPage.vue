<template>
  <div class="adminPage">
    <h3>adminID 님, 안녕하세요.</h3>
    <table>
      <tbody>
        <tr>
          <NavAdminVue/>
          <td>
            <router-view/>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import NavAdminVue from '@/components/common/NavAdmin.vue'

  export default {
    name: 'loginPage',
    components: {
      NavAdminVue
    }
  }
</script>


<style>
.adminPage {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
  font-family: Arial, sans-serif;
}

h3 {
  font-size: 24px;
  margin-bottom: 20px;
}

table {
  border-collapse: collapse;
  width: 100%;
  max-width: 800px;
  background-color: #f5f5f5;
}

td {
  padding: 20px;
}

tr {
  border-bottom: 1px solid #ddd;
}

tr:last-child {
  border-bottom: none;
}

.NavAdminVue {
  background-color: #333;
  color: white;
  padding: 10px;
}

.NavAdminVue a {
  color: white;
  text-decoration: none;
  margin-right: 10px;
}

.NavAdminVue a:hover {
  text-decoration: underline;
}
</style>