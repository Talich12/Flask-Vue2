<template>
      <vs-card-group style="margin-left: 8%; margin-top: 2%;">
        <div v-for="post in $props.data">
          <card @data="Open" :comment_count="post.comment_count" :like_count="post.like_count" :id="post.id">
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
        </div>
  </vs-card-group>
</template>

<script>
export default {
  props:['data'],
  data() {
      return {
      
      };
  },
  methods:{
    Open(data){
      this.$emit('data', data)
    }
  }
}
</script>