<template>
  <div class="totop">
    <vs-button
      color="rgb(106, 78, 147)"
      circle
      icon
      floating
      @click="scrollTop"
    >
      <i class='bx bx-up-arrow-alt' style="font-size: xx-large;"></i>
    </vs-button>
  </div>
</template>

<style>
.totop {
  z-index: 30;
  position: fixed;
  bottom: 5%;
  right: 4%;
}
</style>

<script>
export default {
  methods: {
    scrollTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }
  }
};
</script>
