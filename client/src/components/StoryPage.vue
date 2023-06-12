
<template>
    <div class="center" style="height: 100%;">
      <vs-dialog scroll blur overflow-hidden not-close v-model="active" style="padding-top: 0; padding-bottom: 0; overflow-y: hidden;">
        <div class="storyheader" style="margin-bottom: 3vh; display: flex; align-items: center;">
          <vs-avatar>
          <img :src="require(`@/assets/img/load/${post_data.post.author.avatar}`)" alt="">
        </vs-avatar>
        <p style="font-size: 3vh; margin-left: 1vw;">{{ post_data.post.author.username }}</p>
        <vs-button
          v-if="post_data.post.has_video"
          color="#FF0000"
          border
          upload
          style="margin-left: 8vw;"
        >
          <i class="bx bxl-youtube"></i> Видео на youtube!
        </vs-button>
        <vs-button
          v-if="post_data.post.has_audio"
          danger
          border
          upload
        >
          <i class="bx bxs-microphone-alt"></i> Озвучка истории!
        </vs-button>
        </div>
        <div style="display: flex; flex-direction: column; margin: 1vh; padding: 0.5vh; align-items: center;">
          <hr class="rounded2" style="margin-top: -1vh; border-top: 0.2vh solid #6A4E93; width: 14vw;">
          <p>Жанры: <p style="color: #6A4E93; font-style: italic; margin-top: 1vh;">{{ post_data.post.genre }}</p></p>
          <hr class="rounded2" style="margin-top: 2vh; border-top: 0.2vh solid #6A4E93; width: 18vw;">
          <p>История написана: <p style="color: #6A4E93; font-style: italic; margin-top: 1vh;">{{ formattedTimestamp }}</p></p>
          <hr class="rounded2" style="margin-top: 2vh; border-top: 0.2vh solid #6A4E93; width: 14vw;">
        </div>
        <template #header>
          <h2>
            {{ post_data.post.title }}
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
          <p>{{post_data.post.like_count}}</p>
          <span v-if="!post_data.has_liked">
            <i class='bx bx-heart' ></i>
          </span>
          <i class='bx bxs-heart' v-else ></i>
          </vs-button>
          <vs-button 
            @click="addSave()"
            success
            floating
            icon
            border
          >
          <span v-if="post_data.has_saved">
            <i class='bx bx-bookmark' ></i>
          </span>
          <i class='bx bxs-bookmark' v-else ></i>
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
            @click="addFollow()"
            success
            floating
            icon
            border
            v-if="post_data.has_followed != 2"
          >
          <span v-if="post_data.has_followed == 1">
            <i class='bx bxs-user-plus'  ></i>Подписаться на автора
          </span>
          <span v-if="post_data.has_followed == 0">
          <i class='bx bxs-user-minus'  ></i>Отписаться от автора
          </span>
          </vs-button>
          <vs-button
            @click="deletePost()"
            color="#FF0000"
            floating
            icon
            border
            v-if="post_data.has_followed == 2"
          >
            <i class='bx bx-x'  ></i>Удалить пост
          </vs-button>
        </div>
        <hr class="rounded2" style="margin: 3vh auto 1vh; margin-bottom: 3vh; border-top: 0.2vh solid #6A4E93; width: 15vw;">
        <h2><i class='bx bx-comment-detail' style="margin-right: 0.5vw;"></i>Комментарии:</h2>
        <div style="display: flex;">
        <vs-input border v-model="text" placeholder="Прокомментировать..." style="margin: 1vh; width: 100%;" class="multiline-input"/>
        <vs-button
        @click="addComment()"
        border
        icon
        danger 
        :class="{ 'shake-animation': isCommentAdded }"
        style="width: 100px"
      >
        <i class="bx bx-send"></i>
      </vs-button>
        </div>
        <div v-for="comment in post_data.comments" :class="{ 'shake-animation': isCommentAdded }">
          <usercomment :comment_data="comment" ></usercomment>
        </div>
      </vs-dialog>
    </div>
  </template>

