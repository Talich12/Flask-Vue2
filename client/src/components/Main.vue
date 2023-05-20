<template>
    <div class="containerMain">
      <vs-row justify="space-around">
        <information style="margin-left: 8%; margin-top: 5vh; z-index: 0;">
          <template #title>
            Рекомендации на сегодня
          </template>
          <template #text>
            Обновления происходят каждые два дня чтобы вы все успели прочесть. Рекомендации строятся на основе ваших предпочтений. Не забывайте ставить оценки историям чтобы улучшить систему рекомендаций.
          </template>
        </information>
        <cookie></cookie>
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
        <Information style="margin-left: 8%; margin-top: 5vh; z-index: 0;">
          <template #title>
            Рекомендации на сегодня
          </template>
          <template #text>
            Обновления происходят каждые два дня чтобы вы все успели прочесть. Рекомендации строятся на основе ваших предпочтений. Не забывайте ставить оценки историям чтобы улучшить систему рекомендаций.
          </template>
        </Information>
        <pagination style="margin-left: 8%;"></pagination>
      </vs-row>
      <div class="footer">
        <!-- Ваш код футера -->
      </div>
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
  margin-left: 16%;
  margin-right: 7%;
  margin-top: 12vh;
}

.footer {
  margin-top: auto; /* Расположение футера внизу контейнера */
}
</style>
