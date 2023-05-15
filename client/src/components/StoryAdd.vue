<template>
    <div class="container" style="display: flex; margin-left: 16%; margin-right: 8.33%;">
      <vs-col offset="1" style="margin-top: 11%;">
        <vs-row>
          <vs-select placeholder="Select" v-model="value">
            <vs-option label="Vuesax" value="1">
              Vuesax
            </vs-option>
            <vs-option label="Vue" value="2">
              Vue
            </vs-option>
            <vs-option label="Javascript" value="3">
              Javascript
            </vs-option>
            <vs-option disabled label="Sass" value="4">
              Sass
            </vs-option>
            <vs-option label="Typescript" value="5">
              Typescript
            </vs-option>
            <vs-option label="Webpack" value="6">
              Webpack
            </vs-option>
            <vs-option label="Nodejs" value="7">
              Nodejs
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

  export default {
    data(){
      return {
        title: '',
        body: '',
        value: '',
        file: null
      }
    },
    methods: {
      OnFileSelected(event){
        this.file = event.target.files[0]
        console.log(event)
      },
      onUpload(){
        const fd = new FormData();
        fd.append('file', this.file)
        fd.append('title', this.title)
        fd.append('body', this.body)
        console.log(fd)
        axios.post('http://localhost:3000/upload', fd)
        .then((response) => {
             console.log(response)
         })
      }
    }
  }
</script>

