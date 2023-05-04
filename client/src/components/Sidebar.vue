<template>
  <div class="hidden" style="position: sticky; top: 0px;">
    <vs-sidebar
      background="dark"
      text-white
      absolute
      v-model="active"
      open
      square
      style="width: 16%; max-width: 100%; height: 100vh;"
      >
      <template #logo>
        <!-- ...img logo -->
      </template>
      <vs-sidebar-item to ="main">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        <p style="font-size: 20px;">Главная страница</p>
      </vs-sidebar-item>
      <vs-sidebar-item id="search">
        <template #icon>
          <i class='bx bx-search'></i>
        </template>
        <p style="font-size: 20px;">Поиск</p>
      </vs-sidebar-item>
      <vs-sidebar-item id="recommendations">
        <template #icon>
          <i class='bx bx-merge'></i>
        </template>
        <p style="font-size: 20px;">Рекомендации</p>
      </vs-sidebar-item>
      
      <vs-sidebar-item id="help">
        <template #icon>
          <i class='bx bx-help-circle'></i>
        </template>
        <p style="font-size: 20px;">О нас</p>
      </vs-sidebar-item>
      
      <template #footer>
        <vs-row justify="space-between">
          <vs-avatar>
            <img src="../assets/sample1.jpg" alt="">
          </vs-avatar>

          <vs-avatar color="primary" badge-color="danger" badge-position="top-right">
            <i class='bx bx-bell' style='color:white'></i>

            <template #badge>
              <span style='color:white;'>28</span>
            </template>
          </vs-avatar>
        </vs-row>
      </template>
    </vs-sidebar>
  </div>
</template>
<script>
  export default {
    data:() => ({
      active: 'home',
    })
  }
</script>