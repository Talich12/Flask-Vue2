<template>
  <vs-alert border :hidden-content.sync="hidden" color="danger">
    <template #title>
      Рекомендации на сегодня
    </template>
    Обновления происходят каждые два дня чтобы вы все успели прочесть. Рекомендации строятся на основе ваших предпочтений. Не забывайте ставить оценки историям чтобы улучшить систему рекомендаций.
  </vs-alert>
</template>

<script>
  export default {
    data:() => ({
      hidden: true
    })
  }
</script>
  
  <style>
  .alert-custom {
    align-self:flex-start;
    text-align: left;
  }
  </style>