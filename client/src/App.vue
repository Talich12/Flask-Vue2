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
  font-family: 'Unbounded', cursive;
  font-weight: 100;
  background-color: #2A2A35;
}

body {
  background-color: #2A2A35;
}

.vs-card{
  max-width: 100%;
  background-color:rgb(68, 68, 78);
  color:rgb(238, 239, 249);
}

.vs-raw{
  margin-top: 15%;
}

#app {
  height: 100vh;
  overflow-y: auto;
  scrollbar-color: rgb(106, 78, 147) #FFFFFF;
}

/* Style the scrollbar track */
#app::-webkit-scrollbar-track {
  background-color: #FFFFFF;
}
</style>
