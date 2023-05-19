<template>
  <div id="app">
    <link href="https://fonts.googleapis.com/css2?family=Unbounded&display=swap" rel="stylesheet">
      <sidebar style="z-index: 10;">
      </sidebar>
      <logoheader/>
    <router-view/>
    <myfooter style="z-index: 10;"></myfooter>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
@import 'assets/css/reset.css';

#app {
  background-color: #2A2A35;
  font-family: 'Unbounded';
  scroll-behavior: smooth;
}

body {
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
</style>
