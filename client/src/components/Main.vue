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
      <vs-col v-for="post in Data" offset="1" w="5">
        <card>
          <template #title>
            {{ post.title }}
          </template>
          <template #text>
            {{ post.author.username }}
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
      <pagination :len="len" :page="page" @value="onValue" @page="onPage" style="margin-left: 9%;"></pagination>
    </vs-row>
    <div class="footer">
      <!-- Ваш код футера -->
    </div>
    <vue-particles
        color="#EEEFF9"
        :particleOpacity="0.4"
        :particlesNumber="50"
        shapeType="circle"
        :particleSize="4"
        linesColor="#EEEFF9"
        :linesWidth="1.2"
        :lineLinked="true"
        :lineOpacity="0.5"
        :linesDistance="180"
        :moveSpeed="1.5"
        :hoverEffect="false"
        hoverMode="grab"
        :clickEffect="false"
        clickMode="push"
        style="position:absolute; z-index: -10; height: 100%; width: 100vw; left: 0%; top: 8%;"
      > </vue-particles>
  </div>
</template>


<script>
import axios from 'axios';
import Information from './Information.vue';

export default {
  name: "index",
  props:['video', 'audio'],
  data() {
      return {
          Data: [],
          len: 1,
          page: 1,
          value: 4,
          UserIcon: require(`@/assets/img/load/sample1.jpg`),
      };
  },
  methods: {
      Get() {
          const path = "http://localhost:3000/";
          axios.post(path, {page: this.page, value: this.value, video: this.$props.video, audio: this.$props.audio})
              .then((response) => {
              console.log(response.data);
              this.Data = response.data.data;
              this.len = response.data.len
          })
              .catch((error) => {
              console.log(error);
          });
      },
      onPage(data){
        this.page = data.page
        const path = "http://localhost:3000/";
          axios.post(path, {page: data.page, value: this.value, video: this.$props.video, audio: this.$props.audio})
              .then((response) => {
              console.log(response.data);
              this.Data = response.data.data;
          })
              .catch((error) => {
              console.log(error);
          });
      },
      onValue(data){
        this.value = data.value
        this.page = 1
        const path = "http://localhost:3000/";
          axios.post(path, {value: data.value, page: this.page, video: this.$props.video, audio: this.$props.audio})
              .then((response) => {
              console.log(response.data);
              this.Data = response.data.data;
              this.len = response.data.len
          })
              .catch((error) => {
              console.log(error);
          });
      }
  },
  watch:{
    video: function(){
      this.page = 1
      this.Get()
    },
    audio: function(){
      this.page = 1
      this.Get()
    }
  },
  created() {
      this.Get();
      console.log(this.$props.audio)
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
.vs-card__group .vs-card__group-prev .vs-icon-arrow::after {
  background: rgb(238, 239, 249);
}
.vs-card__group .vs-card__group-prev .vs-icon-arrow::before {
  background: rgb(238, 239, 249);
}
.vs-card__group .vs-card__group-next .vs-icon-arrow::before {
  background: rgb(238, 239, 249);
}
.vs-card__group .vs-card__group-next .vs-icon-arrow::after {
  background: rgb(238, 239, 249);
}
</style>