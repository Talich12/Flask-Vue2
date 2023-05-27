
<template>
    <div class="center">
      <vs-table>
        <template #header>
          <vs-input v-model="search" border placeholder="Search" />
        </template>
        <template #thead>
          <vs-tr>
            <vs-th sort @click="users = $vs.sortData($event ,users, 'username')">
              Name
            </vs-th>
            <vs-th sort @click="users = $vs.sortData($event ,users, 'email')">
              Email
            </vs-th>
            <vs-th sort @click="users = $vs.sortData($event ,users, 'id')">
              Id
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
              <vs-td> 
                  <vs-avatar size="35"><img @click="onRoute()" :src="require(`@/assets/img/load/${tr.avatar}`)" alt="" style="transform: 0;"></vs-avatar> {{ tr.username }}
              </vs-td>
            </router-link>
            <vs-td>
            {{ tr.email }}
            </vs-td>
            <vs-td>
            {{ tr.id }}
            </vs-td>
          </vs-tr>
        </template>
      </vs-table>
    </div>
  </template>
<script>
    export default {
      props :['users'],
      data:() => ({
        Route: this.$route,
        ProfileUrl: '/profile/',
        search: '',
      }),
      methods: {
        onRoute(){
        console.log("vadfasd")
      }
      }
    }
    </script>

    <style>
        .vs-table__tr:hover .vs-table__td {
            background:#30303A;
            color:#6A4E93;
        }
        .vs-table__tr .vs-table__td {
            color:#EEEFF9; 
        }
        .vs-table__header {
            color: #EEEFF9;
            background: #30303A;
        }
        .vs-input-parent--border .vs-input-content .vs-input {
            color: #EEEFF9;
        }
        .vs-table_not-found tr td {
            color:#6A4E93;
        }
        .vs-table table {
            background: #30303A;
        }
        .vs-avatar {
            background: #30303A;
        }
        .vs-table__header ~ .vs-table .vs-table__th:first-child, .vs-table__thead .vs-table__th {
            background: #6A4E93;
        }
        .vs-table__header ~ .vs-table .vs-table__th:first-child, .vs-table__thead .vs-table__th {
            color: #EEEFF9;
        }
        .vs-table__th.sort:hover {
            background: #30303A;
            color: #EEEFF9;
        }
        .vs-table__th.sort:hover:first-child {
            background: #30303A;
            color: #EEEFF9;
        }
        .vs-icon-arrow::after {
            background: #EEEFF9;
        }
        .vs-icon-arrow::before {
            background: #EEEFF9;
        }
    </style>