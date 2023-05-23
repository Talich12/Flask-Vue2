<template>
  <div id="app">
    <link href="https://fonts.googleapis.com/css2?family=Unbounded&display=swap" rel="stylesheet">
      <sidebar style="z-index: 10; animation-duration: 0.5s;" class="animate__animated animate__fadeIn">
      </sidebar>
      <logoheader style="animation-duration: 0.7s;" class="animate__animated animate__fadeIn"/>
    <router-view/>
    <myfooter style="z-index: 10; position: relative; bottom: 0;"></myfooter>
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

.vs-sidebar__item {
  font-family: 'Unbounded';
}
</style>
