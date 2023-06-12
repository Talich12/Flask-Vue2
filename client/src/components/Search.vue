<template>
    <div class="containerMain animate__animated animate__fadeIn" style="animation-duration: 1s;">
      <vs-row justify="space-around">
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center; margin-left: 7%; margin-top: 2vh;">
        <vs-input type="text" v-model="search" placeholder="Поиск по названию..." style="display: block;"/>
        <vs-button @click="Search()" relief danger style="width: 7vw; margin-top: 2vh;">
            Найти
        </vs-button>
        </div>
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
        <pagination :len="len" :page="page" @value="onValue" @page="onPage" style="margin-left: 9%;"></pagination>
      </vs-row>
      <div class="footer">
        <!-- Ваш код футера -->
      </div>
      <vue-particles
          color="#EEEFF9"
          :particleOpacity="0.7"
          :particlesNumber="80"
          shapeType="circle"
          :particleSize="4"
          linesColor="#EEEFF9"
          :linesWidth="1.2"
          :lineLinked="true"
          :lineOpacity="0.5"
          :linesDistance="140"
          :moveSpeed="2"
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
    data() {
        return {
            Data: [],
            len: 1,
            page: 1,
            value: 4,
            search: '',
        };
    },
    methods: {
        Get() {
            const path = "http://localhost:3000/search";
            axios.post(path, {search: this.search, page: this.page, value: this.value})
                .then((response) => {
                console.log(response.data);
                this.Data = response.data.data;
                this.len = response.data.len
            })
                .catch((error) => {
                console.log(error);
            });
        },
        openLoading() {
          const loading = this.$vs.loading({
            background: 'dark',
            color: 'danger',
            type: 'rectangle'
          });
          setTimeout(() => {
            loading.close();
          }, 800);
        },
        onPage(data){
          this.page = data.page
          const path = "http://localhost:3000/search";
            axios.post(path, {search: this.search, page: data.page, value: this.value})
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
          const path = "http://localhost:3000/search";
            axios.post(path, {search: this.search, value: data.value, page: this.page})
                .then((response) => {
                console.log(response.data);
                this.Data = response.data.data;
                this.len = response.data.len
            })
                .catch((error) => {
                console.log(error);
            });
        },
        Search(){
            this.openLoading();
            const path = "http://localhost:3000/search";
            axios.post(path, {search: this.search, value: this.value, page: this.page})
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