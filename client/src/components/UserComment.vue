<template>
    <div class="usercard" style="align-items: center; border: 0.2vh solid #6A4E93; border-radius: 15px; margin-top: 2vh; margin-bottom: 1.5vh;">
        <div style="display: flex; align-items: center; margin: 2vh;">
        <vs-avatar style="margin-right: 1vw;">
            <img :src="require(`@/assets/img/load/${comment_data.user.avatar}`)" alt="">
        </vs-avatar>
        <p style="font-weight: bolder;">{{ comment_data.user.username }}</p>
        </div>
        <p style="margin: 2vh">{{ comment_data.text }}</p>
    </div>
</template>

<script>
  export default {
    props: ['comment_data'],
    data:() => ({
    })
}  
  </script>