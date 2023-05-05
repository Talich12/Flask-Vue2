<template>
  <div id="app" >
      <sidebar style="z-index: 10;">
      </sidebar>
      <logoheader/>
    <router-view/>
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
}


.vs-card{
  max-width: 100%;
  background-color:rgb(68, 68, 78);
  color:rgb(238, 239, 249);
}

.vs-raw{
  margin-top: 15%;
}
</style>
