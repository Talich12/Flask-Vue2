<template>
    <div class="containerInfo">
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
  margin-left: 16%;
  margin-right: 7%;
  margin-top: 8%;
}
.videoContainer {
  margin-left: 8%;
  margin-top: 4%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.video {
  max-width: 100%;
  height: auto;
}
</style>