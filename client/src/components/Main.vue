<template>
    <div class="container" style="display: flex; margin-left: 16%; margin-right: 8.33%;">
        <vs-row justify="space-around" style="margin-top: 6%;">
            <vs-col v-for="post in this.Data" offset="1" w="5">
            <card>
                <template #title>
                    {{post.title}}
                </template>
                <template #text>
                    {{post.body}}
                </template>
                <template #img>
                    <img :src="require(`@/assets/${post.img}`)" alt="">
                </template>
            </card>
        </vs-col>
        </vs-row>
    </div>
  </template>
  
<script>
import axios from 'axios';

export default {
name: 'index',
data() {
    return {
        Data: []
    };

},
methods: {
    Get(){
    const path = 'http://localhost:3000/'; 
    axios.get(path)
    .then((response) => {
        console.log(response.data)
        const data = response.data;
        this.Data = data
    })
    .catch((error) =>{
        console.log(error)
    })
    },
},
created(){
    this.Get();
},
};
</script>