<template>
    <div class="cookie">
    <vs-button
        upload
        color="danger"
        transparent
        :active="active == 5"
        @click="active = 5"
        style="width: 100%;"
      >
        Согласен
      </vs-button>
      </div>
</template>

<script>
export default {
  data:() => ({
    active: 0
  })
}
</script>

<style>
.cookie {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content:baseline;
}
</style>