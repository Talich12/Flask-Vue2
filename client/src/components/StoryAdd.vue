<template>
    <div class="container" style="display: flex; margin-left: 16%; margin-right: 8.33%;">
      <vs-col offset="1" style="margin-top: 11%;">
        <vs-select
          label="Жанр"
          filter
          multiple
          collapse-chips
          placeholder="Collapse chips"
          v-model="value3"
        >
        <template #message-danger>
          Выберите жанры которые подходят вашей истории
        </template>
          <vs-option label="Vuesax" value="1">Vuesax</vs-option>
          <vs-option label="Vue" value="2">Vue</vs-option>
          <vs-option label="Javascript" value="3">Javascript</vs-option>
          <vs-option label="Sass" value="4">Sass</vs-option>
          <vs-option label="Typescript" value="5">Typescript</vs-option>
          <vs-option label="Webpack" value="6">Webpack</vs-option>
          <vs-option label="Nodejs" value="7">Nodejs</vs-option>
        </vs-select>
      </vs-col>

      <vs-col style="margin-top: 11%;">
        <vs-input
        label-placeholder="Название"
        v-model="value"
      />
      </vs-col>
      <vs-row>
        <vs-input
        label-placeholder="Текст"
        v-model="value"
      />
      </vs-row>
      <vs-row>
        <vs-input type="file"
        accept="image/*" @change="uploadImage($event)" 
                                     id="file-input"
        label-placeholder="Обложка"
        v-model="value"
      />
      </vs-row>

    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        value2: ['1', '4', '5', '6'],
      };
    },
    methods: {
        uploadImage(event) {

const URL = 'api/v1/chats/image';

let data = new FormData();
data.append('name', 'my-picture');
data.append('file', event.target.files[0]);
data.append('chatid', this.chat);
data.append('senderid', this.auth_id);

let config = {
    header: {
        'Content-Type': 'image/png'
    }
};

axios.post(URL, data, config).then(
    response => {
        console.log('image upload response > ', response)
      }
  )
},
    }
  };
  </script>
  