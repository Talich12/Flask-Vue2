
<template>
    <div class="center">
      <vs-table class="custom-table">
        <template #header>
          <vs-input v-model="search" border placeholder="Search" />
        </template>
        <template #thead>
          <vs-tr>
            <vs-th sort @click="users = $vs.sortData($event ,users, 'username')">
              Name
            </vs-th>
          </vs-tr>
        </template>
        <template #tbody>
          <vs-tr
            :key="i"
            v-for="(tr, i) in $vs.getSearch(users, search)"
            :data="tr"
          >
            <router-link :to="ProfileUrl+tr.username">
              <vs-td style="width: 100%;"> 
                <div style="display: flex; flex-direction: row; align-items: center;">
                  <vs-avatar size="35"><img :src="require(`@/assets/img/load/${tr.avatar}`)" alt="" style="transform: 0;"></vs-avatar> <p style="margin-left: 1vw; font-size: 2vh;">{{ tr.username }}</p>
                </div>
                </vs-td>
            </router-link>
          </vs-tr>
        </template>
      </vs-table>
    </div>
  </template>
<script>
    export default {
      props :['users'],
      data:() => ({
        route: "url",
        ProfileUrl: '/profile/',
        search: '',
      }),
    }
    </script>

<style scoped>
.custom-table .vs-table__tr:hover .vs-table__td {
  background: #30303A;
  color: #6A4E93;
}

.custom-table .vs-table__tr .vs-table__td {
  color: #EEEFF9;
}

.custom-table .vs-table__header {
  color: #EEEFF9;
  background: #30303A;
}
.custom-table .vs-table__tr:hover .vs-table__td {
  background: #2A2A35;
  transform: scale(0.95);
}

.custom-table .vs-input-parent--border .vs-input-content .vs-input {
  color: #EEEFF9;
}
.custom-table .vs-table__header {
  background: #30303A;
}

.custom-table .vs-table_not-found tr td {
  color: #6A4E93;
}
.custom-table .vs-table table {
  background: #30303A;
}

.custom-table .vs-avatar {
  background: #30303A;
}

.custom-table .vs-table__header ~ .vs-table .vs-table__th:first-child,
.custom-table .vs-table__thead .vs-table__th {
  background: #6A4E93;
  color: #EEEFF9;
}

.custom-table .vs-table__th.sort:hover,
.custom-table .vs-table__th.sort:hover:first-child {
  background: #30303A;
  color: #EEEFF9;
}

.custom-table .vs-icon-arrow::after,
.custom-table .vs-icon-arrow::before {
  background: #EEEFF9;
}
</style>