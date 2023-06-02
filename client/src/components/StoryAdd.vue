<template>
  <div class="container" style="display: flex; margin-left: 16%; margin-right: 7%;">
    <vs-col offset="1" style="margin-top: 11%;">
      <mdeditor/>
      <vs-row>
        <vs-select placeholder="Select" v-model="value">
          <vs-option v-for="(name, id) in Data" :label="name" :value="id">
            {{ name.name }}
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
        <vs-input
          label="body"
          v-model="body"
          placeholder="body"
        />
      </vs-row>
      
      <vs-row>
        <vs-input type="file" @change="OnFileSelected" />
        <button @click="onUpload">UpLoad</button>
      </vs-row>
    </vs-col>
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
      value: '',
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
      fd.append('genre_id', this.value)
      fd.append('file', this.file)
      fd.append('title', this.title)
      fd.append('body', this.body)
      console.log(fd)
      axios.post('http://localhost:3000/upload', fd)
        .then((response) => {
          console.log(this.value)
          console.log(response)
          this.$router.push({ name: 'Main' })
        })
    },
    GetGenre() {
      const path = "http://localhost:3000/Genre";
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
    this.GetGenre();
  },
}
</script>