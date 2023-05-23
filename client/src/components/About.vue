<template>
    <div class="containerInfo animate__animated animate__fadeIn" style="animation-duration: 1s;">
        <vs-row justify="space-around">
        <vs-alert :page.sync="page" shadow color="success" style="margin-left: 8%; z-index: 0;">
        <template #title>
            ThrillTogether с точки зрения проектной деятельности
        </template>
        
        <template #page-1>
        Задача этого сайта - применение наших навыков на деле, оттачивание знаний и практика работы в команде.
      </template>

      <template #page-2>
        Идея сайта позволяет полностью реализовать наши навыки: как в работе с бэкендом так и с фронтендом.
      </template>

      <template #page-3>
        В ходе работы над сайтом получен экспириенс работы в команде.
      </template>
      </vs-alert>
      <div class="videoContainer">
        <video controls class="video">
          <source src="../assets/video.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
    </vs-row>
    <vue-particles
        color="#6A4E93"
        :particleOpacity="0.7"
        :particlesNumber="130"
        shapeType="circle"
        :particleSize="4"
        linesColor="#6A4E93"
        :linesWidth="1.2"
        :lineLinked="true"
        :lineOpacity="0.5"
        :linesDistance="160"
        :moveSpeed="2"
        :hoverEffect="false"
        hoverMode="grab"
        :clickEffect="false"
        clickMode="push"
        style="position:absolute; z-index: -10; height: 80%; width: 100vw; left: 0%; top: 8%;"
      > </vue-particles>
    </div>
</template>

<script>
    export default {
      data:() => ({
        page: 1
      })
    }
  </script>

<style>
.containerInfo {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  padding-left: 16%;
  padding-right: 7%;
  padding-top: 8%;
}
.videoContainer {
  padding-left: 8%;
  padding-top: 4%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.video {
  max-width: 100%;
  height: auto;
}
</style>