<script>
import axios from 'axios';
import marked from 'marked';
  export default {
    props: ['post_data', 'active'],
    data:() => ({
      success: false,
      text: '',
      activebtn: '',
      markdown:  ``,
      isCommentAdded: false,
    }),
    methods:{
      addLike(){
        const path = "http://localhost:3000/post/like";
        axios.post(path, {post_id: this.$props.post_data.post.id},{
            headers: {
                'Authorization': 'Bearer ' + this.$cookies.get("access_token")
            }
        })
            .then((response) => {
            console.log(response.data);
            this.FetchData();
        })
            .catch((error) => {
            console.log(error);
        });
      },
      addComment() {
        if (this.text.trim() !== '') {
          let filteredText = this.replaceCurseWords(this.text);

          const path = "http://localhost:3000/post/comment";
          axios.post(path, { post_id: this.$props.post_data.post.id, text: filteredText }, {
              headers: {
                  'Authorization': 'Bearer ' + this.$cookies.get("access_token")
              }
          })
          .then((response) => {
              this.text = '';
              this.FetchData();
              console.log(response.data);
          })
          .catch((error) => {
              console.log(error);
          });

          this.isCommentAdded = true;
          setTimeout(() => {
              this.isCommentAdded = false;
          }, 1000);
        }
      },

      replaceCurseWords(text) {
        const curseWords = ['бля', 'хуйня', 'пиздец', 'гладиолус'];
        for (const word of curseWords) {
          const regex = new RegExp(word, 'gi');
          text = text.replace(regex, '*'.repeat(word.length));
        }
        return text;
      },
      addSave(){
        const path = "http://localhost:3000/post/save";
        axios.post(path, {post_id: this.$props.post_data.post.id},{
            headers: {
                'Authorization': 'Bearer ' + this.$cookies.get("access_token")
            }
        })
            .then((response) => {
              console.log(response.data);
              this.FetchData();
        })
            .catch((error) => {
            console.log(error);
        });
      },
      addFollow(){
        const path = "http://localhost:3000/post/follow";
        axios.post(path, {user_id: this.$props.post_data.post.author.id},{
            headers: {
                'Authorization': 'Bearer ' + this.$cookies.get("access_token")
            }
        })
            .then((response) => {
              this.FetchData();
              console.log(response.data);
        })
            .catch((error) => {
            console.log(error);
        });
      },
      FetchData(){
        const path = "http://localhost:3000/post/" + this.$props.post_data.post.id;
            axios.get(path,{
                headers: {
                    'Authorization': 'Bearer ' + this.$cookies.get("access_token")
                }
            })
                .then((response) => {
                  this.post_data = response.data
                  
            })
                .catch((error) => {
                console.log(error);
            })
      },
      deletePost(){
        const path = "http://localhost:3000/post/" + this.$props.post_data.post.id + "/delete";
        axios.delete(path,{
                headers: {
                    'Authorization': 'Bearer ' + this.$cookies.get("access_token")
                }
            })
                .then((response) => {
                  this.post_data = response.data
                  window.location.reload();
            })
                .catch((error) => {
                console.log(error);
            })
      }
    },
    computed: {
        formattedTimestamp() {
          const timestamp = this.$props.post_data.post.timestamp;
          const date = new Date(timestamp);
          const year = date.getFullYear();
          const month = String(date.getMonth() + 1).padStart(2, '0');
          const day = String(date.getDate()).padStart(2, '0');
          return `${year}-${month}-${day}`;
        },
        markdownToHtml(){
            return marked(this.$props.post_data.post.body);
        }
    }
}  
  </script>

<style>
.shake-animation {
  animation: shake 0.35s;
}

@keyframes shake {
  0% {
    transform: translateX(0);
  }
  20% {
    transform: translateX(-5px);
  }
  40% {
    transform: translateX(5px);
  }
  60% {
    transform: translateX(-5px);
  }
  80% {
    transform: translateX(5px);
  }
  100% {
    transform: translateX(0);
  }
}
.vs-input-parent--border .vs-input-content .vs-input {
  width: 100%;
  line-break:anywhere;
  margin-right: 1vh;
}
.vs-dialog {
    background: #2A2A35;
    color: #EEEFF9;
    z-index: 10000000000;
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