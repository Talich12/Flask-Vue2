<template>
  <div class="containerInfo animate__animated animate__fadeIn" style="animation-duration: 1s;">
  <div class="container" style=" margin-left: 16%; margin-right: 7%;">
    <vs-col offset="1" style="margin-top: 11%;">
      <div style="display: flex; justify-content: center; margin-bottom: 2vh; opacity: 0.8;">
          <vs-checkbox danger >
            <p style="color: #EEEFF9; font-size: 1vw;">Нецензурная лексика</p>
          <template #icon>
            <i class='bx bx-angry'></i>
          </template>
        </vs-checkbox>
        <vs-checkbox danger style="margin-left: 2vw;">
            <p style="color: #EEEFF9; font-size: 1vw;">Кровь/Насилие</p>
          <template #icon>
            <i class='bx bx-knife'></i>
          </template>
        </vs-checkbox>
      </div>
      <div style="display: flex; justify-content: center; margin-bottom: 2vh;">
      <vs-input color="#FF0000" state="success" type="video" v-model="video" label-placeholder="youtube" style="margin-right: 5px;">
        <template #icon>
          <i class='bx bxl-youtube' ></i>
        </template>
      </vs-input>
      <vs-input danger type="audio" state="success" v-model="audio" label-placeholder="audioboom">
        <template #icon>
          <i class='bx bxs-microphone-alt' ></i>
        </template>
      </vs-input>
      <vs-button
      flat
        style="min-width: 200px"
        success
        animation-type="scale"
      >
        <i class='bx bxl-markdown'></i>
        <template #animate >
          Markdown подсказка
        </template>
      </vs-button>
      </div>
      <div style="display: flex; justify-content: center; margin-bottom: 2vh;">
      <vs-select
        class="genrestory"
        label="Жанры"
        filter
        state="danger"
        multiple
        placeholder="Выберите"
        collapse-chips
        v-model="value"
        style="margin-right: 5px; margin-top: 2.3px; height: 34px;"
      >
        <vs-option v-for="genre in Data" :label="genre.name" :value="genre.name">
          {{genre.name}}
        </vs-option>
      </vs-select>
      <vs-input
          state="danger"
          label="Название"
          v-model="title"
          placeholder="В чёрном чёрном..."
          style="margin-right: 5px;"
        />
        <vs-input label="Обложка истории" id="inputstoryimg" state="danger" type="file" @change="OnFileSelected"/>
        <vs-button border danger @click="onUpload" style="height: 33.2px;">Загрузить</vs-button>
      </div>
      <mdeditor @body="onBody" style="margin-right: 0%;"/>
    </vs-col>
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
        style="position:absolute; z-index: -1; height: 100%; width: 100vw; left: 0%; top: 8%;"
      > </vue-particles>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import mdeditor from './MarkdownEditor.vue';

export default {
  components: {
    mdeditor
  },
  data() {
    return {
      video: '',
      audio: '',
      title: '',
      body: '',
      value: [],
      file: null,
      Data: []
    }
  },
  methods: {
    OnFileSelected(event) {
      this.file = event.target.files[0]
      console.log(event)
    },
    onUpload() {
      const fd = new FormData();
      fd.append('genre', this.value)
      fd.append('file', this.file)
      fd.append('title', this.title)
      fd.append('body', this.body)
      fd.append('audio', this.audio)
      fd.append('video', this.video)
      console.log(fd)
      axios.post('http://localhost:3000/storyadd', fd,{
          headers: {
              'Authorization': 'Bearer ' + this.$cookies.get("access_token"),
          }
      })
        .then((response) => {
          console.log(this.value)
          console.log(response)
          this.$router.push({ name: 'Main' })
        })
    },
    onBody(data){
      this.body = data.body
      console.log(this.body)
    },
    GetGenre() {
      const path = "http://localhost:3000/genre";
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
  watch:{
    value: function(){
      console.log(this.value)
    }
  },
  created() {
    this.GetGenre();
  },
}
</script>

<style>
  .vs-select__chips__input::placeholder {
    color: rgb(106, 78, 147);
    font-family: 'Unbounded';
  }
</style>