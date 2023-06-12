<template>
  <div class="header">
    <div class="image-container" ref="imageContainer">
      <img src="../assets/tt.svg" alt="" class="image" style="z-index: 100;">
      <img src="../assets/tteye.svg" alt="" class="pupil" ref="pupil">
    </div>
    <p style="color: rgb(106, 78, 147); display: flex; justify-self: flex-end; align-self: flex-start;">&beta;</p>
  </div>
</template>

<style>
.header {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 10%;
  width: 100%;
  position: fixed;
  z-index: 2;
  top: 0;
  left: 0;
  background-color: #2A2A35;
  -webkit-box-shadow: 0 0 25px 0 rgba(0,0,0,0.4);
  -moz-box-shadow: 0 0 25px 0 rgba(0,0,0,0.4);
  box-shadow: 0 0 25px 0 rgba(0,0,0,0.4);
}

.image-container {
  position: relative;
  padding: 2vh;
  display: flex;
  width: 40vw;
  height: 100%;
  margin-left: 16%;
  justify-content: center;
  align-items: center;
}

.image,
.pupil {
  position: absolute;
  height: 8vh;
  transition: transform 0.3s ease-out;
}
</style>

<script>
export default {
  mounted() {
    this.addMouseMoveListener();
    window.addEventListener('resize', this.updatePupilPosition);
  },
  beforeUnmount() {
    this.removeMouseMoveListener();
    window.removeEventListener('resize', this.updatePupilPosition);
  },
  methods: {
    addMouseMoveListener() {
      document.addEventListener('mousemove', this.updatePupilPosition);
    },
    removeMouseMoveListener() {
      document.removeEventListener('mousemove', this.updatePupilPosition);
    },
    updatePupilPosition(event) {
    const pupil = this.$refs.pupil;
    const imageContainer = this.$refs.imageContainer;
    const rect = imageContainer.getBoundingClientRect();

    // Calculate the position of the mouse relative to the image container
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;

    // Calculate the maximum range of movement for the pupil within the image container
    const maxX = 9;
    const maxY = 5;

    // Calculate the position of the pupil based on the mouse coordinates
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const distanceX = mouseX - centerX;
    const distanceY = mouseY - centerY;

    // Calculate the distance ratio within the radius
    const radius = 100;
    const distanceRatioX = Math.min(Math.max(distanceX, -radius), radius) / radius;
    
    // Clamp the distanceY value within a certain range
    const clampedDistanceY = Math.min(Math.max(distanceY, -radius), radius);
    const distanceRatioY = clampedDistanceY / radius;

    // Calculate the position of the pupil within the maximum range
    const pupilX = (distanceRatioX * maxX + maxX / 2 -4);
    const pupilY = (distanceRatioY * maxY + maxY / 2);

    // Update the position of the pupil
    pupil.style.transform = `translate(${pupilX}px, ${pupilY}px)`;
  },

  },
};
</script>
