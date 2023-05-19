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
      <vs-sidebar-item id="main" to="main">
        <template #icon>
          <i class='bx bxs-home' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size:1vw; font-family: 'Unbounded'; font-weight: bolder;">Главная страница</p>
      </vs-sidebar-item>
      <vs-sidebar-item id="search">
        <template #icon>
          <i class='bx bxs-search' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">Поиск</p>
      </vs-sidebar-item>
      <vs-sidebar-item id="recommendations">
        <template #icon>
          <i class='bx bx-merge' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">Рекомендации</p>
      </vs-sidebar-item>

      <vs-sidebar-item id="audio">
        <template #icon>
          <i class='bx bxs-microphone-alt' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">Истории с аудио</p>
      </vs-sidebar-item>
      <vs-sidebar-group>
        <template #header>
          <vs-sidebar-item arrow style="margin-right: 7%;">
            <template #icon>
              <i class='bx bxs-plus-circle'></i>
            </template>
            Подписки
          </vs-sidebar-item>
        </template>

        <vs-sidebar-item id="authors">
        <template #icon>
          <i class='bx bxs-user' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">Авторы</p>
      </vs-sidebar-item>
      <vs-tooltip right danger>
      <vs-sidebar-item id="genresubs">
        <template #icon>
          <i class='bx bxs-book-heart' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">Жанры</p>
      </vs-sidebar-item>
      <template #tooltip>
          Кнопка быстрого доступа к вашим любимым жанрам!
        </template>
      </vs-tooltip>
      </vs-sidebar-group>

      <vs-sidebar-group>
        <template #header>
          <vs-sidebar-item arrow style="margin-right: 7%;">
            <template #icon>
              <i class='bx bxs-spreadsheet'></i>
            </template>
            Подборки
          </vs-sidebar-item>
        </template>

        <vs-sidebar-item id="genre">
        <template #icon>
          <i class='bx bxs-book' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">По жанрам</p>
      </vs-sidebar-item>

      <vs-sidebar-item id="winners">
        <template #icon>
          <i class='bx bxs-trophy' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">Победители</p>
      </vs-sidebar-item>
      
      <vs-tooltip right danger>
      <vs-sidebar-item id="admin">
        <template #icon>
          <i class='bx bxs-quote-right' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">От редакции</p>
      </vs-sidebar-item>
      <template #tooltip>
          Истории отобранные администрацией
        </template>
      </vs-tooltip>

      <vs-sidebar-item id="likes">
        <template #icon>
          <i class='bx bxs-like' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">По лайкам</p>
      </vs-sidebar-item>

      </vs-sidebar-group>

      <vs-sidebar-item id="bookmarks">
        <template #icon>
          <i class='bx bxs-bookmark' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">Закладки</p>
      </vs-sidebar-item>
      
      <vs-sidebar-item to="about" id="help">
        <template #icon>
          <i class='bx bxs-help-circle' style="font-size: 1vw;"></i>
        </template>
        <p style="font-size: 1vw; font-family: 'Unbounded'; font-weight: bolder;">О нас</p>
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
  data: () => ({
    active: '',
  }),
};
</script>
