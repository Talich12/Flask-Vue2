<template>
    <div
      class="bg-container"
    >
      <div class="spotlight"></div>
    </div>
  </template>
  <script>
    export default {
      name: 'VSpotlight',
      data() {
        return {
          spotlight: null,
          spotlightSize: 'transparent 160px, rgba(0, 0, 0, 0.85) 200px)',
        };
      },
      mounted() {
        const t = this;
        t.spotlight = document.querySelector('.spotlight');
        window.addEventListener('mousemove', (e) => {
          t.updateSpotlight(e);
        });
      },
      methods: {
        updateSpotlight(e) {
          const t = this;
          t.spotlight.style.backgroundImage = `radial-gradient(circle at ${
            (e.pageX / window.innerWidth) * 100
          }% ${(e.pageY / window.innerHeight) * 100}%, ${t.spotlightSize}`;
        },
      },
    };
  </script>
  <style scoped>
    .spotlight {
      pointer-events: none;
      z-index: 1000;
      position: absolute;
      right: 2px;
      bottom: 2px;
      height: 100%;
      width: 100%;
      background-image: radial-gradient(
        circle,
        transparent 160px,
        rgba(0, 0, 0, 0.85) 200px
      );
    }
  </style>