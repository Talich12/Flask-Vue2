<template>
  <div id="app">
    <cookie></cookie>
    <link href="https://fonts.googleapis.com/css2?family=Unbounded&display=swap" rel="stylesheet">
      <sidebar @video="onVideo" @audio="onAudio" style="z-index: 10; animation-duration: 0.5s;" class="animate__animated animate__fadeIn">
      </sidebar>
      <logoheader style="animation-duration: 0.7s;" class="animate__animated animate__fadeIn"/>
    <router-view  :audio="audio" :video="video" />
    <myfooter style="z-index: 10; position: relative; bottom: 0;"></myfooter>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    audio: false,
    video: false,
  }),
  methods:{
    onVideo(data){
      this.video = data.video
    },
    onAudio(data){
      this.audio = data.audio
    }
  }
};
</script>

<style>
@import 'assets/css/reset.css';

#app {
  background-color: #2A2A35;
  font-family: 'Unbounded';
}

body {
  overflow-y: hidden;
  background-color: #2A2A35;
  font-family: 'Unbounded';
}

.vs-card{
  max-width: 100%;
  background-color:rgb(48, 48, 58);
  color:rgb(238, 239, 249);
}

#app {
  height: 100vh;
  overflow-y: auto;
  scrollbar-color: rgb(106, 78, 147) rgb(68, 68, 78);
}

.vs-sidebar__item {
  font-family: 'Unbounded';
}

:root {
  --vs-shadow-opacity: 0.35; /* Set the desired value for --vs-shadow-opacity */
}

.vs-avatar img {
  height: 105%;
  width: 105%;
}
#vs-input--inputstoryimg {
  min-width: 200px;
}
::-webkit-file-upload-button {
   display: none;
}
::file-selector-button {
  display: none;
}
.vs-input-parent--border .vs-input-content .vs-input {
  color: #EEEFF9;
}
.vs-dialog__close i::before {
  background: #EEEFF9
}
.vs-dialog__close i::after {
  background: #EEEFF9
}
</style>
