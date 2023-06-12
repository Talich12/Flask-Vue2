<template>
    <div class="containerMain animate__animated animate__fadeIn" style="animation-duration: 1s;">
      <vs-row justify="space-around">
        <information id="top" style="margin-left: 8%; margin-top: 5vh; z-index: 0;">
          <template #title>
            Рекомендации на сегодня
          </template>
          <template #text>
            Обновления происходят каждые два дня чтобы вы все успели прочесть. Рекомендации строятся на основе ваших предпочтений. Не забывайте ставить оценки историям чтобы улучшить систему рекомендаций.
          </template>
        </information>
        <vs-col v-for="genre in Data" offset="1" w="5">
            <vs-card @click="onClick(genre.id)" style="margin-top: 7%;">
                <template #title>
                    <h3>{{ genre.name }}</h3>
                </template>
                <template #text>
                    <p>{{ genre.description }}</p>
                </template>
                <template #img>
                    <img :src="require(`@/assets/img/load/${genre.image}`)" alt="">
                </template>
            </vs-card>
        </vs-col>
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
    data() {
        return {
          Data: [],
        };
    },
    methods: {
        Get() {
            const path = "http://localhost:3000/genre";
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                this.Data = response.data
            })
                .catch((error) => {
                console.log(error);
            });
        },
        onClick(id){
            this.$router.push('/genretop/' + id)
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