
<template>
    <div class="center" style="height: 100%;">
      <vs-dialog scroll blur overflow-hidden not-close v-model="active" style="padding-top: 0; padding-bottom: 0; overflow-y: hidden;">
        <div class="storyheader" style="margin-bottom: 3vh; display: flex; align-items: center;">
          <vs-avatar>
          <img :src="require(`@/assets/img/load/${post_data.author.avatar}`)" alt="">
        </vs-avatar>
        <p style="font-size: 3vh; margin-left: 1vw;">{{ post_data.author.username }}</p>
        <vs-button
          v-if="post_data.has_video"
          color="#FF0000"
          border
          upload
          :activebtn="activebtn == 2"
          @click="active = 2"
          style="margin-left: 8vw;"
        >
          <i class="bx bxl-youtube"></i> Видео на youtube!
        </vs-button>
        <vs-button
          v-if="post_data.has_audio"
          danger
          border
          upload
          :activebtn="activebtn == 2" 
          @click="active = 2"
        >
          <i class="bx bxs-microphone-alt"></i> Озвучка истории!
        </vs-button>
        </div>
        <div style="display: flex; flex-direction: column; margin: 1vh; padding: 0.5vh; align-items: center;">
          <hr class="rounded2" style="margin-top: -1vh; border-top: 0.2vh solid #6A4E93; width: 14vw;">
          <p>Жанры: {{ post_data.genre }}</p>
          <hr class="rounded2" style="margin-top: 2vh; border-top: 0.2vh solid #6A4E93; width: 18vw;">
          <p>История написана: {{ post_data.timestamp }}</p>
          <hr class="rounded2" style="margin-top: 2vh; border-top: 0.2vh solid #6A4E93; width: 14vw;">
        </div>
        <template #header>
          <h2>
            {{ post_data.title }}
          </h2>
        </template>
        <div class="con-content" style="margin-bottom: 2vh;">
             <div v-html="markdownToHtml"></div>
        </div>
        <hr class="rounded2" style="margin: 7vh auto 1vh; margin-bottom: 3vh; border-top: 0.2vh solid #6A4E93; width: 15vw;">
        <div style="display: flex; justify-content: center;">
          <vs-button
            @click="addLike()"
            color="#FF0000"
            floating
            icon
            border
          >
          <p>{{post_data.like_count}}</p>
            <i class='bx bxs-heart' ></i>
          </vs-button>
          <vs-button 
            success
            floating
            icon
            border
          >
            <i class='bx bxs-bookmark' ></i>
          </vs-button>
          <vs-button
            success
            floating
            icon
            border
          >
            <i class='bx bx-share' ></i>
          </vs-button>
          <vs-button
            warn
            floating
            icon
            border
          >
            <i class='bx bx-error' ></i>
          </vs-button>
          <vs-button
            success
            floating
            icon
            border
          >
            <i class='bx bxs-user-plus' ></i>Подписаться на автора
          </vs-button>
        </div>
        <hr class="rounded2" style="margin: 3vh auto 1vh; margin-bottom: 3vh; border-top: 0.2vh solid #6A4E93; width: 15vw;">
        <h2><i class='bx bx-comment-detail' style="margin-right: 0.5vw;"></i>Комментарии:</h2>
        <div style="display: flex;">
        <vs-input border v-model="value" placeholder="Прокомментировать..." style="margin: 1vh; width: 100%;" class="multiline-input"/>
        <vs-button
        icon
        danger
        flat
        :active="active == 1"
        @click="active = 1"
      >
        <i class="bx bx-send"></i>
      </vs-button>
        </div>
        <usercomment></usercomment>
        <usercomment></usercomment>
      </vs-dialog>
    </div>
  </template>

<script>
import axios from 'axios';
import marked from 'marked';
  export default {
    props: ['post_data', 'active'],
    data:() => ({
      activebtn: '',
      markdown:  ``,
    }),
    methods:{
      addLike(){
        const path = "http://localhost:3000/post/like";
        axios.post(path, {post_id: this.$props.post_data.id},{
            headers: {
                'Authorization': 'Bearer ' + this.$cookies.get("access_token")
            }
        })
            .then((response) => {
            console.log(response.data);
            if (response.data.Status == "add_like")
              this.$props.post_data.like_count++
            else{
              this.$props.post_data.like_count--
            }
        })
            .catch((error) => {
            console.log(error);
        });
      }
    },
    computed: {
        markdownToHtml(){
            return marked(this.$props.post_data.body);
        }
    }
}  
  </script>

<style>
.vs-input-parent--border .vs-input-content .vs-input {
  width: 100%;
  line-break:anywhere;
  margin-right: 1vh;
}
.vs-dialog {
    background: #2A2A35;
    color: #EEEFF9;
}
.vs-dialog--scroll {
    max-width:none;
    width: 50vw;
    height: 100%;
    padding: 0;
    margin: 0;
}
.vs-dialog__content.notFooter {
    max-height: 100vh;
    height: 90vh;
    margin-bottom: 0;
}
code {
  color: #f66;
}

h1, h2, h3, h4, h5, h6 {
  margin-top: 1em;
  margin-bottom: 0.5em;
  font-weight: bold;
}

h1 {
  font-size: 2em;
}

h2 {
  font-size: 1.5em;
}

h3 {
  font-size: 1.17em;
}

h4 {
  font-size: 1em;
}

h5 {
  font-size: 0.83em;
}

h6 {
  font-size: 0.67em;
}

strong {
  font-weight: bold;
}

em {
  font-style: italic;
}

blockquote {
  margin: 1em 0;
  padding: 0.5em 1em;
  background-color: rgb(42, 42, 53);
  border-left: 2px solid #f66;
}

ol {
  margin: 1em 0;
  padding-left: 2em;
}

ul {
  margin: 1em 0;
  padding-left: 2em;
}

li {
  margin-bottom: 0.5em;
}

code {
  background-color: rgb(42, 42, 53);
  padding: 0.2em 0.4em;
  font-family: "Monaco", courier, monospace;
}

hr {
  border: none;
  border-top: 1px solid #f66;
  margin: 1em 0;
}
img {
    max-width: 100%;
    height: auto;
}
</style>