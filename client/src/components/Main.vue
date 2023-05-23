<template>
    <div class="containerMain animate__animated animate__fadeIn" style="animation-duration: 1s;">
      <vs-row justify="space-around">
        <information style="margin-left: 8%; margin-top: 5vh; z-index: 0;">
          <template #title>
            Подборка самых популярных историй на сегодня
          </template>
          <template #text>
            Описание подобрки
          </template>
        </information>
        <cookie></cookie>
        <totop></totop>
        <vs-col v-for="post in Data" offset="1" w="5">
          <card>
            <template #title>
              {{ post.title }}
            </template>
            <template #text>
              {{ post.body }}
            </template>
            <template #img>
              <img :src="require(`@/assets/img/load/${post.img}`)" alt="">
            </template>
          </card>
        </vs-col>
        <information style="margin-left: 8%; margin-top: 5vh; z-index: 0;">
          <template #title>
            Рекомендации на сегодня
          </template>
          <template #text>
            Обновления происходят каждые два дня чтобы вы все успели прочесть. Рекомендации строятся на основе ваших предпочтений. Не забывайте ставить оценки историям чтобы улучшить систему рекомендаций.
          </template>
        </information>
        <cardrecs></cardrecs>
        <pagination style="margin-left: 9%;"></pagination>
      </vs-row>
      <div class="footer">
        <!-- Ваш код футера -->
      </div>
      <vue-particles
        color="#EEEFF9"
        :particleOpacity="0.7"
        :particlesNumber="110"
        shapeType="circle"
        :particleSize="4"
        linesColor="#EEEFF9"
        :linesWidth="1.2"
        :lineLinked="true"
        :lineOpacity="0.5"
        :linesDistance="140"
        :moveSpeed="2"
        :hoverEffect="false"
        hoverMode=""
        :clickEffect="false"
        clickMode=""
        style="position:absolute; z-index: -10; height: 80%; width: 100vw; left: 0%; top: 8%;"
      > </vue-particles>
    </div>
  </template>
  
  
<script>
import axios from 'axios';
import Information from './Information.vue';

export default {
    name: "index",
    data() {
        return {
            Data: []
        };
    },
    methods: {
        Get() {
            const path = "http://localhost:3000/";
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                const data = response.data;
                this.Data = data;
            })
                .catch((error) => {
                console.log(error);
            });
        },
    },
    created() {
        this.Get();
    },
    components: { Information }
};
</script>

<style>
.containerMain {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Высота экрана, чтобы футер всегда был внизу */
  padding-left: 16%;
  padding-right: 7%;
  padding-top: 12vh;
}

.footer {
  padding-top: 0; /* Расположение футера внизу контейнера */
}
</style>