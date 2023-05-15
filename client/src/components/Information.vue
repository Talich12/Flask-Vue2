<template>
    <vs-alert relief color="dark" :page.sync="page" class="alert-custom" style="z-index: 0;">
      <template #title>
        Рекомендации
      </template>
  
      <template #page-1>
        Здесь подборка для вас на сегодня:
      </template>
  
      <template #page-2>
        Подборка обновляется каждые два дня
      </template>
  
      <template #page-3>
        Подборка генерируется на основе ваших предпочтений
      </template>
    </vs-alert>
  </template>
  
  <script>
  export default {
    data: () => ({
      page: 1,
    }),
  };
  </script>
  
  <style>
  .alert-custom {
    align-self:flex-start;
    text-align: left;
  }
  </style>
  