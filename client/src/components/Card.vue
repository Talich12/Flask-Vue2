<template>
    <vs-card @click="onClick()" style="margin-top: 7%;">
        <template #title>
            <h3><slot name="title"></slot></h3>
        </template>
        <template #img>
            <slot name="img"></slot>
        </template>
        <template #text>
        <p>
            <slot name="text"></slot>
        </p>
        </template>
        <template #interactions>
        <vs-button danger icon>
            <i class='bx bx-heart'></i>
            <span class="span">
            {{like_count}}
            </span>
        </vs-button>
        <vs-button class="btn-chat" shadow primary>
            <i class='bx bx-chat' ></i>
            <span class="span">
            {{comment_count}}
            </span>
        </vs-button>
        </template>
    </vs-card>
</template>

<script>
import axios from 'axios';
export default {
    props:['id', 'comment_count', 'like_count'],
    data() {
      return {
        len: 1,
        page: 1,
        value: 4,
      };
    },
    methods:{
        onClick(){
            const path = "http://localhost:3000/post/" + this.$props.id;
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