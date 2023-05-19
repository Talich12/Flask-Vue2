<template>
  <vs-alert border :hidden-content.sync="hidden" color="danger">
    <template #title>
      <slot name="title"></slot>
    </template>
    <p><slot name="text"></slot></p>
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