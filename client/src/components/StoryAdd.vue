<template>
  <div class="containerInfo animate__animated animate__fadeIn" style="animation-duration: 1s;">
  <div class="container" style=" margin-left: 16%; margin-right: 7%;">
    <vs-col offset="1" style="margin-top: 11%;">
      <mdeditor @body="onBody" style="margin-right: 0%;"/>
      <vs-row>
        <vs-select
        label="Жанры"
        multiple
        placeholder="Filter"
        v-model="value"
      >
        <vs-option v-for="genre in Data" :label="genre.name" :value="genre.name">
          {{genre.name}}
        </vs-option>
      </vs-select>
      </vs-row>

      <vs-row>
        <vs-input
          label="title"
          v-model="title"
          placeholder="title"
        />
      </vs-row>
      
      
      <vs-row>
        <vs-input type="file" @change="OnFileSelected" />
        <button @click="onUpload">UpLoad</button>
      </vs-row>
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