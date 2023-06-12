<template>
    <vs-card @click="onClick()" style="margin-top: 7%;">
        <template #title>
            <h3>{{post.title}}</h3>
        </template>
        <template #img>
            <img :src="require(`@/assets/img/load/${post.img}`)" alt="">
        </template>
        <template #text>
        <p>
            {{ post.author.username }}
        </p>
        </template>
        <template #interactions>
        <vs-button danger icon>
            <i class='bx bx-heart'></i>
            <span class="span">
            {{post.like_count}}
            </span>
        </vs-button>
        <vs-button danger icon>
            <i class='bx bx-chat' ></i>
            <span class="span">
            {{post.comment_count}}
            </span>
        </vs-button>
        <vs-button v-if="post.has_audio == true" primary icon>
            <i class='bx bxs-microphone-alt' ></i>
            <span class="span">
            </span>
        </vs-button>
        <vs-button  v-if="post.has_video == true" primary icon>
            <i class='bx bxs-film' ></i>
            <span class="span">

            </span>
        </vs-button>
        <vs-button v-if="post.has_curse == true" color="#FF0000" icon>
            <i class='bx bx-angry' ></i>
            <span class="span">
            </span>
        </vs-button>
        <vs-button v-if="post.has_violence == true" color="#FF0000" icon>
            <i class='bx bx-knife' ></i>
            <span class="span">
            </span>
        </vs-button>
        </template>
    </vs-card>
</template>

<script>
import axios from 'axios';
export default {
    props:['post'],
    data() {
      return {
        len: 1,
        page: 1,
        value: 4,
      };
    },
    methods:{
        onClick(){
            const path = "http://localhost:3000/post/" + this.$props.post.id;
            axios.get(path)
                .then((response) => {
                this.$emit('data', response.data)
            })
                .catch((error) => {
                console.log(error);
            })
        }
    }
}
</script>